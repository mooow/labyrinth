from labyrinth.labyrinth import Labyrinth
from labyrinth.solver import *
from time import sleep
import curses
from sys import argv
import copy

def main_C(screen, solver):
    while solver.status == Solver.STATUS_UNSOLVED:
        #screen.clear()
        solver.step()
        screen.addstr(1,0,str(solver.count))
        screen.addstr(2,0,str(solver.labyrinth))
        screen.refresh()
        #input("Press ENTER key to continue...")
        sleep(SLEEP)

def run(title, solver):
    screen = curses.initscr()
    screen.addstr(0,0,title)
    curses.wrapper(main_C, solver)
    print(solver.status,solver.count)
    print(solver.labyrinth)

if len(argv) == 3:
    r,c = int(argv[1]), int(argv[2])
else:
    r,c = 15, 40

SLEEP = 0.005
l1 = Labyrinth(r,c, 0.3)
l2 = copy.deepcopy(l1)

run("DFS", DFS_Solver(l1))
input("Premere INVIO per continuare...")
run("BFS", BFS_Solver(l2))
