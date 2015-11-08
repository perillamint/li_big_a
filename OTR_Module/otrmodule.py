







class NotEmplementedError:
    def __init__(self):
        return



MSG_TYPE_NOT_ENCRYPTED = 0
MSG_TYPE_ENCRYPTED = 1
MSG_TYPE_REQUEST_VERIFY = 2


class MessageBlock:
    def __init(self, msg, msgtype):
        return



class OtrModule:
    def __init__(self, outQueue, inQueue):
	self.isConnected = False


        return

# Interface to main framework

    # Connect to other
    #   return :
    #       
    #       None -
    def Connect(self):
        return None





    # Encrypt outgoing message.
    #   encrypted message will be inserted on outQueue
    #
    #   return : 
    #       None -
    def SendMessage(self, msg):
        return None







    # Decrypt given message
    #    decrypted message will be inserted on inQueue
    #
    #    return :
    #        None - 
    def ReceiveMessage(self, msg):
        return None



    # Disconnect to other
    #   return :
    #       
    #       None - 
    def Disconnect(self):
        return None





    # Send verification request to other
    #    communicate with HSM module to get encrypted key
    #    insert verification message on outQueue
    #    encrypted key will
    def VerifyOther(self):
        raise NotEmplementedError()




# Interface inner module

    def _encrypt_my_key(self):
        return None
	
    def _make_message_block(self, msg, msgtype):
        return None

    









