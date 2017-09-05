import random

class Cube:
    _all = set() # This is for managing cube instances. Can you think of the way to handle the lifecycle of cubes??
    def __init__(self, coor):
        self.coor = coor
        self.value = random.choice([2,4])
        self.__class__._all.add(self)

    # edge matters!! because this judging process only occurs when the cube reaches the wall
    # judging process : if the value of two cubes are the same
