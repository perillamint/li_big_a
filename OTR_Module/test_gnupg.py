import gnupg

def Verify(msg, key):
	gpg = gnupg.GPG(gnupghome="keys")
#	gpg.encoding("utf-8")
	import_result = gpg.import_keys(key)
	verify = gpg.verify(msg)
	isVerified = verify.valid
	return isVerified

def Sign():
	print ("before Signgpg")
	gpg = gnupg.GPG(gnupghome="keys")
#	gpg.encoding('utf-8')
	print ("before input")
	input = gpg.gen_key_input(Passphrase='foo')
	print (input)
	print ("before key")
	key = gpg.gen_key(input)
	print ("before sig1")
	sig = gpg.sign('hello',keyid=key.fingerprint,passphrase='bar')
	print ("before print1")
	print (Verify(sig.data,key.data))
	print ("before sig2")
	sig = gpg.sign('hello',keyid=key.fingerprint,passphrase='foo')
	print ("before print2")
	print (Verify(sig.data,key.data))

print ("before Sign()")
Sign()