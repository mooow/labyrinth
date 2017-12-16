from labyrinth.point import Point
from labyrinth.matrix import Matrix
import random

class Labyrinth (object):
    TILE_EMPTY     = " "
    TILE_WALL      = "█"
    TILE_SPAWN     = "⦿"
    TILE_EXIT      = "▽"
    TILE_VISITED   = "∙"
    TILE_DEAD      = "☒"

    def __init__(self, x = 80, y = 25, p = 0.15):
        self.size = Point(x,y)
        self.matrix = Matrix(x,y, Labyrinth.TILE_EMPTY)
        self.probability = p
        self.__generate__()

    def __generate__(self):
        for c in range(self.matrix.cols):
            self.matrix[Point(0, c)] = Labyrinth.TILE_WALL
            self.matrix[Point(self.matrix.rows - 1,c)] = Labyrinth.TILE_WALL
        for r in range(self.matrix.rows):
            self.matrix[Point(r, 0)] = Labyrinth.TILE_WALL
            self.matrix[Point(r, self.matrix.cols - 1)] = Labyrinth.TILE_WALL

        # place exit on bottom line
        c = random.randrange(1, self.matrix.cols - 1)
        self.exit = Point(self.matrix.rows - 1, c)
        self.matrix[self.exit] = Labyrinth.TILE_EXIT

        # generate walls
        for r in range(1, self.matrix.rows - 1):
            for c in range(1, self.matrix.cols - 1):
                if random.random() <= self.probability:
                    self.matrix[Point(r,c)] = Labyrinth.TILE_WALL

        # choose spawn Point
        r = random.randrange(1, self.matrix.rows - 1)
        c = random.randrange(1, self.matrix.cols - 1)
        self.spawn = Point(r,c)
        self.matrix[self.spawn] = Labyrinth.TILE_SPAWN

    def __str__(self): return str(self.matrix)
