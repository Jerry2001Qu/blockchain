from blockchain.src.node import Node

class Network:
    def __init__(self):
        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)
