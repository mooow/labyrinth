from labyrinth.labyrinth import Labyrinth
from labyrinth.point import Point

class Solver(object):
    STATUS_SOLVED     = "Solved"
    STATUS_UNSOLVABLE = "Unsolvable"
    STATUS_UNSOLVED   = "Unsolved"

    def __init__(self, lab):
        self.labyrinth = lab
        self.status = Solver.STATUS_UNSOLVED
        self.count = 0

    def step(self):
        self.__step__()
        self.count += 1

    def __step__(self): raise NotImplementedError

    def __point_in_boundaries__(self, point):
        return point.x in range(self.labyrinth.size.x) and \
                                        point.y in range(self.labyrinth.size.y)

    def __point_untested__(self, point):
        return self.__point_in_boundaries__(point) and \
             self.labyrinth.matrix[point] in [Labyrinth.TILE_EMPTY, \
                                                Labyrinth.TILE_EXIT]

    def __point_is_exit__(self, point):
        return self.labyrinth.exit == point

    def __set_visited__(self, point):
        if point != self.labyrinth.spawn:
            self.labyrinth.matrix[point] = Labyrinth.TILE_VISITED

    def __check__(self, point):
        return self.__point_untested__(point) or \
                                                self.labyrinth.spawn == point

class BFS_Solver(Solver):
    def __init__(self, lab):
        super().__init__(lab)
        self.buffer = [self.labyrinth.spawn]

    def test(self, point):
        if self.__point_untested__(point):
            self.buffer.append(point)

    def __dequeue__(self):
        point = Point(-1,-1)
        while not self.__check__(point): point = self.buffer.pop(0)
        return point

    def __step__(self):
        try:
            point = self.__dequeue__()  # dequeue
            if self.__point_is_exit__(point):
                self.status = Solver.STATUS_SOLVED
            for p in point.neighbours(): self.test(p)
            self.__set_visited__(point)
        except IndexError:
            self.status = Solver.STATUS_UNSOLVABLE

class DFS_Solver(Solver):
    def __init__(self, lab):
        super().__init__(lab)
        self.buffer = [self.labyrinth.spawn]

    def __pop__(self):
        point = Point(-1,-1)
        while not self.__check__(point): point = self.buffer.pop()
        return point

    def test(self, points):
        count = 0
        for point in points:
            if self.__point_untested__(point):
                self.buffer.append(point)
                count += 1
        return count

    def __step__(self):
        try:
            point = self.__pop__()
            if self.__point_is_exit__(point):
                self.status = Solver.STATUS_SOLVED
            if self.test(point.neighbours()) != 0:
                self.labyrinth.matrix[point] = Labyrinth.TILE_VISITED
            else: self.labyrinth.matrix[point] = Labyrinth.TILE_DEAD
        except IndexError:
            self.status = Solver.STATUS_UNSOLVABLE
