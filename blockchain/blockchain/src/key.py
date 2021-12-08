import rsa

HASH_METHOD = 'SHA-256'

class Key:
    def __init__(self):
        self.pub_key, self.priv_key = rsa.newkeys(512)
    
    def sign(self, message):
        return rsa.sign(message, self.priv_key, HASH_METHOD)

    @staticmethod
    def verify(message, signature, pub_key):
        try:
            rsa.verify(message, signature, pub_key)
            return True
        except rsa.VerificationError:
            return False
        except Exception as e:
            raise e

    def get_pub_key(self):
        return self.pub_key
