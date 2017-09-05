import random

class Cube:
    _all = set() # This is for managing cube instances. Can you think of the way to handle the lifecycle of cubes??
    def __init__(self, coor):
        self.coor = coor
        self.value = random.choice([2,4])
        self.__class__._all.add(self)
