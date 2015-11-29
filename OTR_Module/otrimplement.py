import potr

import queue


# Context implement for potr.Context

DEFAULT_POLICY_FLAGS = {
    'ALLOW_V1' : False,
    'ALLOW_V2' : True,
    'REQUIRE_ENCRYPTION' : True,
}

PROTOCOL = 'xmpp'
MMS = 1024

class Context(potr.context.Context) :
    def __init__(self, jid) :
        super(Context, self).__init__(Account('user'), jid)
        self.msgbuf = queue.Queue()


    def setPeerName(name) :
        self.peer = name
        return
    
    def getPolicy(self, key) :
        if key in DEFAULT_POLICY_FLAGS :
            return DEFAULT_POLICY_FLAGS[key]
        else :
            return False

    # return bytes
    def handleReceived(self, message_byte_string) :
        
        try :
            recvs = self.receiveMessage(message_byte_string, self)
        except Exception as e :
            print("Error occured")
            return False


        # check message to be sent to user
        if recvs[0] is None :
            return None

        return recvs[0]

    # return queue
    def handleSend(self, message_byte_string) :
        self.sendMessage(0, message_byte_string, appdata=self)

        # dequeue injected message and make queue
        outqueue = queue.Queue()
        while not self.msgbuf.empty() :
            outqueue.put(self.msgbuf.get())

        return outqueue

    def isConnected(self) :
        return self.state == potr.context.STATE_ENCRYPTED     
        
    # return queue
    def handleConnectionRequest(self, message_byte_string) :
        self.receiveMessage(message_byte_string, appdata=self)

        # dequeue injected message and make queue
        outqueue = queue.Queue()
        while not self.msgbuf.empty() :
            outqueue.put(self.msgbuf.get())

        return outqueue


    def getDefaultQueryMessage(self) :
        return self.user.getDefaultQueryMessage(self.getPolicy)


    def inject(self, msg, appdata = None) :
        self.msgbuf.put(msg)

# empty implementation of account
class Account(potr.context.Account):

    def __init__(self, jid):
        global PROTOCOL, MMS
        super(Account, self).__init__(jid, PROTOCOL, MMS)

    # auto generate random private key
    def loadPrivkey(self):
        return None
    
    # auto generate random private key
    def savePrivkey(self):
        pass



