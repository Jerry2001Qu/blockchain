
class Observer:
    def __init__(self):
        self.events = []

    def report(self, event):
        self.events.append(event)
