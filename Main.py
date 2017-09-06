from Board import Board

def printing(grid): # This is for playing in the terminal but you might need
                    # the logic here when playing on GUI
    print_grid = []
    for i in range(len(grid)):
        row_list = []
        for j in range(len(grid)):
            if grid[i][j]:
                copy_value = grid[i][j].value # Let's see if I can make this as one line
                row_list.append(copy_value)
            else: row_list.append(0)
        print_grid.append(row_list)
    for i in range(len(grid)):
        print(print_grid[i])

def input_validation(user_input):
    valid_inputs = ('u', 'd', 'l', 'r')
    if user_input in valid_inputs:
        return user_input
    else:
        print("Please enter a character in this list: {}".format("characters list"))
        return input_validation(input())

def main(grid):
    won = False # or flag
    while won == False:
        direction = input_validation(input())
        if board.move_cube(direction) == 1: # You should do something here.....
            won = True
        board.create_cube(direction)
        printing(grid)

board = Board()
main(board.grid)
