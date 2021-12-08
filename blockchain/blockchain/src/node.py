from blockchain.src.key import Key

class Node:
    def __init__(self):
        self.key = Key()
        self.chain = None

    def make_transaction(self, to_address):
        pass

    def get_pub_key(self):
        return self.key.get_pub_key()
