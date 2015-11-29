
import base64

import otrmanager
import otrimplement

#import networkmanager
#import usermanager

# by wrapping with message block, we can add some control message

MSG_TYPE_NONE = 0
MSG_TYPE_ENCRYPTED = 1
MSG_TYPE_VERIFY = 2


class MessageBlock :
    def __init__(self):
        self.msg = ''
        self.typ = MSG_TYPE_NONE

    def CreateFromText(message, messagetype) :
        messageblock = MessageBlock()
        if type(message) is str :
            messageblock.msg = message.encode(encoding='UTF-8')
        elif type(message) is bytes :
            messageblock.msg = message
        else :
            return None

        if not (messagetype in range(1, 3, 1)) :
            return None

        messageblock.typ = messagetype

        return messageblock

    def CreateFromBytes(bytestring) :
        if not (type(bytestring) is bytes) :
            return None

        # decode
        serialized = base64.b64decode(bytestring)
        if len(deserialized) < 6 :
            return None

        msgtyp = int.from_bytes(serialized[0:2], byteorder='little')
        msglength = int.from_bytes(serialized[2:6], byteorder='little')
        message = serialized[6:len(serialized)]
        
        if not (msgtyp in range(1, 3, 1)) :
            return None

        if not (len(msgcontext) is msglength) :
            return None

        
        if len(msgcontext) > 1024 :
            return None

        # create message block
        messageblock = MessageBlock()
        messageblock.msg = message
        messageblock.typ = msgtyp


        return messageblock


    def ExportToBytes(self) :
        
        bytes_typ = bytes([self.typ])
        bytes_len = bytes([len(self.msg)])
        
        # check type
        if not (len(bytes_typ) is 1) :
            return None
        
        # check length
        if (len(bytes_len) <= 0) :
            return None
        elif (len(bytes_len) > 4) :
            return None
        elif (len(bytes_len) is 4) :
            # padding
            do()

        # check message
        if len(self.msg) > 1024 :
            return None
        
        #serialize
        serialized = bytes_typ + bytes_len + self.msg
        
        #encode
        b64encoded = base64.b64encode(serialized)

        return b64encoded


    def ExportToText(self) :
        if not (self.typ in range(1, 3, 1)) :
            return None

        return self.msg

    def GetType(self) :
        return self.typ


# return ecrypted message on bytes
def __EncryptMessageOf__(message, typ) :
    # Ascii guard plaintext
    guarded = base64.b64encode(message)
    if guarded is None :
        return None

    # Create MessageBlock
    messageblock = MessageBlock.CreateFromText(message, typ)
    if messageblock is None :
        return None

    return messageblock.ExportToBytes()

# return decrypted message and its type
def __DecryptMessageOf__(message, typ) :

    # Create MessageBlock
    messageblock = MessageBlock.CreateFromBytes(message)
    if messageblock is None :
        return None
        
    # check messageblock has non-ascii-bytes
    # TODO

    # check messageblock type
    if not (messageblock.typ is typ) :
        return None

    # decrypt Ascii guard
    unguarded = base64.b64decode(messageblock.ExportToPlainText())
    if unguarded is None :
        return None

    return unguarded



class OTRsession :
    def __init__(self, jid_other, starter) :
        self.jid = jid_other
        self.isStarter = starter
        self.isOTRconnected = False
        self.isGPGverified = False
        self.otrContext = otrimplement.Context(jid_other)


    def isConnected(self) :
        return self.isOTRconnected

    def isGPGverified(self) :
        return self.isGPGverified

    # send to other
    def SendMessage(self, plaintext) :
        if self.__CheckStable__(True, True) :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_UNSTABLE)
            return

        # encrypt message
        sending = __EncryptMessageOf__(plaintext, MSG_TYPE_ENCRYPTED)
        if sending is None :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return
            
        # encrypt with otr
        messagequeue = self.otrContext.handleSend(sending)
        if messagequeue is None :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_SEND_WRONG)
            return

        # send to network manager
        while not messagequeue.empty():
#            networkmanager.NetManager().SendMessage(self.jid, messagequeue.get())
            print("sending : %s" % messagequeue.get())

        return
        
    # recv from other
    def ReceiveMessage(self, encrypted) :
        if self.__CheckStable__(True, True) :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_UNSTABLE)
            return

        # check encrypted has non-ascii-bytes
        # TODO
        
        # decrypt with otr
        received = self.otrContext.handleReceived(encrypted)
        if received is None :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # decrypt message
        unguarded = __DecryptMessageOf__(received, MSG_TYPE_ENCRYPTED)
        if unguarded is None :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # send only message to user manager
#        usermanager.UserManager().OnReceive(self.jid, unguarded)
        print("receiving : %s" % unguarded)

        return

    def StartConnection(self) :
        # create connection message
        connection_message = self.otrContext.getDefaultQueryMessage()

        # send to network manager
#        networkmanager.NetManager().SendMessage(self.jid, connection_message)
        print("sending : %s" % connection_message)

        return

    def HandleConnection(self, message) :
        # decrypt with otrcontext
        replyqueue = self.otrContext.handleConnectionRequest(message)
        if self.context.isConnected() :
            self.isOTRconnected = True
            if self.isStarter :
                self.StartVerification()
            return
        elif replyqueue is None :
            return
        
        # send to network manager
        while not replyqueue.empty() :
#            networkmanager.NetManager().SendMessage(self.jid, replyqueue.get())
            print("sending : %s" % messagequeue.get())
        

        return

    def StartVerification(self) :
        if self.__CheckStable__(True, False) :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_UNSTABLE)
            return
        
        # get verification key
        keyseed = self.__GetVerificationKeySeed__()
        otrmanager.OTRManager.Instance().GetVerifKeyOf(self.jid, keyseed)

        return
        

    def OnVerificationKeyGet(self, key) :
        # encrypt message
        sending = __EncryptMessageOf__(key, MSG_TYPE_VERIFY)
        if sending is None :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_VERIF_FAIL)
            return

        # encrypt with otr
        messagequeue = self.otrContext.handleSend(sending)
        if messagequeue is None :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_VERIF_FAIL)
            return

        # send to network manager
        while not messagequeue.empty():
#            networkmanager.NetManager().SendMessage(self.jid, messagequeue.get())
            print("sending : %s" % messagequeue.get())

        return

    def HandleVerification(self, message) :
        if self.__CheckStable__(True, False) :
            otrmanager.OTRManager.Instance().Error(jid, otrmanager.ERR_UNSTABLE)
            return
        
        # check encrypted has non-ascii-bytes
        # TODO

        # decrypt with otr
        received = self.otrContext.handleReceived(message)
        if received is None :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # decrypt Ascii guard
        unguarded = __DecryptMessageOf__(received, MSG_TYPE_VERIFY)
        if unguarded is None :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # verify other
        key = otrmanager.OTRManager.Instance().GetGPGKeyOf(self.jid)
        if not (self.__Verify__(key, unguarded)):
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_VERIF_FAIL)
            return

        # set verfication flag
        self.isGPGverified = True

        # if user not connection starter request
        if not self.isStarter :
            self.StartVerification()

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



    def __GetVerificationKeySeed__(self) :


        return "Not Implemented"

    def __Verify__(self, key, msg) :


        return True








