class Figure:
    def __init__(self, a = 0, b = 0, c = 0, d = 0):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def dimention(self):
        pass
    def perimetr(self):
        return None
    def square(self):
        return None
    def squareSurface(self):
        return None
    def squareBase(self):
        return None
    def height(self):
        return None
    def volume(self):
        return self.square()
class Triangle(Figure):
    def __init__(self, a, b, c, d = 0):
        super().__init__(a, b, c)
    def dimention(self):
        return 2
    def perimetr(self):
        return self.a + self.b + self.c
    def square(self):
        p = self.perimetr()/2
        pa = p - self.a
        pb = p - self.b
        pc = p - self.c
        return pa*pb*pc*p ** 0.5
    def __str__(self):
        return f"Triangle {self.a}, {self.b}, {self.c}"
class Rectangle(Figure):
    def __init__(self, a, b, c = 0, d = 0):
        super().__init__(a, b)
    def dimention(self):
        return 2
    def perimetr(self):
        return self.a + self.b
    def square(self):
        return self.a * self.b
    def __str__(self):
        return f"Rectangle {self.a}, {self.b}"
class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c, d)
    def dimention(self):
        return 2
    def perimetr(self):
        return self.a + self.b + self.c + self.d
    def square(self):
        e = abs(self.a - self.b)
        if e != 0:
            p = e + self.c + self.d
            pe = p - e
            pd = p - self.d
            pc = p - self.c
            h_2 = (pe*pd*pc*p ** 0.5 / e)
            return (self.a + self.b) * h_2
        else:
            return self.a * self.c
    def __str__(self):
        return f"Trapeze {self.a}, {self.b}, {self.c}, {self.d}"
class Parallelogram(Figure):
    def __init__(self, a, b, h, d = 0):
        super().__init__(a, b, h)
    def dimention(self):
        return 2
    def perimetr(self):
        return (self.a + self.b) * 2
    def square(self):
        return self.a * self.c
    def __str__(self):
        return f"Parallelogram {self.a}, {self.b}, {self.c}"
class Circle(Figure):
    def __init__(self, r, b = 0 , c = 0 ,d = 0):
        super().__init__(r)
    def dimention(self):
        return 2
    def perimetr(self):
        return self.a * 2 * 3.14
    def square(self):
        return 3.14 * self.a * self.a
    def __str__(self):
        return f"Circle {self.a}"
class Ball(Figure):
    def __init__(self, r, b = 0, c = 0 ,d = 0):
        super().__init__(r)
    def dimention(self):
        return 3
    def squareSurface(self):
        return 4 * 3.14 * self.a * self.a
    def squareBase(self):
        return 0
    def height(self):
        return 2 * self.a
    def volume(self):
        return 4 * 3.14 * self.a * self.a * self.a / 3
    def __str__(self):
        return f"Ball {self.a}"
class TriangularPyramid(Figure):
    def __init__(self, a, h, c =  0, d = 0):
        super().__init__(a, h)
        self.t_b = Triangle(a, a, a)
        t = (h * h + a * a / 3) ** 0.5
        self.t_S = Triangle(a, t, t)
    def dimention(self):
        return 3
    def squareSurface(self):
        return self.t_S.square() * 3 + self.t_b.square()
    def squareBase(self):
        return self.t_b.square()
    def height(self):
        return self.b
    def volume(self):
        return self.squareBase() * self.b
    def __str__(self):
        return f"TriangularPyramid {self.a}, {self.b}"
class QuadrangularPyramid(Figure):
    def __init__(self, a, b, h, d = 0):
        super().__init__(a, b, h)
        self.r_b = Rectangle(a, b)
        t = (h * h + b * b / 4 + a * a / 4) ** 0.5
        self.t_S = Triangle(a, t, t)
    def dimention(self):
        return 3
    def squareSurface(self):
        return self.r_b.square() + 4 * self.t_S.square()
    def squareBase(self):
        return self.r_b.square()
    def height(self):
        return self.c
    def volume(self):
        return self.squareBase() * self.c
    def __str__(self):
        return f"QuadrangularPyramid {self.a}, {self.b}, {self.c}"
class RectangularParallelepiped(Figure):
    def __init__(self, a, b, c, d = 0):
        super().__init__(a, b, c)
        self.r1 = Rectangle(a, b)
        self.r2 = Rectangle(a, c)
        self.r3 = Rectangle(c, b)
    def dimention(self):
        return 3
    def squareSurface(self):
        return 2 * (self.r1.square() + self.r2.square() + self.r3.square())
    def squareBase(self):
        return self.r1.square()
    def height(self):
        return self.c
    def volume(self):
        return self.a * self.b * self.c
    def __str__(self):
        return f"RectangularParallelepiped {self.a}, {self.b}, {self.c}"
class Cone(Figure):
    def __init__(self, r, h, c = 0 , d = 0):
        super().__init__(r, h)
        self.c_b = Circle(r)
    def dimention(self):
        return 3
    def squareSurface(self):
        return self.c_b.square() + ((self.a * self.a + self.b * self.b) ** 0.5) * 3.14 * self.a
    def squareBase(self):
        return self.c_b.square()
    def height(self):
        return self.b
    def volume(self):
        return self.squareBase() * self.b
    def __str__(self):
        return f"Cone {self.a}, {self.b}"
class TriangularPrism(Figure):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c, h)
        self.t_b = Triangle(a, b, c)
    def dimention(self):
        return 3
    def squareSurface(self):
        return self.t_b.square() * 2 + self.d * (self.a + self.b + self.c)
    def squareBase(self):
        return self.t_b.square()
    def height(self):
        return self.d
    def volume(self):
        return self.squareBase() * self.d
    def __str__(self):
        return f"TriangularPrism {self.a}, {self.b}, {self.c}, {self.d}"
if __name__ == "__main__":
    f = open("input03.txt")
    max = Triangle(0, 0, 0)
    for line in f.readlines():
        A = [0] * 5
        i = 0
        for l in line.split():
            A[i] = l
            i += 1
        if A[0] == "Triangle":
            p = Triangle(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "Rectangle":
            p = Triangle(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "Trapeze":
            p = Trapeze(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "Parallelogram":
            p = Parallelogram(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "Circle":
            p = Circle(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "Ball":
            p = Ball(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "TriangularPyramid":
            p = TriangularPyramid(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "QuadrangularPyramid":
            p = QuadrangularPyramid(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "RectangularParallelepiped":
            p = RectangularParallelepiped(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "Cone":
            p = Cone(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if A[0] == "TriangularPrism":
            p = TriangularPrism(int(A[1]), int(A[2]), int(A[3]), int(A[4]))
        if p.volume() >= max.volume():
            max = p
    print(max)
    f.close()