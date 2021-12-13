from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
from urllib.parse import parse_qs
import json
from http import cookies
import random

from ticketsDB import TicketsDB

class MyRequestHandler(BaseHTTPRequestHandler):

  
    def load_cookie(self):
        print("headers and cookies", self.headers)

        if "Cookie" in self.headers:
            self.cookie = cookies.SimpleCookie(self.headers["Cookie"])
        else:
            self.cookie = cookies.SimpleCookie()


    def send_cookie(self):
        self.cookie["oompa"] = "loompa"
        self.cookie["oompa"]["samesite"] = "None"
        self.cookie["oompa"]["secure"] = True

        for morsel in self.cookie.values():
            self.send_header("Set-Cookie", morsel.OutputString())


    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", self.headers['Origin'])
        self.send_header("Access-Control-Allow-credentials", "true")
        #self.send_cookie()
        super().end_headers()


    def handelGetTickets(self):

        self.load_cookie()

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        db = TicketsDB()
        tickets = db.getTickets()
        self.wfile.write(bytes(json.dumps(tickets), "utf-8"))

    
    def handelAddTicket(self):

        self.load_cookie()

        contentLength = int(self.headers["Content-Length"])
        requestBody = self.rfile.read(contentLength).decode("utf-8")
        print("raw request body:", requestBody)

        parsed_body = parse_qs(requestBody)
        print("parsed body", parsed_body)
        
        ranNumber = random.randrange(0,7)
        entrant_name = parsed_body['entrant_name'][0]
        entrant_age = parsed_body['entrant_age'][0]
        guest_name = parsed_body['guest_name'][0]
        random_token = ranNumber
        
        db = TicketsDB()
        if self.cookie:

            self.send_response(403)
            self.end_headers()
            self.wfile.write((bytes("The Oompa Loompas have already received your ticket. Please try again tomorrow.", "utf-8")))
        
        else:
            db.createTicket(entrant_name, entrant_age, guest_name, random_token)
            self.send_response(201)
            self.send_cookie()
            self.end_headers()
            self.wfile.write((bytes("Created", "utf-8")))


    def handelDeleteTicket(self):
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        db = TicketsDB()
        db.deleteTicket()
        pass


    def handelNotFound(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("It seems that this resource has been lost in the choclate pipes. An Oompa Loompa will be dispatched promptly to recover the artifact.", "utf-8"))
        pass


    def do_GET(self):
        
        print("GET Path is ", self.path)

        if self.path == '/tickets':
            self.handelGetTickets()
        else:
            self.handelNotFound()
        pass

    def do_POST(self):

        print("POST Path is ", self.path)

        if self.path == '/tickets':
            self.handelAddTicket()
        else:
            self.handelNotFound()
        pass

    def do_DELETE(self):

        print("DELETE Path is ", self.path)

        if self.path == '/tickets':
            self.handelDeleteTicket()
        else:
            self.handelNotFound()
        pass


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


def run():
    
    listen = ("127.0.0.1", 8080)
    server = ThreadedHTTPServer(listen , MyRequestHandler)
    
    print("The server is running!")
    server.serve_forever()

    return

run()