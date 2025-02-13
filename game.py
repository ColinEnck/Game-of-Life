# this game is an implementation of Conway's Game of Life: https://en.wikipedia.org/wiki/Conway's_Game_of_Life
# this code took references from W3Schools: https://www.w3schools.com/python/
# this code utilizes the curses python library
# documentation can be found here:
# https://docs.python.org/3/howto/curses.html
# https://docs.python.org/3/library/curses.html#module-curses
import curses
from curses import wrapper

f = open("debug.txt", "w")

def create_blank_board(y: int, x: int) -> list:
    board = []
    # for each line on screen, add list to board with dead cells
    for i in range(y):
        line = []
        for j in range(x):
            line.append(False)
        board.append(line)
    return board

# prints the whole board
def print_board(stdscr, board: list):
    for i in range(curses.LINES - 1):
        for j in range(curses.COLS):
            if board[i][j]:
                stdscr.addch(curses.ACS_BLOCK)
            else:
                stdscr.addch(curses.ACS_BOARD)

# updates a cell on the board and draws it to screen
def update(stdscr, board: list, y: int, x: int, life: bool):
    stdscr.move(y, x)
    board[y][x] = life
    if life:
        stdscr.addch(curses.ACS_BLOCK)
    else:
        stdscr.addch(curses.ACS_BOARD)
    stdscr.move(y, x)

# moves time ahead one unit of time
def move_time(stdscr, board: list, y_len: int, x_len: int):
    # save position of cursor
    y_pos, x_pos = stdscr.getyx()
    # cells that are now alive
    alive_cells = []
    # cells that are now dead
    dead_cells = []
    for y in range(0, y_len - 1):
        for x in range(0, x_len - 1):
            neighbors = 0
            # counts number of neighbors
#            for i in range(-1, 1):
#                for j in range(-1, 1):
#                    if i == 0 and j == 0: 
#                        continue
#                    if board[y + i][x + j]:
#                        neighbors += 1
            if board[y-1][x-1]:
                neighbors += 1
            if board[y-1][x]:
                neighbors += 1
            if board[y-1][x+1]:
                neighbors += 1
            if board[y][x-1]:
                neighbors += 1
            if board[y][x+1]:
                neighbors += 1
            if board[y+1][x-1]:
                neighbors += 1
            if board[y+1][x]:
                neighbors += 1
            if board[y][x+1]:
                neighbors += 1

            f.write(str(neighbors))
            if board[y][x] and neighbors < 2:
                dead_cells.append((y, x))
            elif board[y][x] and neighbors > 3:
                dead_cells.append((y, x))
            elif not board[y][x] and neighbors == 3:
                alive_cells.append((y, x))
        f.write('\n')
    f.write("\n---\n")
    for cell in alive_cells:
        update(stdscr, board, cell[0], cell[1], True)
    for cell in dead_cells:
        update(stdscr, board, cell[0], cell[1], False)
    stdscr.move(y_pos, x_pos)

# processes keystrokes
def process_input(stdscr, board: list) -> int:
    key = stdscr.getkey()
    y, x = stdscr.getyx()
    if key == "w":
        if not y == 0:
            stdscr.move(y - 1, x) 
    elif key == "s":
        if not y == curses.LINES - 1:
            stdscr.move(y + 1, x)
    elif key == "a":
        if not x == 0:
            stdscr.move(y, x - 1)
    elif key == "d":
        if not x == curses.COLS - 1:
            stdscr.move(y, x + 1)
    elif key == ",":
        update(stdscr, board, y, x, True)
    elif key == ".":
        update(stdscr, board, y, x, False)
    elif key == "t":
        move_time(stdscr, board, curses.LINES - 1, curses.COLS)
    elif key == "q":
        return -1

def main(stdscr):
    # makes room at the last line for the cursor
    lines = curses.LINES - 1
    cols = curses.COLS

    stdscr.clear()
    board = create_blank_board(lines, cols)
    print_board(stdscr, board)

    while True:
        if process_input(stdscr, board) == -1:
            break
        stdscr.refresh()

wrapper(main)
