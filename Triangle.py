import numpy


class Triangle:
    def __init__(self, a, b, c):
        self.setSides(a, b, c)

    def setSides(self, a, b, c):
        self.isNegative(a, b, c)
        self.isTriangle(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b + self.c) / 2
        square = numpy.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return square

    def isNegative(self, a, b, c):
        for x in (a, b, c):
            if x <= 0:
                raise TypeError
        return True

    def isTriangle(self, a, b, c):
        for x in (a, b, c):
            if x >= a + b + c - x:
                raise ValueError
        return True
