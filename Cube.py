import random

class Cube:
    _target_value = 32
    def __init__(self, coor):
        self.coor = coor
        self.value = random.choice([2,4])

    def change_value(self):
        self.value *= 2

    def tells_winning_or_not(self):
        if self.value == self._target_value:
            print("$"*80)
            print("You got {}. Congratulations!!!".format(self._target_value))
            return True
    # edge matters!! because this judging process only occurs when the cube reaches the wall
    # judging process : if the value of two cubes are the same
