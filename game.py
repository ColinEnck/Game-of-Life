# this code utilizes the curses python library
# documentation can be found here: https://docs.python.org/3/howto/curses.html
import curses

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# close the application
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()