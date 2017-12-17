class Point (object):
    def __init__(self, y = 0, x = 0):
        self.x, self.y = x, y

    def __eq__(self, point):
        if type(point) != Point: raise ValueError
        return self.x == point.x and self.y == point.y

    #def __init__(self, point):
    #    assert type(point) == Point
    #    self.__init__(point.x, point.y)

    def distance(self, point):
        assert type(point) == Point
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2 )  ** 0.5

    def neighbours(self):
        yield Point(self.y-1, self.x)   # NORD
        yield Point(self.y, self.x+1)   # EST
        yield Point(self.y+1, self.x)   # SUD
        yield Point(self.y, self.x-1)   # OVEST
