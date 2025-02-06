# this code took references from W3Schools: https://www.w3schools.com/python/
# this code utilizes the curses python library
# documentation can be found here: https://docs.python.org/3/howto/curses.html
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

# returns the character to be printed if the cell is alive or dead
def life_char(alive: bool) -> int:
    if alive:
        return curses.ACS_BLOCK
    else:
        return curses.ACS_BOARD

def print_board(stdscr, board: list):
    for i in range(curses.LINES - 1):
        for j in range(curses.COLS):
            stdscr.addch(life_char(board[i][j]))

# updates a cell on the board and draws it to screen
def update(stdscr, board: list, y: int, x: int, life: bool):
    board[y][x] = life
    stdscr.addch(life_char(board[y][x]))
    stdscr.move(y, x)

# changes life state of a piece on the board
def life(board: list, y: int, x: int, life: bool):
    board[y][x] = life

# processes keystrokes
def process_keys(stdscr, board):
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
        if process_keys(stdscr, board) == -1:
            break
        stdscr.refresh()

wrapper(main)
