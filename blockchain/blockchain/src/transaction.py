from blockchain.src.key import Key

class Transaction:
    def __init__(self, pub_key, prev_hash):
        self.pub_key = pub_key
        self.prev_hash = prev_hash
        self.sig = None

    def is_signed(self):
        return not self.sig is None

    def set_sig(self, sig):
        self.sig = sig

    def get_message(self):
        return self.pub_key + self.prev_hash

    def verify(self):
        return Key.verify(self.get_message(), self.sig, self.pub_key)
