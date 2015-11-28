# Error codes
ERR_UNSTABLE = 0
ERR_SEND_WRONG = 1
ERR_RECV_WRONG = 2
ERR_VERIF_FAIL = 3





# Manage OTR Sessions and Connect with other layer
# Implemented as singleton
class OTRManager :
    def __init__(self) :
        self.otrsessions = {}
        self.otrerrors = {}

    def CreateOTR(self, jid) :
        # Create OTR session
        # TODO

        # Call user layer OTR creation callback
        # TODO

        # Call network layer OTR creation callback
        # TODO

        # SendConnectionMessage
        # TODO

        return


    # called from user layer
    # call when user send message(plain text)
    def SendMessage(self, jid, message) :
        if not (jid in self.otrsessions.keys()) :
            # TODO : user layer to destroy session
            return

        # select session
        session = self.otrsessions[jid]

        # handle send message
        session.SendMessage(message)

        return


    # called from network layer
    # call when user receive message(otr encrypted)
    def ReceiveMessage(self, jid, message) :
        if not (jid in self.otrsessions.keys()) :
            # TODO : create new OTR session
            createNewOTRSession()
            
        # select session
        session = self.otrsessions[jid]
        
        # handle received message
        if not session.isConnected() :
            session.HandleConnection(message)
        elif not session.isVerified() :
            session.HandleVerification(message)
        else :
            session.ReceiveMessage(message)

        return


    # called from network layer
    # call when session is destroyed by layer under OTR layer
    def DestroySession(self, jid) :
 
        # Call user layer OTR destroy callback
        # TODO

        # destroy
        # TODO


        return

    def GetGPGKeyOf(self, jid) :
        return "Not Implemented"

    def GetVerifKeyOf(self, jid, keyseed) :

        # send message to hsm
        # TODO
        OnGetVerifKeyOf(jid, keyseed)

        return

    def OnGetVerifKeyOf(self, jid, key) :
        if not (jid in self.otrsessions.keys()) :
            return

        # send session key
        session = self.otrsessions[jid]
        session.OnVerificationKeyGet(key)

        return

    def Error(self, jid, errorcode) :

        return






