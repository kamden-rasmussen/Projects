import sqlite3
from passlib.hash import bcrypt

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class TasksDB():

    def __init__(self):
        self.connection = sqlite3.connect("tasks.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        pass

    def getAllTasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        data = self.cursor.fetchall()
        #print(data)
        return data
        
    def getOneTask(self, idForTask):
        identifier = [idForTask]
        self.cursor.execute("SELECT * FROM tasks WHERE id = ?", identifier)
        data = self.cursor.fetchone()
        #print(data)
        return data
    
    def createTask(self, task, dueDate, priority, progress, reference):
        data = [task, dueDate, priority, progress, reference]
        self.cursor.execute("INSERT INTO tasks (task, dueDate, priority, progress, reference) VALUES (?,?,?,?,?)", data)
        self.connection.commit()
        pass

    def modifyTask(self, identifier, task, dueDate, priority, progress, reference ):
        dataToMod = [task, dueDate, priority, progress, reference, identifier]
        self.cursor.execute("UPDATE tasks SET task = ?, dueDate = ?, priority = ?, progress = ?, reference = ? WHERE id = ?", dataToMod)
        self.connection.commit()
        pass

    def deleteTask(self, identifier):
        identifier = [identifier]
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", identifier)
        self.connection.commit()
        pass

    #CREATE TABLE tasks(id INTEGER PRIMARY KEY, task STRING, dueDate INTEGER, priority INTEGER, progress INTEGER, reference STRING );
    #INSERT INTO tasks(task, dueDate, priority, progress, reference) VALUES ('Complete Resourceful', 14, 8, 0, 'se3200');
#---------------------------------------------------------------------------------------------------------------------------------------------------- 


    def createUser(self, email, firstName, lastName, password):
        hashedPass = bcrypt.hash(password)
        data = [email, firstName, lastName, hashedPass]
        self.cursor.execute("INSERT INTO users (email, firstName, lastName, password) VALUES (?,?,?,?)", data)
        self.connection.commit()


    def getOneUserWithEmail(self, emailForUser):
        identifier = [emailForUser]
        self.cursor.execute("SELECT * FROM users WHERE email = ?", identifier)
        data = self.cursor.fetchone()
        #print("got one ", data)
        if data:
            return data
        else:
            return None    


    def getOneUserWithID(self, ID):
        identifier = [ID]
        self.cursor.execute("SELECT * FROM users WHERE id = ?", identifier)
        data = self.cursor.fetchone()
        #print("got one ", data)
        if data:
            return data
        else:
            return None


    def checkPassword(self, emailForUser, userPassword):
        identifier = [emailForUser]
        self.cursor.execute('SELECT password FROM users WHERE email = ?', identifier)
        data = self.cursor.fetchone()
        return bcrypt.verify(userPassword, data['password'])


    def getAllUsers(self):
        self.cursor.execute("SELECT * FROM users")
        data = self.cursor.fetchall()
        #print(data)
        return data


    # def modifyUser(self, identifier, email, firstName, lastName, password):
    #     dataToMod = [email, firstName, lastName, password, identifier]
    #     self.cursor.execute("UPDATE users SET email = ?, firstName = ?, lastName = ?, password = ?, WHERE id = ?", dataToMod)
    #     self.connection.commit()
    #     pass


    def deleteUser(self, identifier):
        identifier = [identifier]
        self.cursor.execute("DELETE FROM users WHERE id = ?", identifier)
        self.connection.commit()


    #CREATE TABLE users(id INTEGER PRIMARY KEY, email STRING, firstName STRING, lastName STRING, password STRING );
    #INSERT INTO users(id, email, firstName, lastName, password) VALUES ('testone@test.com', 'test', 'one', 'asdfjkl;');