# NEED : HSM Module interface to encrypt key
# NEED : Network Module to request public PGP key
import struct

import otrimplement

# Type of Message
MSG_TYPE_NOT_ENCRYPTED = 0
MSG_TYPE_ENCRYPTED = 1
MSG_TYPE_REQUEST_VERIFY = 2
MSG_TYPE_RECEIVE_VERIFY = 3

# Wrapper for Message
class MessageBlock:
    def __init(self) :
        self.msg = None
        self.msgtype = None
        return
    
    def msg_to_message_block(msg, msgtype) :
        # convert msg to bytestring
        bytemsg = b''
        if type(msg) == type(string) :
            bytemsg = msg.encode(encoding='UTF-8')
        elif type(msg) == type(bytes) :
            bytemsg = msg
        else :
            raise MessageBlockParsingError
       
        # create message block
        msgblock = MessageBlock()
        msgblock.msg = bytemsg
        msgblock.msgtype = msgtype

        
        return msgblock

    def byte_to_message_block(bytestr) :
        # check bytestr is at least 6bytes
        if len(bytestr) < 6 :
            raise MessageBlockParsingError

        # unpack info of MessageBlock(6bytes)
        info = struct.unpack('!hi', bytestr[0:5])
        if info[0] < 0 or info[0] > 3 :
            raise MessageBlockParsingError
        if info[1] < 0 or info[1] > 1024 :
            raise MessageBlockParsingError
        elif info[1] != len(bytestr[6:len(bytestr)]) :
            raise MessageBlockParsingError
        
        # create message block
        msgblock = MessageBlock()
        msg.msg = bytestr[6:info[1]]
        msg.msgtype = info[0]

        return msgblock

    def message_block_to_byte(self) :
        # pack MessageBlock to byte
        return struct.pack('!hi', self.msgtype, len(self.msg)) + self.msg




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
        if reply is None or reply is False :
            return False
        elif reply is True :
            return True
        
        # reply to other
        while not reply.empty():
            self.onSended(reply.get())


        if self.context.isConnected() :
            return True
        return False


    def IsConnected(self) :
        return self.isConnected

    # Send verification request to other
    #    communicate with HSM module to get encrypted key
    #    call SemdMessage
    #    encrypted key will
    def RequestVerification(self, msgtyp) :
        # Check Stability
        if not isConnected :
            self.onError(ERR_OTR_NOT_ESTABLISHED)
            return 
        if msgtyp is not MSG_REQUEST_VERIFY and msgtyp is not MSG_REPLY_VERIFY :
            self.onError(ERR_INVALID_PARAMETER)
            return

        # encrypt my key
        key = self._encrypt_my_key()
        if key is None :
            return

        # send key
        self.SendMessage(key, msgtyp = MSG_TYPE_REQUEST_VERIFY)
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
        if (not isConnected) :
            onError(ERR_OTR_NOT_ESTABLISHED)
            return False

        
        if (not isVerified) :
            onError(ERR_NOT_VERIFIED_USER)
            return False


        # Create MessageBlcok
        msgblock = msg_to_message_block(msg, msgtyp)
        msg_bstring = msgblock.message_block_to_byte()

        # pass message to otr
        try :
            sendqueue = context.handleSend(msg_bstring)
        except Exception as e :
            onError(ERR_WRONG_MESSAGE)
            return False
        if type(sendqueue) is not type (Queue.queue) :
            return False

        # Process Send Message by CallBack
        while not sendqueue.empty() :
            onSended(sendqueue.get())

        return True







    # Decrypt given message
    #    decrypted message will be call bakced
    #    return :
    #        True : Message received successfully
    #        False: Message received failed
    def ReceiveMessage(self, msg) :
        # Check Stability
        if (not isConnected) :
            onError(ERR_OTR_NOT_ESTABLISHED)
            return False
 
        # Get Queued Message
        try :
            recvqueue = context.handleReceive(msg) 
        except Exception as e :
            onError(ERR_WRONG_MESSAGE)
            return False

        # Process Received Message by CallBack
        while not recvqueue.empty() : 
            if not _handle_recv_(queuemessage.get()) :
                return False

        return True



    
       
# Interface inner module
    def _encrypt_my_key(self) :
        return b'this is not emplemented yet'

    def _verify_other_(self, key) :
        isVerified = True
        return True
    
    def _handle_recv_(self, decrypted_message) :
        if decrypted_message is None:
            return True

        # create message block
        try:
             msgblock = byte_to_message_block(decrypted_message)
        except MessageBlockParsingError :
            onError(ERR_WRONG_MESSAGE)
            return False

        # switch case with message type
        if msgtyp == MSG_TYPE_NOT_ENCRYPTED :
            onError(ERR_MSG_NOT_ENCRYPTED)
            return False

        elif msgtyp == MSG_TYPE_ENCRYPTED :
            if (not isVerified) :
                onError(ERR_NOT_VERIFIED_USER)
                return False

            onReceived(msgblock.msg)
            return True

        elif msgtyp is MSG_TYPE_REQUEST_VERIFY :
            result = _verify_other_(msgblock.msg)
            RequestVerifyCation(MSG_TYPE_RECEIVE_VERIFY)
            return True

        elif msgtyp == MSG_TYPE_RECEIVE_VERIFY :
            result = _verify_other_(msgblock.msg)
            return True

        else :
            onError(ERR_WRONG_MESSAGE)
            return False

        return False




