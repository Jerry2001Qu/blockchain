
MAX_BLOCK_SIZE = 64

class Block:
    def __init__(self, observer, prev_hash):
        self.observer = observer
        self.prev_hash = prev_hash

        self.transactions = []
        self.root_hash = None
        self.nonce = 0
        self.hash = None

    def is_full(self):
        return len(self.transactions) < MAX_BLOCK_SIZE

    # returns True if added
    def add_transaction(self, transaction):
        if not self.is_full():
            if transaction.verify():
                self.transactions.append(transaction)
                return True
            else:
                self.observer.report((transaction))
        return False
        
    def gen_root_hash(self):
        pass

    def gen_hash(self):
        pass
