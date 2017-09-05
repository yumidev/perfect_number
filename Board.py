import random
from Cube import Cube

class Board:
    _board_size = 5
    def __init__(self):
        # self.grid = [[,,,,],[,,,,],[,,,,],[,,,,],[,,,,]]
        self.grid = [[]]

    # get random coor for new cube
    def random_coor_generator(self, direction):
        print(direction)
        coor = None # You may want to change the name of this variable
        try:
            if direction == 'up':
                coor = [
                    random.randint(0, self._board_size-1), 0]
            elif direction == 'down':
                coor = [
                    random.randint(0, self._board_size-1), self._board_size-1]
            elif direction == 'left':
                coor = [
                    self._board_size-1, random.randint(0, self._board_size-1)]
            elif direction == 'right':
                coor = [
                    0, random.randint(0, self._board_size-1)]
        except ValueError:
            return random_coor_generator(input())
        return coor

    # create a new cube and assign coor value
    def create_cube(self, direction):
        cube = Cube(self.random_coor_generator(direction))
        print(cube.coor)
        print(cube.value)
        print(cube._all)

    # How to manipulate the cubes when Board gets user input?
    # Is Board meant to handle cube moves?
    # Board handling changing coor of a cube
    # it should decide whether to move the cube or not
    # first condition: does it have enough space to move?
    #   if the coor is on the edge, don't move the cube
    # second condition: the coor where the cube is moving, is it empty or occupied?
    #   if it's occupied, the cube should start judging


    # cube judging the value change
    # and its own presence(or coor modifying)... or you can make
    # the cube to let Board know that it should delete the coor of that cube
    def move_cube(self, )


board = Board()

board.create_cube(input())
