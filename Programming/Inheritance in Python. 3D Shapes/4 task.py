class Shape:
    def volume(self):
        pass

    def surface_area(self):
        pass

class Cube(Shape):
    def __init__(self, a):
        self.a = a

    def volume(self):
        return self.a ** 3

    def surface_area(self):
        return 6 * self.a ** 2

    def getName(self):
        return 'Куб'

class Sphere(Shape):
    def __init__(self, r):
        self.r = r

    def volume(self):
        return (4/3) * 3.14 * self.r**3

    def surface_area(self):
        return 4 * 3.14 * self.r**2

    def getName(self):
        return 'Сфера'

class Cylinder(Shape):
    def __init__(self, r, h):
        self.r = r
        self.h = h

    def volume(self):
        return 3.14 * self.r**2 * self.h

    def surface_area(self):
        return 2 * 3.14 * self.r * (self.r + self.h)

    def getName(self):
        return 'Цилиндр'

class Parallelepiped(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c

    def surface_area(self):
        return 2 * (self.a * self.b + self.b * self.c + self.a * self.c)

    def getName(self):
        return 'Параллелепипед'

class Ellipsoid(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return (4/3) * 3.14 * self.a * self.b * self.c

    def surface_area(self):
        p = 1.6075
        return 4 * 3.14 * ((self.a**p * self.b**p + self.a**p * self.c**p + self.b**p * self.c**p)/3)**(1/p)

    def getName(self):
        return 'Эллипсоид'

def func(l):
    volume_list = []
    for i in l:
        volume_list.append(i.volume())

    for i in range(len(l)):
            if volume_list[i] >= sum(volume_list)-volume_list[i]:
                print(f'Объём: {volume_list[i]}\n'
                      f'Площадь поверхности: {l[i].surface_area()}\n'
                      f'Название: {l[i].getName()}')


l = [Cube(2), Sphere(200), Cylinder(2, 2), Parallelepiped(1, 2, 3), Ellipsoid(1, 2, 3)]
func(l)