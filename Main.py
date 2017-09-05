from Board import Board

def printing(grid): # This is for playing in the terminal but you might need
                    # The logic here when playing on GUI
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

def main(grid):
    won = False # or flag
    while won == False:
        direction = input()
        if board.move_cube(direction) == 1: # You should do something here.....
            print("Did you get in?")
            won = True
        board.create_cube(direction)
        print(won)
        printing(grid)
    else:
        pass

board = Board()
main(board.grid)
