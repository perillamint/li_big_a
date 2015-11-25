# NEED : HSM Module interface to encrypt key
# NEED : Network Module to request public PGP key
import struct

import otrimplement
import base64

class MessageBlockParsingError(Exception):
    pass

# Type of Message
MSG_TYPE_NOT_ENCRYPTED = 0
MSG_TYPE_ENCRYPTED = 1
MSG_TYPE_REQUEST_VERIFY = 2
MSG_TYPE_REPLY_VERIFY = 3

# Wrapper for Message
class MessageBlock:
    def __init(self) :
        self.msg = None
        self.msgtype = None
        return
    
    def msg_to_message_block(msg, msgtype) :
        # convert msg to bytestring
        bytemsg = b''
        if type(msg) is str :
            bytemsg = msg.encode(encoding='UTF-8')
        elif type(msg) is bytes :
            bytemsg = msg
        else :
            raise MessageBlockParsingError
       
        # create message block
        msgblock = MessageBlock()
        msgblock.msg = bytemsg
        msgblock.msgtype = msgtype

        
        return msgblock

    def byte_to_message_block(b64str) :
        bytestr = base64.b64decode(b64str)
        if bytestr is None :
            raise MessageBlockParsingError

        # check bytestr is at least 6bytes
        if len(bytestr) < 6 :
            raise MessageBlockParsingError

        # unpack info of MessageBlock(6bytes)
        info = struct.unpack('!hi', bytestr[0:6])
        if info[0] < 0 or info[0] > 3 :
            raise MessageBlockParsingError
        if info[1] < 0 or info[1] > 1024 :
            raise MessageBlockParsingError
        elif info[1] != len(bytestr[6:len(bytestr)]) :
            raise MessageBlockParsingError
        
        # create message block
        msgblock = MessageBlock()
        msgblock.msg = bytestr[6:6 + info[1]]
        msgblock.msgtype = info[0]
 
        return msgblock

    def message_block_to_byte(self) :
        # pack MessageBlock to byte
        bytestr = struct.pack('!hi', self.msgtype, len(self.msg)) + self.msg
 
        encoded = base64.b64encode(bytestr)
        if encoded is None :
            raise MessageBlockParsingError

        return encoded




# Type of ERROR
ERR_OTR_NOT_ESTABLISHED = 0
ERR_MULTIPLE_CONNECTION_REQUEST = 1
ERR_NOT_VERIFIED_USER = 2
ERR_WRONG_MESSAGE = 3


# Wrapper for Total OTR Module
class OtrModule:
    def __init__(self, account, onSend, onRecv, onErr) :
        self.isConnected = False
        self.isVerified = False
        self.onSended = onSend
        self.onReceived = onRecv
        self.onError = onErr

        self.context = otrimplement.Context(account, self)
        return

# Interface to main framework
    # Connect to other.
    #   return : 
    #       True = connection request successful
    #       False = Connection request failed
    def RequestConnect(self) :
        if self.isConnected :
            onError(ERR_MULTIPLE_CONNECTION_REQUEST)
            return False

        connection_message = '?OTRv2?\nI want to start ' \
        'an OTR private conversation.\n See https://otr.' \
        'cypherpunks.ca/ for more information.'.encode('UTF-8')

        self.onSended(connection_message)
        return True

    # Reply to connection request
    #   return :
    #        True = connection established successfully
    #        False = connection not yet established
    def ReplyConnect(self, msg = None) :
        # Check stablity
        if self.isConnected :
            self.onError(ERR_MULTIPLE_CONNECTION_REQUEST)
            return False

        if msg is None :
            return False

        # get reply message
        reply = self.context.handleConnectionRequest(msg)        

        # reply to other
        while not reply.empty():
            self.onSended(reply.get())


        if self.context.isConnected() :
            self.isConnected = True
            return True
        return False


    def IsConnected(self) :
        return self.isConnected

    # Send verification request to other
    #    communicate with HSM module to get encrypted key
    #    call SemdMessage
    #    encrypted key will
    def RequestVerification(self, msgtyp=MSG_TYPE_REQUEST_VERIFY) :
        # Check Stability
        if not self.isConnected :
            self.onError(ERR_OTR_NOT_ESTABLISHED)
            return 
        if msgtyp is not MSG_TYPE_REQUEST_VERIFY :
            if msgtyp is not MSG_TYPE_REPLY_VERIFY :
                self.onError(ERR_INVALID_PARAMETER)
                return

        # encrypt my key
        key = self._encrypt_my_key()
        if key is None :
            return

        # send key
        self.SendMessage(key, msgtyp)
        return 



    # Disconnect to other
    #   return :
    def Disconnect(self) :
        # Send Disconnection Message

        return None



    # Encrypt outgoing message.
    #    return :
    #        True : Message sended successfully
    #        False: Message sended failed
    def SendMessage(self, msg, msgtyp = MSG_TYPE_ENCRYPTED) :
        # Check Stability
        if (not self.isConnected) :
            self.onError(ERR_OTR_NOT_ESTABLISHED)
            return False

       
        if (msgtyp is MSG_TYPE_ENCRYPTED) and (not self.isVerified) :
            self.onError(ERR_NOT_VERIFIED_USER)
            return False


        # Create MessageBlcok
        msgblock = MessageBlock.msg_to_message_block(msg, msgtyp)
        msg_bstring = msgblock.message_block_to_byte()

        # pass message to otr
        try :
            sendqueue = self.context.handleSend(msg_bstring)
        except Exception as e :
            self.onError(ERR_WRONG_MESSAGE)
            return False

        # Process Send Message by CallBack
        while not sendqueue.empty() :
            self.onSended(sendqueue.get())

        return True







    # Decrypt given message
    #    decrypted message will be call bakced
    #    return :
    #        True : Message received successfully
    #        False: Message received failed
    def ReceiveMessage(self, msg) :
        # Check Stability
        if (not self.isConnected) :
            self.onError(ERR_OTR_NOT_ESTABLISHED)
            return False 

        # Get Queued Message
        #try :
        #    recvqueue = self.context.handleReceived(msg) 
        #except Exception as e :
        #    self.onError(ERR_WRONG_MESSAGE)
        #    return False
       # Get Queued Message
        recvqueue = self.context.handleReceived(msg) 
       
        # Process Received Message by CallBack
        while not recvqueue.empty() : 
            result = self._handle_recv_(recvqueue.get())
            if not result :
                return False

        return True



    
       
# Interface inner module
    def _encrypt_my_key(self) :
        return b'this is not emplemented yet'

    def _verify_other_(self, key) :
        self.isVerified = True
        print("verified")
        return True
    
    def _handle_recv_(self, decrypted_message) :
        if decrypted_message is None:
            return True

        # create message block
        try:
             msgblock = MessageBlock.byte_to_message_block(decrypted_message)
        except MessageBlockParsingError :
            self.onError(ERR_WRONG_MESSAGE)
            return False
        
        # switch case with message type
        if msgblock.msgtype == MSG_TYPE_NOT_ENCRYPTED :
            self.onError(ERR_MSG_NOT_ENCRYPTED)
            return False
        
        elif msgblock.msgtype == MSG_TYPE_ENCRYPTED :
            if (not self.isVerified) :
                self.onError(ERR_NOT_VERIFIED_USER)
                return False
            self.onReceived(msgblock.msg)
            return True

        elif msgblock.msgtype is MSG_TYPE_REQUEST_VERIFY :
            result = self._verify_other_(msgblock.msg)
            self.RequestVerification(msgtyp=MSG_TYPE_REPLY_VERIFY)
            return True

        elif msgblock.msgtype == MSG_TYPE_REPLY_VERIFY :
            result = self._verify_other_(msgblock.msg)
            return True

        else :
            self.onError(ERR_WRONG_MESSAGE)
            return False

        return False




