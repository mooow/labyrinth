from labyrinth.labyrinth import Labyrinth
from labyrinth.solver import *
from time import sleep
import curses
from sys import argv
from copy import deepcopy

def main(screen, win1, win2):
    l1 = Labyrinth(r,c,p)
    l2 = deepcopy(l1)
    s1 = DFS_Solver(l1)
    s2 = BFS_Solver(l2)

    flag = True
    while flag:
        r1 = run(win1, s1, "DFS")
        r2 = run(win2,s2,"BFS")
        flag = r1 or r2

    screen.addstr(curses.LINES-1, 0, "Press any key to exit... ")
    curses.curs_set(1)
    screen.getch()

def run(win, solver, message):
    if solver.status != Solver.STATUS_UNSOLVED: return False
        #screen.clear()
    solver.step()
    win.addstr(0,0,"{}: {}".format(message, solver.count))
    win.addstr(1,0,str(solver.labyrinth))
    win.refresh()
    #input("Press ENTER key to continue...")
    sleep(s)
    return True

DEFAULT_ROWS = 15
DEFAULT_COLUMNS = 40
DEFAULT_PROBABILITY = 0.15
DEFAULT_SPEED = 0.005


if len(argv) == 5:
    r,c,p,s = int(argv[1]), int(argv[2]), float(argv[3]), float(argv[4])
elif len(argv) == 4:
    r,c,p,s = int(argv[1]), int(argv[2]), float(argv[3]), DEFAULT_SPEED
elif len(argv) == 3:
    r,c,p,s = int(argv[1]), int(argv[2]), DEFAULT_PROBABILITY, DEFAULT_SPEED
else:
    r,c,p,s = DEFAULT_ROWS, DEFAULT_COLUMNS, DEFAULT_PROBABILITY, DEFAULT_SPEED

screen = curses.initscr()
curses.noecho()
curses.curs_set(0)
win1 = curses.newwin(curses.LINES, (curses.COLS-1)//2, 0, 0)
win2 = curses.newwin(curses.LINES, (curses.COLS-1)//2, 0, (curses.COLS+1)//2)
curses.wrapper(main, win1, win2)
