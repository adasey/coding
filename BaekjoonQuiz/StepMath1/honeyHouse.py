import math as m

class Honey():
    def __init__(self):
        self.room = 0

    def makeHoney(self, number):
        self.room = m.ceil((1 + m.sqrt(12 * number - 3) / 3) / 2)
        return self.room