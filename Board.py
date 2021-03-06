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
    def random_coor_generator(self, direction, directions):
        end_index = self._board_size-1
        if direction == directions['up']:
            coor = [
                end_index, random.randint(0, end_index)]
        elif direction == directions['down']:
            coor = [
                0, random.randint(0, end_index)]
        elif direction == directions['left']:
            coor = [
                random.randint(0, end_index), end_index]
        elif direction == directions['right']:
            coor = [
                random.randint(0, end_index), 0]
        return coor

    # create a new cube and assign coor value to the cube's value
    def create_cube(self, direction, directions):
        # Make sure the space is empty
        coor = None # You may want to change the name of this variable
        count = 0 # don't try to put a new cube if you can't find a space from one wall
        while count < self._board_size:
            coor = self.random_coor_generator(direction, directions)
            count += 1
            if not self.grid[coor[0]][coor[1]]:
                break
        if count < self._board_size:
            self.grid[coor[0]][coor[1]] = Cube(coor)

    def move_cube(self, direction, directions):
        if direction == directions['up']:
            for i in range(self._board_size):
                for j in range(1, self._board_size):
                    if self.grid[j][i]:
                        if not self.grid[j-1][i]:
                            self.grid[j][i].coor = [j-1,i] # Do I really need this?
                            # below 2 lines actually moving the cube
                            self.grid[j-1][i] = self.grid[j][i]
                            self.grid[j][i] = False
                        else:
                            if self.grid[j-1][i].value == self.grid[j][i].value: # when the values are the same
                                # move the cube, change the coor and change the value of that cube
                                self.grid[j][i].change_value()
                                self.grid[j][i].coor = [j-1,i] # Do I really need this?
                                # below 2 lines actually moving the cube
                                self.grid[j-1][i] = self.grid[j][i]
                                self.grid[j][i] = False
                                if self.grid[j-1][i].tells_winning_or_not():
                                    return 1
        elif direction == directions['down']:
            for i in range(self._board_size):
                for j in range(self._board_size-2, -1, -1):
                    if self.grid[j][i]:
                        if not self.grid[j+1][i]:
                            self.grid[j][i].coor = [j+1,i] # Do I really need this?
                            # below 2 lines actually moving the cube
                            self.grid[j+1][i] = self.grid[j][i]
                            self.grid[j][i] = False
                        else:
                            if self.grid[j+1][i].value == self.grid[j][i].value: # when the values are the same
                                # move the cube, change the coor and change the value of that cube
                                self.grid[j][i].change_value()
                                self.grid[j][i].coor = [j+1,i] # Do I really need this?
                                # below 2 lines actually moving the cube
                                self.grid[j+1][i] = self.grid[j][i]
                                self.grid[j][i] = False
                                if self.grid[j+1][i].tells_winning_or_not():
                                    return 1
        elif direction == directions['left']:
            for i in range(self._board_size):
                for j in range(1, self._board_size):
                    if self.grid[i][j]:
                        if not self.grid[i][j-1]:
                            self.grid[i][j].coor = [i, j-1] # Do I really need this?
                            # below 2 lines actually moving the cube
                            self.grid[i][j-1] = self.grid[i][j]
                            self.grid[i][j] = False
                        else:
                            if self.grid[i][j-1].value == self.grid[i][j].value: # when the values are the same
                                # move the cube, change the coor and change the value of that cube
                                self.grid[i][j].change_value()
                                self.grid[i][j].coor = [i, j-1] # Do I really need this?
                                # below 2 lines actually moving the cube
                                self.grid[i][j-1] = self.grid[i][j]
                                self.grid[i][j] = False
                                if self.grid[i][j-1].tells_winning_or_not():
                                    return 1
        elif direction == directions['right']:
            for i in range(self._board_size):
                for j in range(self._board_size-2, -1, -1):
                    if self.grid[i][j]:
                        if not self.grid[i][j+1]:
                            self.grid[i][j].coor = [i, j+1] # Do I really need this?
                            # below 2 lines actually moving the cube
                            self.grid[i][j+1] = self.grid[i][j]
                            self.grid[i][j] = False
                        else:
                            if self.grid[i][j+1].value == self.grid[i][j].value: # when the values are the same
                                # move the cube, change the coor and change the value of that cube
                                self.grid[i][j].change_value()
                                self.grid[i][j].coor = [i, j+1] # Do I really need this?
                                # below 2 lines actually moving the cube
                                self.grid[i][j+1] = self.grid[i][j]
                                self.grid[i][j] = False
                                if self.grid[i][j+1].tells_winning_or_not():
                                    return 1
