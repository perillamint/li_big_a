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
    def __init__(self, account, otrmodule) :
        super(Context, self).__init__(account, 'peer')
        self.msgbuf = queue.Queue()


    def setPeerName(name) :
        self.peer = name
        return
    
    def getPolicy(self, key) :
        if key in DEFAULT_POLICY_FLAGS :
            return DEFAULT_POLICY_FLAGS[key]
        else :
            return False

    def handleReceived(self, message_byte_string) :
        recvs = self.receiveMessage(message_byte_string, self)

        # iterate recvs to make queue


    def handleSend(self, message_byte_string) :
        msgbuf = queue.Queue()
        self.sendMessage(0, message_byte_string, appdata=self)
        
        # dequeue injected message and make queue
        outqueue = Queue.queue()
        while not msgbuf.empty() :
            outqueue.put(msgbuf.get())

        return outqueue

        
        
    def handleConnectionRequest(self, message_byte_string) :
        msgbuf = queue.Queue()
        self.receiveMessage(message_byte_string)
        
        # dequeue injected message and make queue
        outqueue = Queue.queue()
        while not msgbuf.empty() :
            outqueue.put(msgbuf.get())

        return outqueue


    def inject(self, msg, appdata = None) :
        appdata.msgbuf.put(msg)


class MyAccount(potr.context.Account):

    def __init__(self, jid):
        global PROTOCOL, MMS
        super(MyAccount, self).__init__(jid, PROTOCOL, MMS)

  # this method needs to be overwritten to load the private key
  # it should return None in the event that no private key is found
  # returning None will trigger autogenerating a private key in the default implementation
    def loadPrivkey(self):
        return None

  # this method needs to be overwritten to save the private key
    def savePrivkey(self):
        pass



