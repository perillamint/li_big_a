




# Type of Message
MSG_TYPE_NOT_ENCRYPTED = 0
MSG_TYPE_ENCRYPTED = 1
MSG_TYPE_REQUEST_VERIFY = 2
MSG_TYPE_RECEIVE_VERIFY = 3

# Get message and wrapping it
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
        
        return None

    def message_block_to_byte(self) :
        
        return None




# Type of ERROR
ERR_OTR_NOT_ESTABLISHED = 0
ERR_MULTIPLE_CONNECTION_REQUEST = 1
ERR_NOT_VERIFIED_USER = 2

# NEED : HSM Module interface to encrypt key
# NEED : Network Module to request public PGP key

class OtrModule:
    def __init__(self, onSend, onRecv, onErr) :
        self.isConnected = False
        self.isVerified = False
        self.onSended = onSend
        self.onReceived = onRecv
        self.onError = onErr
        return

# Interface to main framework

    # Connect to other.
    #   return : 
    #       True = connection request successful
    #       False = Connection request failed
    def RequestConnect(self) :
        if isConnected :
            onError(ERR_MULTIPLE_CONNECTION_REQUEST)
            return False

        connection_message = b""
        onSended(connection_message)
        
        return True

    # Reply to connection request
    #   return :
    #        True = connection established successfully
    #        False = connection not yet established
    def ReplyConnect(self, msg = None) :
        # Check stablity
        if isConnected :
            onError(ERR_MULTIPLE_CONNECTION_REQUEST)
            return False

# MEED : OTR CONNECTOR        
        # Handle connection message
        # 
        #



        return False


    # Send verification request to other
    #    communicate with HSM module to get encrypted key
    #    call SemdMessage
    #    encrypted key will
    def RequestVerification(self, msgtyp) :
        # Check Stability
        if not isConnected :
            onError(ERR_OTR_NOT_ESTABLISHED)
            return 
        if msgtyp is not MSG_REQUEST_VERIFY and msgtyp is not MSG_REPLY_VERIFY :
            onError(ERR_INVALID_PARAMETER)
            return


        # send Message
        key = self._encrypt_my_key()
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
            RequestVerification()
            return False


        # Create MessageBlcok
        msgblock = msg_to_message_block(msg, msgtyp)
        msg_bstring = msgblock.message_block_to_byte()
# NEED : OTR CONNECTOR
        # pass message to otr
        onSended(encrypted_message)
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
 
# NEED : OTR CONNECTOR       
        # pass message to otr
        
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
            RequestVerifyCation(MSG_TYPE_RECEIV_VERIFY)
            return True

        elif msgtyp == MSG_TYPE_RECEIVE_VERIFY :
            result = _verify_other_(msgblock.msg)
            return True

        else :
            onError(ERR_WRONG_MESSAGE)
            return False

        return True



    
       
# Interface inner module
    def _encrypt_my_key(self) :
        return b'this is not emplemented yet'

    def _verify_other_(self, key) :
        return True
    









