from Board import Board

# This is for playing in the terminal but you might need the logic here when playing on GUI
def printing(grid):
    print_grid = []
    count_empty_block = 0

    for i in range(Board._board_size):
        row_list = []
        for j in range(Board._board_size):
            if grid[i][j]:
                row_list.append(grid[i][j].value)
            else:
                row_list.append(0)
                count_empty_block += 1
        print_grid.append(row_list)

    for i in range(Board._board_size): # only this part is doing actual printing. Others should be separated.
        print(print_grid[i])

    if not count_empty_block: # see if you can separate this block of code
        for i, j in ((i,j) for i in range(Board._board_size) for j in range(Board._board_size-1)):
            if print_grid[i][j] == print_grid[i][j+1] or print_grid[j][i] == print_grid[j+1][i]:
                return
        print("Game finished. You lose")
        return 1

def input_validation(user_input, valid_inputs):
    if user_input in valid_inputs:
        return user_input
    else:
        print("Please enter a character in this list: {}".format("characters list"))
        return input_validation(input(), valid_inputs)

def main(board):
    directions = {'up': 'i', 'down': 'k', 'left': 'j', 'right': 'l'} # make only the main function control valid_inputs
    # for terminal game, you can make the value as set and make the board to use the values. You just need to change == to in.
    print("Your goal is to get number 128")
    print("Enter a character from this list - up: i, down: k, left: j, right: l")

    flag = False # to tell the game is finished
    while flag == False:
        direction = input_validation(input(), directions.values())
        if board.move_cube(direction, directions) == 1: # You should do something here.....
            flag = True
        board.create_cube(direction, directions)
        if printing(board.grid) == 1:
            flag = True

main(Board())
