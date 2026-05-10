class Figure:
    def __init__(self):
        pass
    def dimention(self):
        pass
    def perimetr(self):
        pass
    def square(self):
        pass
    def squareSurface(self):
        pass
    def squareBase(self):
        pass
    def height(self):
        pass
    def volume(self):
        pass
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b
class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.c = h
class Circle(Figure):
    def __init__(self, r):
        self.r = r
class Ball(Figure):
    def __init__(self, r):
        self.r = r
class TriangularPyramid(Figure):
    def __init__(self, a, h):
        self.a = a
        self.h = h
class QuadrangularPyramid(Figure):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
class RectangularParallelepiped(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
class Cone(Figure):
    def __init__(self, r, h):
        self.r = r
        self.h = h
class TriangularPrism(Figure):
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h