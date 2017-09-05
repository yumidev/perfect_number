import random
from Cube import Cube

class Board:
    _board_size = 5
    def __init__(self):
        self.grid = []
        for i in range(self._board_size):
            inner_list=[]
            for j in range(self._board_size):
                inner_list.append(False) # Which is better, False or None?
            self.grid.append(inner_list)

    # get random coor for new cube
    def random_coor_generator(self, direction):
        end_index = self._board_size-1
        try:
            if direction == 'up':
                coor = [
                    end_index, random.randint(0, end_index)]
            elif direction == 'down':
                coor = [
                    0, random.randint(0, end_index), ]
            elif direction == 'left':
                coor = [
                    random.randint(0, end_index), end_index]
            elif direction == 'right':
                coor = [
                    random.randint(0, end_index), 0]
        except ValueError:
            return random_coor_generator(input())
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

    # def move_cube(self, direction):
    #     if direction == 'down':
    #         for i in range(self._board_size):
    #             for j+1 in range(self._board_size):
    #                 if self.grid[i,j] == X:
    #                     # move the cube (change the coor, change the value on the grid)
    #                     # 잠시만요, 리스트 안에 인스턴스를 넣는게 가능합니까?
    #                     # 해본적이 없어서 모르겠네요.. 집에 가면 할 수 있을까요?
    #                     # 일단 지금 너무 배고파요

board = Board()
board.create_cube(input())

def printing(grid):
    for i in range(len(grid)):
        print(grid[i])

printing(board.grid)
