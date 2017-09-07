import random

class Cube:
    _target_value = 128
    def __init__(self, coor):
        self.coor = coor
        self.value = random.choice([2,4])

    def change_value(self):
        self.value *= 2

    def tells_winning_or_not(self):
        if self.value == self._target_value:
            print("*"*50)
            print("You got {}. Congratulations!!!".format(self._target_value))
            print("*"*50)
            return True
