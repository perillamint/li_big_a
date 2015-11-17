








MSG_TYPE_NOT_ENCRYPTED = 0
MSG_TYPE_ENCRYPTED = 1
MSG_TYPE_REQUEST_VERIFY = 2
MSG_TYPE_RECEIVE_VERIFY = 3

class MessageBlock:
    def __init(self, msg, msgtype):
        return


# Type of ERROR
ERR_OTR_NOT_ESTABLISHED = 0
ERR_MULTIPLE_CONNECTION_REQUEST = 1
ERR_NOT_VERIFIED_USER = 2

# NEED : HSM Module interface to encrypt key
# NEED : Network Module to request public PGP key

class OtrModule:
    def __init__(self, onSend, onRecv, onErr):
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
    def RequestConnect(self):
        if isConnected :
            onError(ERR_MULTIPLE_CONNECTION_REQUEST)
            return False

        # send connection message
        # connection_message = ""
        # onSended(connection_message)
        
        return True

    # Reply to connection request
    #   return :
    #        True = connection established successfully
    #        False = connection not yet established
    def ReplyConnect(self, msg = None):
        # Check stablity
        if isConnected :
            onError(ERR_MULTIPLE_CONNECTION_REQUEST)
            return False
       
        # Handle connection message
        # 
        #



        return False


    # Send verification request to other
    #    communicate with HSM module to get encrypted key
    #    call SemdMessage
    #    encrypted key will
    def RequestVerification(self, msgtyp):
        # Check Stability
        if not isConnected :
            onError(ERR_OTR_NOT_ESTABLISHED)
            return 
        if msgtyp != MSG_REQUEST_VERIFY and msgtyp != MSG_REPLY_VERIFY
            onError(ERR_INVALID_PARAMETER)
            return


        # send Message
        # key = self._encrypt_my_key()
        # self.SendMessage(key, msgtyp)

        return



    # Disconnect to other
    #   return :
    def Disconnect(self):
        # Send Disconnection Message

        return None



    # Encrypt outgoing message.
    #    return :
    #        True : Message sended successfully
    #        False: Message sended failed
    def SendMessage(self, msg, msgtyp = MSG_ENCRYPTED):
        # Check Stability
        if (not isConnected):
            RequestConnection()
            return False

        if (not isVerified):
            RequestVerification()
            return False


        # Create MessageBlcok
        # Serialize MessageBlock to byte string
        # onSended(serialize_message_blcok)
        return True







    # Decrypt given message
    #    decrypted message will be call bakced
    #
    #    return :
    #        True : Message received successfully
    #        False: Message received failed
    def ReceiveMessage(self, msg):
      
        # Check Stability
        if (not isConnected) :
            onError(ERR_OTR_NOT_ESTABLISHED)
            return False
        
        # Create MessageBlock
        # Deserialize MessageBlock from byte string
        # if Deserialize failed, onError(ERR_WRONG_MESSAGE)
        if msgtyp == MSG_TYPE_NOT_ENCRYPTED :
            onError(ERR_MSG_NOT_ENCRYPTED)
            return False
        elif msgtyp == MSG_TYPE_ENCRYPTED :
            if (not isVerified) :
                onError(ERR_NOT_VERIFIED_USER)
                return False

            # decrypt message
            # check write message
        elif msgtyp == MSG_TYPE_REQUEST_VERIFY :
            # verify others
            # RequestVerifyCation(MSG_TYPE_RECEIV_VERIFY)
        elif msgtyp == MSG_TYPE_RECEIVE_VERIFY :
            #verify others 

        else
            # onError(ERR_WRONG_MESSAGE)
            return False

        return True



    
       
# Interface inner module
    def _reply_verification(self, msg):
        return

    def _encrypt_my_key(self):
        return None
	
    def _make_message_block(self, msg, msgtype):
        return None

    









