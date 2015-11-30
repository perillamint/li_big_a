
import otrsession

import gnupg

import pycurl
from io import BytesIO


class Singleton:

    def __init__(self, decorated):
        self._decorated = decorated

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)



# Error codes
ERR_UNSTABLE = 0
ERR_SEND_WRONG = 1
ERR_RECV_WRONG = 2
ERR_VERIF_FAIL = 3



# Manage OTR Sessions and Connect with other layer
# Implemented as singleton
@Singleton
class OTRManager :
    def __init__(self) :
        self.otrsessions = {}
        self.otrerrors = {}

    def CreateOTR(self, jid) :
        # Create OTR session
        if jid in self.otrsessions.keys() :
            return

        self.otrsessions[jid] = otrsession.OTRsession(jid, True) 

        # Call user layer OTR creation callback
        # TODO

        # SendConnectionMessage
        self.otrsessions[jid].StartConnection()

        return


    # called from user layer
    # call when user send message(plain text)
    def SendMessage(self, jid, message) :
        if not (jid in self.otrsessions.keys()) :
            # TODO : user layer to destroy session
            return

        # select session
        session = self.otrsessions[jid]

        # handle send message
        session.SendMessage(message)

        return


    # called from network layer
    # call when user receive message(otr encrypted)
    def ReceiveMessage(self, jid, message) :
        if not (jid in self.otrsessions.keys()) :
            self.otrsessions[jid] = otrsession.OTRsession(jid, False)
            
        # select session
        session = self.otrsessions[jid]
        
        # handle received message
        if not session.isConnected() :
            session.HandleConnection(message)
        elif not session.isVerified() :
            session.HandleVerification(message)
        else :
            session.ReceiveMessage(message)

        return


    # called from network layer
    # call when session is destroyed by layer under OTR layer
    def DestroySession(self, jid) :
 
        # Call user layer OTR destroy callback
        # TODO

        # destroy
        del self.otrsessions[jid]

        return

    def GetGPGKeyOf(self, jid) :
        if type(jid) is str :
            jid = jid.encode('UTF-8')
        
        jid_parsed = jid.replace(b'@', b'_at_')
        jid_parsed = jid_parsed.replace(b'.', b'_dot_')
        jid_url = b'http://laurelin.arewesecureyet.org/keys/' + jid_parsed + b'.asc'
       
        # connect at reserved server
        buff = BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, jid_url)
        c.setopt(c.WRITEDATA, buff)
        c.perform()
        c.close()
	
        return buff.getvalue()


    # signing
    def GetVerifKeyOf(self, jid, keyseed) :
        # send message to hsm
        # TODO

        # temporary use in-computer signing
        keypath = '/home/poong/python/lba_otr/samplekeys/'
        if(jid == 'one@arewesecureyet.org') :
            keypath = keypath + 'two@arewesecureyet.org.asc'
        elif(jid == 'two@arewesecureyet.org') :
            keypath = keypath + 'one@arewesecureyet.org.asc'
        f = open(keypath, 'r')
        readed = f.read()
        f.close()


        gpg = gnupg.GPG(gnupghome='keys')
        imported = gpg.import_keys(readed)
        
        verifkey = gpg.sign(keyseed, keyid=imported.results[0]['fingerprint'], passphrase='libiga')
       
        # call when verification key is signed
        self.OnGetVerifKeyOf(jid, verifkey.data)

        return

    def OnGetVerifKeyOf(self, jid, key) :
        if not (jid in self.otrsessions.keys()) :
            return

        # send session key
        session = self.otrsessions[jid]
        session.OnVerificationKeyGet(key)

        return

    def Error(self, jid, errorcode) :
        print("Errored : %d" % errorcode)
        return






