import random

class Board:
    def __init__(self):
        self.grid = []

    # get random coor for new cube
    def random_coor_generator(direction):
        try:
            if direction = 'up':
                coor = [
                    random.randint(0, board_size-1), 0]
            elif direction = 'down':
                coor = [
                    random.randint(0, board_size-1), board_size-1)]
            elif direction = 'left'
                coor = [
                    board_size-1, random.randint(0, board_size-1)]
            elif direction = 'right'
                coor = [
                    0, random.randint(0, board_size-1)]
        except ValueError:
            return random_coor_generator(input())
        return coor
