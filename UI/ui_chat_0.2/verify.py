import gnupg

def Verify(msg, key):
	gpg = gnupg.GPG(gnupghome="keys")
	import_result = gpg.import_keys(key)
	verify = gpg.verify(msg)
	isVerified = verify.valid
	return isVerified