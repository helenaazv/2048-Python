import random #tile placement
import curses #draw the board/arrow key presses/updates display
import copy #stores board state before move

def init_board():  #add tiles and return board
    board = [[0] * 4 for _ in range(4)] #4x4 board
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = []  #store coordinates of empty cells
    
    for i in range(4): #row
        for j in range(4): #column
            if board[i][j] == 0: #empty cell? add to list
                empty_cells.append((i, j))

    if empty_cells:
        i, j = random.choice(empty_cells) #select random (i,j) coordinate
        board[i][j] = 2 if random.random() < 0.9 else 4 #assign 2 or 4 to new tile

def compress(row): #shifts numbers to the left Ex: [0, 2, 0, 4] --> [2, 4, 0, 0]
    new_row = [] 
    for num in row:                   
        if num != 0:                  
            new_row.append(num)     

    nonzero_total = len(new_row)

    new_row += [0] * (4 - nonzero_total) #add 0s to make row have 4 elements again
    return new_row

def merge(row): #combine equal numbers Ex:[2, 2, 0, 0] --> [4, 0, 0, 0]
    for i in range(3):
        if row[i] != 0 and row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    return row

def move_left(board):
    new_board = []
    for row in board:
        row = compress(row) #Ex: [2, 0, 2, 4] --> [2, 2, 4, 0]
        row = merge(row) #Ex: [2, 2, 4, 0] --> [4, 0, 4, 0]
        row = compress(row) #Ex: [4, 0, 4, 0] --> [4, 4, 0, 0]
        new_board.append(row)
    return new_board

def move_right(board): #Moving right = moving left on a reversed row
    board = [row[::-1] for row in board] #Reverse
    board = move_left(board) #Apply
    return [row[::-1] for row in board] #Reverse



def rotate_clockwise(board):
    new_board = [] 

    for i in range(4):  #for each column
        new_row = []    

        for j in range(4):  #for each row, takes from column i, moving bottom to top
            value = board[3 - j][i]
            new_row.append(value)  

        new_board.append(new_row)  

    return new_board

# Clockwise rotation (value = board[3 - j][i]):
#     [a30, a20, a10, a00],
#     [a31, a21, a11, a01],
#     [a32, a22, a12, a02],
#     [a33, a23, a13, a03]



def rotate_counter_clockwise(board): 
    new_board = [] 

    for i in range(4): #for each column
        new_row = [] 

        for j in range(4):  #for each row, takes from row j, moving right to left
            value = board[j][3 - i]
            new_row.append(value)

        new_board.append(new_row)

    return new_board

# Counter-clockwise rotation (value = board[j][3 - i]):
#     [a03, a13, a23, a33],
#     [a02, a12, a22, a32],
#     [a01, a11, a21, a31],
#     [a00, a10, a20, a30]



def move_up(board):
    board = rotate_counter_clockwise(board)
    board = move_left(board)
    board = rotate_clockwise(board)
    return board

def move_down(board):
    board = rotate_counter_clockwise(board)
    board = move_right(board)
    board = rotate_clockwise(board)
    return board


def is_game_over(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0: #empty spaces?
                return False
            if j < 3 and board[i][j] == board[i][j + 1]: #Tile equal to right tile? Merge
                return False
            if i < 3 and board[i][j] == board[i + 1][j]: #Tile equal to tile below? Merge
                return False
    return True

def draw_board(stdscr, board, score): #stdscr = curses screen object
    stdscr.clear()
    stdscr.addstr("2048 Game | Score: {}\n".format(score))
    for row in board:
        stdscr.addstr("+----" * 4 + "+\n")
        stdscr.addstr("".join("|{:^4}".format(num if num != 0 else '') for num in row) + "|\n")
    stdscr.addstr("+----" * 4 + "+\n")
    stdscr.addstr("Use arrow keys to move. Press 'q' to quit.\n")
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0) #Hides the blinking cursor
    stdscr.nodelay(0) #Makes getch() a blocking call, waits for user input
    stdscr.keypad(True) #allows arrow keys

    board = init_board()
    score = 0

    while True:
        draw_board(stdscr, board, score) #redraw board

        key = stdscr.getch() #waits for user

        if key == ord('q'):
            break

        original_board = copy.deepcopy(board) #copies before move

        if key == curses.KEY_LEFT:
            board = move_left(board)
        elif key == curses.KEY_RIGHT:
            board = move_right(board)
        elif key == curses.KEY_UP:
            board = move_up(board)
        elif key == curses.KEY_DOWN:
            board = move_down(board)

        if board != original_board:
            add_new_tile(board) #new tile
            score = sum(sum(row) for row in board) #sums all values for score
            
            if is_game_over(board):
                draw_board(stdscr, board, score)
                stdscr.addstr("Game Over! Press any key to exit.")
                stdscr.getch()
                break

if __name__ == '__main__':
    curses.wrapper(main)
