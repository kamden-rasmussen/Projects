import base64, os

class SessionStore:

    
    #dictionaries: keys are session ID's, values are dictionaries
    
    #methods
    #create session id
    #get session data (by session ID)
    #create/updating session data (by session ID)


    def __init__(self):
        #data members
        self.sessions = {}
        pass

    def generateSessionID(self):
        randomNumber = os.urandom(32)
        randomNumberString = base64.b64encode(randomNumber).decode("utf-8")
        return randomNumberString

    def getSessionData(self, sessionID):
        if sessionID in self.sessions:
            return self.sessions[sessionID]
        else:
            return None

    def createSession(self):
        sessionID = self.generateSessionID()
        self.sessions[sessionID] = {} # dictionary for THIS session
        return sessionID

    def setSessionData(self):
        pass
