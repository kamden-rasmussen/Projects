import sqlite3
from sqlite3.dbapi2 import DatabaseError

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

class TicketsDB():

    def __init__(self):
        self.connection = sqlite3.connect("tickets.db")
        self.connection.row_factory = dict_factory
        self.cursor = self.connection.cursor()
        return
    

    def getTickets(self):
        self.cursor.execute("SELECT * FROM tickets")
        tickets = self.cursor.fetchall()
        return tickets
    

    def createTicket(self, entrant_name, entrant_age, guest_name, random_token):
        ticketInfo = [entrant_name, entrant_age, guest_name, random_token]
        print(ticketInfo)
        self.cursor.execute("INSERT INTO tickets(entrant_name, entrant_age, guest_name, random_token) VALUES (?,?,?,?)", ticketInfo)
        self.connection.commit()


    # def deleteTicket(self):
    #     self.cursor.execute("DELETE FROM tickets")
    #     self.connection.commit()

#CREATE TABLE tickets(id INTEGER PRIMARY KEY, entrant_name STRING, entrant_age INTEGER, guest_name STRING, random_token INTEGER );
#INSERT INTO tickets(entrant_name, entrant_age, guest_name, random_token) VALUES ('TestUser', 8, 'TestUserParent', 5);
