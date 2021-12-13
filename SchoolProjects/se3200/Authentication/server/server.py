from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import parse_qs
import json
import os.path
from tasks_db import TasksDB

from http import cookies
from session_store import SessionStore

SESSION_STORE = SessionStore()


class MyRequestHandler(BaseHTTPRequestHandler):

    def load_cookie(self):
        print("headers", self.headers)

        #if request headers contain cookie data
        if "Cookie" in self.headers:
            #load cookie data from the request headers
            self.cookie = cookies.SimpleCookie(self.headers["Cookie"])
        else:
            self.cookie = cookies.SimpleCookie()


    def send_cookie(self):
        for morsel in self.cookie.values():
            self.send_header("Set-Cookie", morsel.OutputString())


        #save the session for the CURRENT client into self.session
    def load_session(self):
        # upon client request
        # Use self.cookie() & session store
        self.load_cookie()
        # check if session ID cookie exists
        if "sessionId" in self.cookie:
        #if it does
            #load session from session store using session ID
            sessionID = self.cookie["sessionId"].value
            self.sessionData = SESSION_STORE.getSessionData(sessionID)
            # if cannot load session (invalid session ID)
            if self.sessionData == None:
                sessionID = SESSION_STORE.createSession()
                self.cookie["sessionId"] = sessionID
                self.sessionData = SESSION_STORE.getSessionData(sessionID)
                #create a new session with a new session ID
                # set the new session ID into the session ID cookie

        else:
            sessionID = SESSION_STORE.createSession()
            self.cookie["sessionId"] = sessionID
            self.sessionData = SESSION_STORE.getSessionData(sessionID)
        
        self.cookie["sessionId"]["samesite"] = "None"
        self.cookie["sessionId"]["secure"] = True


    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", self.headers['Origin'])
        self.send_header("Access-Control-Allow-credentials", "true")
        #BaseHTTPRequestHandler.end_headers(self)
        self.send_cookie()
        super().end_headers()
        

    def handleHello(self):
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            # headers go here, if any
            self.end_headers()
            # body goes here, if any
            self.wfile.write(bytes("Hello, world.", "utf-8"))


    def handleGetToDoList(self):

        if not self.userLoggedIn():
            return

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        
        self.end_headers()
        db = TasksDB()
        toDoList = db.getAllTasks()
        self.wfile.write(bytes(json.dumps(toDoList), "utf-8"))


    def handleGetOneTask(self, identifier):

        if not self.userLoggedIn():
            return
        
        db = TasksDB()
        item = db.getOneTask(identifier)
        if item:
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            
            self.end_headers()
            self.wfile.write(bytes(json.dumps(item), "utf-8"))
        else:
            self.handleNotFound()


    def handleAddToList(self):

        if not self.userLoggedIn():
            return

        # Read incoming Request Body
        contentLength = int(self.headers["Content-Length"])
        requestBody = self.rfile.read(contentLength).decode("utf-8")
        print("raw request body:", requestBody)

        # Parse data
        parsed_body = parse_qs(requestBody)
        print("parsed body", parsed_body)
        
        task = parsed_body['task'][0]
        dueDate = parsed_body['dueDate'][0]
        priority = parsed_body['priority'][0]
        progress = parsed_body['progress'][0]
        reference = parsed_body['reference'][0]

        db = TasksDB()
        db.createTask(task, dueDate, priority, progress, reference)
        
        self.send_response(201)
        self.end_headers()

        self.wfile.write((bytes("Created", "utf-8")))
    

    def handleUpdateTask(self, identifier):

        if not self.userLoggedIn():
            return

        db = TasksDB()
        task = db.getOneTask(identifier)

        if task:
            self.send_response(204)
            self.end_headers()

            contentLength = int(self.headers["Content-Length"])
            requestBody = self.rfile.read(contentLength).decode("utf-8")
            print("raw request body:", requestBody)

            # Parse data
            parsed_body = parse_qs(requestBody)
            print("parsed body", parsed_body)
            
            task = parsed_body['task'][0]
            dueDate = parsed_body['dueDate'][0]
            priority = parsed_body['priority'][0]
            progress = parsed_body['progress'][0]
            reference = parsed_body['reference'][0]

            db.modifyTask(identifier, task, dueDate, priority, progress, reference)
        else:
            self.handleNotFound()


    def handleDeleteTask(self, identifier):

        if not self.userLoggedIn():
            return

        db = TasksDB()
        task = db.getOneTask(identifier)

        if task:
            db.deleteTask(identifier)
            self.send_response(200)
            self.end_headers()
        else:
            self.handleNotFound()


    def handleNotFound(self):
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            # headers go here, if any
            self.end_headers()
            #body goes here
            self.wfile.write(bytes("Not Found.", "utf-8"))


    def handleNoUserFound(self):
        self.send_response(401)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Incorrect Login info", "utf-8"))


    def handleGetAllUsers(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        
        self.end_headers()
        db = TasksDB()
        toDoList = db.getAllUsers()
        self.wfile.write(bytes(json.dumps(toDoList), "utf-8"))

    
    def handleGetOneUser(self, identifier):
            db = TasksDB()
            user = db.getOneUserWithID(identifier)
            if user:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(bytes(json.dumps(user), "utf-8"))
            else:
                self.handleNotFound()


    def handleAddUser(self):
        # Read incoming Request Body
        contentLength = int(self.headers["Content-Length"])
        requestBody = self.rfile.read(contentLength).decode("utf-8")
        print("raw request body:", requestBody)

        # Parse data
        parsed_body = parse_qs(requestBody)
        print("parsed body", parsed_body)
        
        email = parsed_body['email'][0]
        firstName = parsed_body['firstName'][0]
        lastName = parsed_body['lastName'][0]
        password = parsed_body['password'][0]
        
        db = TasksDB()
        if db.getOneUserWithEmail(email):
            self.send_response(422)
            self.end_headers()

        else:
            db.createUser(email, firstName, lastName, password)
            self.send_response(201)
            self.end_headers()
            self.wfile.write((bytes("Created", "utf-8")))


    def handleUpdateUser(self, identifier):
        db = TasksDB()
        user = db.getOneUserWithEmail(identifier)

        if user:
            self.send_response(204)
            self.end_headers()

            contentLength = int(self.headers["Content-Length"])
            requestBody = self.rfile.read(contentLength).decode("utf-8")
            print("raw request body:", requestBody)

            # Parse data
            parsed_body = parse_qs(requestBody)
            print("parsed body", parsed_body)
            
            email = parsed_body['email'][0]
            firstName = parsed_body['firstName'][0]
            lastName = parsed_body['lastName'][0]
            password = parsed_body['password'][0]
            db.createUser(email, firstName, lastName, password)

        else:
            self.handleNotFound()


    def handleAuthenticateUser(self):
        contentLength = int(self.headers["Content-Length"])
        requestBody = self.rfile.read(contentLength).decode("utf-8")
        print("raw request body:", requestBody)

        # Parse data
        parsed_body = parse_qs(requestBody)
        print("parsed body", parsed_body)
        
        emailForUser = parsed_body['email'][0]
        userPassword = parsed_body['password'][0]
        
        print("username = ", emailForUser)
        print("password = ", userPassword)

        db = TasksDB()
        user = db.getOneUserWithEmail(emailForUser)
        print("user = ", user)
        self.sessionData["hello"] = "world"

        if user:
            if db.checkPassword(emailForUser, userPassword):
                self.send_response(201)
                self.end_headers()
                self.sessionData["userID"] = user["id"]
                print("Noice user")
            else:
                self.handleNoUserFound()
        else:
            self.handleNoUserFound()


    def handleDeleteUser(self, identifier):
        db = TasksDB()
        task = db.getOneUserWithID(identifier)

        if task:
            db.deleteUser(identifier)
            self.send_response(200)
            self.end_headers()
        else:
            self.handleNotFound()


    def userLoggedIn(self):
        #print(self.sessionData["userID"])
        #print(self.sessionData["hello"])
        if "userID" in self.sessionData:
            print("User Logged In")
            return True
        else:
            print("User Not Logged In")
            self.handleNoUserFound()
            return False


    def do_GET(self):
        self.load_session()

        print("The request path is: ", self.path)

        url_parts = self.path.split('/')
        collection = url_parts[1]

        if len(url_parts) > 2:
            idInDB = url_parts[2]
        else:
            idInDB = None

        if collection == "tasks":
            if idInDB:
                self.handleGetOneTask(idInDB)
            else:
                self.handleGetToDoList()
        
        elif collection == "adminusers":
            if idInDB:
                self.handleGetOneUserWithID(idInDB)
            else:
                self.handleGetAllUsers()

        elif collection == "hello":
            self.handleHello()
        else:
            self.handleNotFound()
    

    def do_POST(self):
        self.load_session()
        
        if self.path == "/tasks":
            self.handleAddToList()
        elif self.path == "/users":
            self.handleAddUser()
        elif self.path == "/sessions":
            self.handleAuthenticateUser()
        else:
            self.handleNotFound()


    def do_PUT(self):
        self.load_session()
        
        url_parts = self.path.split('/')
        collection = url_parts[1]
        if len(url_parts) > 2:
            idInDb = url_parts[2]
        else:
            idInDb = None
        
        if collection == "tasks":
            if idInDb:
                self.handleUpdateTask(idInDb)
        # elif collection == "users":
        #     if idInDb:
        #         self.handleUpdateUser(idInDb)
        else:
            self.handleNotFound()

        
    def do_DELETE(self):
        self.load_session()

        url_parts = self.path.split('/')
        collection = url_parts[1]
        # print("collection ", collection)
        
        if len(url_parts) > 2:
            idInDb = url_parts[2]
        else:
            idInDb = None
        
        if collection == "tasks":
            if idInDb:
                self.handleDeleteTask(idInDb)
        if collection == "adminusers":
            # print("entering delete user. ID = ", idInDb)

            if idInDb:
                self.handleDeleteUser(idInDb)
        else:
            self.handleNotFound()
    
    
    def do_OPTIONS(self):
        self.load_session()

        self.send_response(204)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    #start server
    
    listen = ("127.0.0.1", 8080)
    server = ThreadedHTTPServer(listen , MyRequestHandler)
    
    print("The server is running!")
    server.serve_forever()

    return

run()