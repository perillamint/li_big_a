
import base64

import otrmanager

MSG_TYPE_ENCRYPTED = 0
MSG_TYPE_VERIFY_A = 1
MSG_TYPE_VERIFY_B = 2

class MessageBlock :
    def CreateFromText(message, messagetype) :
        pass
    def CreateFromBytes(bytestring) :
        pass
    def ExportToBytes(self) :
        pass
    def ExportToText(self) :
        pass
    def GetType(self) :
        pass


class OTRsession :
    def __init__(self, jid_other, starter) :
        self.jid = jid_other
        self.isStarter = starter
        self.isOTRconnected = false
        self.isGPGverified = false
        self.otrContext = None


    def isConnected(self) :
        return self.isOTRconnected

    def isGPGverified(self) :
        return self.isGPGverified

    # send to other
    def SendMessage(self, plaintext) :
        if __CheckStable__(True, True) :
            otrmanager.OTRManager().Error(jid, ERR_UNSTABLE)

        # Ascii guard plaintext
        guarded = base64.b64encode(plaintext)
        if guarded is None :
            otrmanager.OTRManager().Error(jid, otrmanager.ERR_SEND_WRONG)
       

        # Create MessageBlock
        messageblock = MessageBlock.CreateFromText(message, MSG_TYPE_ENCRYPTED)
        if messageblock is None :
            otrmanager.OTRManager().Error(jid, otrmanager.ERR_SEND_WRONG)

        # encrypt with otr TODO
        messagequeue = self.otrContext.
        if messagequeue is None :
            otrmanager.OTRManager().Error(jid, otrmanager.ERR_SEND_WRONG)

    # recv from other
    def ReceiveMessage(self, encrypted) :
        if __CheckStable__(True, True) :
            otrmanager.OTRManager().Error(jid, ERR_UNSTABLE)
        
        # decrypt with otr TODO
        received = self.otrContext.
        if received is None :
            otrmanager.OTRManager().Error(jid, otrmanager.ERR_RECV_WRONG)

        # Create MessageBlock
        messageblock = MessageBlock.CreateFromBytes(received)
        if messageblock is None :
            otrmanager.OTRManager().Error(jid, otrmanager.ERR_RECV_WRONG)

        # decrypt Ascii guard
        unguarded = base64.b64decode(messageblock.ExportToPlainText())
        if unguarded is None :
            otrmanager.OTRManager().Error(jid, otrmanager.ERR_RECV_WRONG)


    def StartConnection(self) :
        return

    def HandleConnection(self, message) :
        return

    def StartVerification(self) :
        return

    def HandleVerification(self, message) :

        return

    # __CheckStable__(connect(bool), verify(bool))
    def __CheckStable__ (self, connect, verify) :
        result = true

        # check otr is connected 
        if connect :
            if not isOTRconnected :
                result = false

        # check gpg is verified
        if verify :
            if not isGPGverified :
                result = false

        return result











