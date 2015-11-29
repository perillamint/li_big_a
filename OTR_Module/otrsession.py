
import base64
import struct
import gnupg
import hashlib

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
        if len(serialized) < 6 :
            return None

        msgtyp = struct.unpack('<h', serialized[0:2])[0]
        msglength = struct.unpack('<i', serialized[2:6])[0]
        message = serialized[6:len(serialized)]
        
        if not (msgtyp in range(1, 3, 1)) :
            return None

        if not (len(message) == msglength) :
            return None

        
        if len(message) > 1024 :
            return None

        # create message block
        messageblock = MessageBlock()
        messageblock.msg = message
        messageblock.typ = msgtyp


        return messageblock


    def ExportToBytes(self) :
        # check message
        if len(self.msg) > 1024 :
            return None       
        bytes_typ = struct.pack('<h', self.typ)
        bytes_len = struct.pack('<i', len(self.msg))  
       
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

    if type(message) is str :
        message = message.encode(encoding='UTF-8')
    elif not (type(message) is bytes) :
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
    if not (messageblock.typ == typ) :
        return None

    text = messageblock.ExportToText()
    if text is None :
        return None

    return text



class OTRsession :
    def __init__(self, jid_other, starter) :
        self.jid = jid_other
        self.isStarter = starter
        self.isOTRconnected = False
        self.isGPGverified = False
        self.otrContext = otrimplement.Context(jid_other)


    def isConnected(self) :
        return self.isOTRconnected

    def isVerified(self) :
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
            print("sending to %s : %s" % (self.jid, messagequeue.get()))

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
        if received is False :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return
        elif received is None :
            return

        print(received)

        # decrypt message
        unguarded = __DecryptMessageOf__(received, MSG_TYPE_ENCRYPTED)
        if unguarded is None :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_RECV_WRONG)
            return

        # send only message to user manager
#        usermanager.UserManager().OnReceive(self.jid, unguarded)
        print("receiving from %s : %s" % (self.jid, unguarded))

        return

    def StartConnection(self) :
        # create connection message
        connection_message = self.otrContext.getDefaultQueryMessage()

        # send to network manager
#        networkmanager.NetManager().SendMessage(self.jid, connection_message)
        print("sending to %s : %s" % (self.jid, connection_message))

        return

    def HandleConnection(self, message) :
        # decrypt with otrcontext
        replyqueue = self.otrContext.handleConnectionRequest(message)
        if self.otrContext.isConnected() :
            print("connection with %s succedd" % self.jid)
            self.isOTRconnected = True
        elif replyqueue is None : 
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_UNSTABLE) 
            return

        # send to network manager
        while not replyqueue.empty() :
#            networkmanager.NetManager().SendMessage(self.jid, replyqueue.get())
            print("sending to %s : %s" % (self.jid, replyqueue.get()))
        
        if self.isOTRconnected :
            if self.isStarter :
                self.StartVerification()

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
        if self.__CheckStable__(True, False) :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_UNSTABLE)
            return

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
            print("sending to %s : %s" % (self.jid, messagequeue.get()))

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
        result = False

        # check otr is connected 
        if connect :
            if not self.isOTRconnected :
                result = True

        # check gpg is verified
        if verify :
            if not self.isGPGverified :
                result = True

        return result



    def __GetVerificationKeySeed__(self) :
        if self.__CheckStable__(True, False) :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_UNSTABLE)
            return

        tmpkeyseed = self.otrContext.crypto.sessionId
        keyseed = hashlib.sha256(tmpkeyseed).hexdigest()

        return keyseed

    def __Verify__(self, key, msg) :
        if self.__CheckStable__(True, False) :
            otrmanager.OTRManager.Instance().Error(self.jid, otrmanager.ERR_UNSTABLE)
            return

        # verify by gnupg
        gpg = gnupg.GPG(gnupghome='keys')
        import_result = gpg.import_keys(key)
        verify = gpg.verify(msg)

        return verify.valid








