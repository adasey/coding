import math as m

class Extra():

    def __init__(self):
        self.honey_house = []
        self.count = 1

    def setCalNumber(self, number):
        self.honey_house = [(3 * a * (a + 1)) + 1 for a in range(int(m.sqrt(number * 2 + 1) - 1))]

    def makeExtra(self, number):
        self.count = 1
        self.setCalNumber(number)

        if 1 < number < 4:
            self.count += 1

        for i in range(len(self.honey_house) - 1):
            # print(self.honey_house[i], self.honey_house[i + 1])
            if self.honey_house[i] < number <= self.honey_house[i + 1]:
                self.count += 1
                break

            else:
                self.count += 1

        return self.count