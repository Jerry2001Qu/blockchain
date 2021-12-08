import rsa

HASH_METHOD = 'SHA-256'

class Key:
    def __init__(self):
        self.pub_key, self.priv_key = rsa.newkeys(256)
    
    def sign(self, message):
        return rsa.sign(message, self.priv_key, HASH_METHOD)

    @staticmethod
    def verify(message, signature, pub_key):
        return rsa.verify(message, signature, pub_key)

    def get_pub_key(self):
        return self.pub_key
