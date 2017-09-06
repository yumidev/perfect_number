import random
from Cube import Cube

class Board:
    _board_size = 5
    def __init__(self):
        self.grid = []
        for i in range(self._board_size):
            row_list=[]
            for j in range(self._board_size):
                row_list.append(False) # Which is better, False or None?
            self.grid.append(row_list)

    # get random coor for new cube
    def random_coor_generator(self, direction): # TODO invalid key input error handling
        end_index = self._board_size-1
        if direction == 'u':
            coor = [
                end_index, random.randint(0, end_index)]
        elif direction == 'd':
            coor = [
                0, random.randint(0, end_index)]
        elif direction == 'l':
            coor = [
                random.randint(0, end_index), end_index]
        elif direction == 'r':
            coor = [
                random.randint(0, end_index), 0]
        else:
            return self.random_coor_generator(input())
        return coor

    # create a new cube and assign coor value to the cube's value
    def create_cube(self, direction):
        # Make sure the space is empty
        coor = None # You may want to change the name of this variable
        while True :
            coor = self.random_coor_generator(direction)
            if not self.grid[coor[0]][coor[1]]:
                break
        self.grid[coor[0]][coor[1]] = Cube(coor)

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



    def move_cube(self, direction):
        if direction == 'up':
            for i in range(self._board_size):
                for j in range(1, self._board_size):
                    print("Count: {}".format(self.grid[j][i]))
                    if self.grid[j][i]:
                        if not self.grid[j-1][i]:
                            # move the cube and change the coor and empty the current coor
                            print(self.grid[j][i])
                            self.grid[j][i].coor = [j-1,i] # Do I really need this?
                            self.grid[j-1][i] = self.grid[j][i]
                            self.grid[j][i] = False
                        else:
                            if self.grid[j-1][i].value == self.grid[j][i].value: # when the values are the same
                                # move the cube, change the coor and change the value of that cube
                                self.grid[j][i].change_value()
                                if self.grid[j][i].tells_winning_or_not():
                                    print("Why don't you work??")
                                    return 1
                                self.grid[j-1][i] = self.grid[j][i]
                                self.grid[j][i] = False
        elif direction == 'd':
            pass
