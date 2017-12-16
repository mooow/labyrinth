from labyrinth.point import Point

class Matrix(object):
    def __init__(self, rows, cols, init):
        self.rows = rows
        self.cols = cols
        self.length = rows * cols
        self.vector = [ init for j in range(self.length)]

    def __len__(self): return self.length

    def __point2idx__(self, point):
        assert type(point) == Point
        idx = point.x + self.cols * point.y
        if idx >= self.length: raise IndexError
        return idx

    def __getitem__(self, key):
        idx = self.__point2idx__(key)
        return self.vector[idx]

    def __setitem__(self, key, value):
        idx = self.__point2idx__(key)
        self.vector[idx] = value

    def __str__(self):
        str = ""
        for r in range(self.rows):
            start = r * self.cols
            str += "".join(self.vector[start:start+self.cols]) + '\n'
        return str
