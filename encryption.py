import codecs
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

class ENCRYPTION_ECB:
	#takes string key, 16 chars like: 'dhfjgkhyirkjghtp'
	def __init__(self,key):
		self.key=key.encode()
		self.BLOCKSIZE=16
		
	#takes encrypted hex data like: 'B05E660F92C8BBAD93ED49320DE1D9C2'
	def decrypt(self,hexdata):
		self.hexdata=hexdata.encode()
		self.data_b=codecs.decode(hexdata,'hex')
		self.decipher = AES.new(self.key,AES.MODE_ECB)
		self.plaintext = unpad(self.decipher.decrypt(self.data_b),self.BLOCKSIZE)
		return(self.plaintext.decode())