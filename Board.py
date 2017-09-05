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


board = Board()

board.create_cube(input())
