from labyrinth.labyrinth import Labyrinth
from labyrinth.solver import *
from labyrinth.config import Configure
from time import sleep
import curses
from sys import argv
from copy import deepcopy
import logging

def main(screen, conf, win1, win2):
    l1 = Labyrinth(conf['rows'], conf['cols'], conf['prob'])
    l2 = deepcopy(l1)
    s1 = DFS_Solver(l1)
    s2 = BFS_Solver(l2)

    flag = True
    while flag:
        r1 = run(win1, s1, "DFS")
        r2 = run(win2,s2,"BFS")
        flag = r1 or r2
        sleep(conf['delay'])

    win1.addstr(0,0,"DFS: {}, {}".format(s1.count, s1.status))
    win1.refresh()
    win2.addstr(0,0,"BFS: {}, {}".format(s2.count, s2.status))
    win2.refresh()
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
    return True

screen = curses.initscr()
LINES, COLS = curses.LINES, curses.COLS
curses.endwin()

configurator = Configure(LINES, COLS)

logging.debug("LINES=%d COLS=%d" % (LINES,COLS))
logging.debug("CONF: %s" % configurator.conf)

curses.initscr()
curses.curs_set(0)
win1 = curses.newwin(LINES, COLS//2, 0, 0)
win2 = curses.newwin(LINES, COLS//2, 0, COLS//2+1)
curses.wrapper(main, configurator.conf, win1, win2)
