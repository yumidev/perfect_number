import random

class Cube:
    _all = set() # This is for managing cube instances. Can you think of the way to handle the lifecycle of cubes??
    _target_value = 8
    def __init__(self, coor):
        self.coor = coor
        self.value = random.choice([2,4])
        self.__class__._all.add(self)

    def change_value(self):
        self.value *= 2

    def tells_winning_or_not(self):
        print("*"*80)
        if self.value == self._target_value:
            print("$"*80)
            print("You got {}. Congratulations!!!".format(self._target_value))
            return True
    # edge matters!! because this judging process only occurs when the cube reaches the wall
    # judging process : if the value of two cubes are the same
