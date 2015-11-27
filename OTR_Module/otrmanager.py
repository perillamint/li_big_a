

# Error codes
ERR_UNSTABLE = 0
ERR_SEND_WRONG = 1
ERR_RECV_WRONG = 2
ERR_VERIF_FAIL = 3





# Manage OTR Sessions and Connect with other layer
# Implemented as singleton
class OTRManager :

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
        session = self.otrsessions[jid]
        if session is None :
            # TODO : user layer to destroy session
            return

        # handle send message
        session.SendMessage(message)

        return


    # called from network layer
    # call when user receive message(otr encrypted)
    def ReceiveMessage(self, jid, message) :
        session = self.otrsessions[jid]
        if session is None :
            # TODO : create new OTR session
            return

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

    def Error(jid, errorcode) :
        return






