import random

class Cube:
    def __init__(self, coor):
        self.coor = [coor]
        self.value = random.choice([2,4])

cube = Cube([1,0])
print(cube.coor)
print(cube.value)
