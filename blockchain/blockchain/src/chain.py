
class Chain:
    def __init__(self):
        self.chain = []

    def verify(self):
        pass

    def get_last_hash(self):
        return self.chain[-1].get_hash()
