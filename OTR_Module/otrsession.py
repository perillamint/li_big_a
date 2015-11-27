
import base64

import otrmanager

import networkmanager
import usermanager

MSG_TYPE_ENCRYPTED = 0
MSG_TYPE_VERIFY_A = 1
MSG_TYPE_VERIFY_B = 2

class MessageBlock :
    def __init__(self):
        self.msg = ''
        self.typ = MSG_TYPE_ENCRYPTED


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
        if self.__CheckStable__(True, True) :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_UNSTABLE)
            return

        # Ascii guard plaintext
        guarded = base64.b64encode(plaintext)
        if guarded is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        # Create MessageBlock
        messageblock = MessageBlock.CreateFromText(message, MSG_TYPE_ENCRYPTED)
        if messageblock is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        # encrypt with otr
        messagequeue = self.otrContext.
        if messagequeue is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        
        # send to network manager
        while not messagequeue.empty():
           networkmanager.NetManager().SendMessage(self.jid, messagequeue.get())


        return
        
    # recv from other
    def ReceiveMessage(self, encrypted) :
        if self.__CheckStable__(True, True) :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_UNSTABLE)
            return
        
        # decrypt with otr
        received = self.otrContext.
        if received is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # Create MessageBlock
        messageblock = MessageBlock.CreateFromBytes(received)
        if messageblock is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        if not (messageblock.typ is MSG_TYPE_ENCRYPTED) :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # decrypt Ascii guard
        unguarded = base64.b64decode(messageblock.ExportToPlainText())
        if unguarded is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        
        # send to user manager
        usermanager.UserManager().OnReceive(self.jid, unguarded)



        return

    def StartConnection(self) :
        # create connection message
        connection_message = '?OTRv2?\nI want to start ' \
            'an OTR private conversation.\n See https://otr.' \
            'cypherpunks.ca/ for more information.'.encode('UTF-8')

        # send to network manager
        networkmanager.NetManager().SendMessage(self.jid, connection_message)

        return

    def HandleConnection(self, message) :
        # decrypt with otrcontext
        replyqueue = self.otrContext.
        if self.context.isConnected() :
            self.isOTRconnected = True
        elif replyqueue is None :
            return
        
        # send to network manager
        while not replyqueue.empty() :
           networkmanager.NetManager().SendMessage(self.jid, replyqueue.get())

        return

    def StartVerification(self) :
        if self.__CheckStable__(True, False) :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_UNSTABLE)
            return

        verificationkey = self.__GetVerificationKey__()

        # Ascii guard plaintext
        guarded = base64.b64encode(verificationkey)
        if guarded is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        # Create MessageBlock
        messageblock = MessageBlock.CreateFromText(message, MSG_TYPE_VERIFY_A)
        if messageblock is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        # encrypt with otr
        messagequeue = self.otrContext.
        if messagequeue is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        # send to network manager
        while not messagequeue.empty() :
           networkmanager.NetManager().SendMessage(self.jid, messagequeue.get())

        return

    def HandleVerification(self, message) :
        if self.__CheckStable__(True, False) :
            otrmanager.OTRManager().Error(jid, otrmanager.ERR_UNSTABLE)
            return
        
       # decrypt with otr
        received = self.otrContext.
        if received is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # Create MessageBlock
        messageblock = MessageBlock.CreateFromBytes(received)
        if messageblock is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        
        if not (messageblock.typ is MSG_TYPE_VERIFY_A or messageblock.typ is MSG_TYPE_VERIFY_B) :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # decrypt Ascii guard
        unguarded = base64.b64decode(messageblock.ExportToPlainText())
        if unguarded is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # verify other
        key = networkmanager.NetManager().RequestGPGKey(self.jid)
        if not self.__Verify__(key, unguarded) :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_VERIF_FAIL)
            return


        # if Message Type is A, you need to send your key
        verificationkey = self.__GetVerificationKey__()

        # Ascii guard plaintext
        guarded = base64.b64encode(verificationkey)
        if guarded is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        # Create MessageBlock
        messageblock = MessageBlock.CreateFromText(message, MSG_TYPE_VERIFY_B)
        if messageblock is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        # encrypt with otr
        messagequeue = self.otrContext.
        if messagequeue is None :
            otrmanager.OTRManager().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        # send to network manager
        while not messagequeue.empty() :
           networkmanager.NetManager().SendMessage(self.jid, messagequeue.get())

        return


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


    def __GetVerificationKey__(self) :
        return "Not Implemented"

    def __Verify__(self, key, msg) :
        return True







