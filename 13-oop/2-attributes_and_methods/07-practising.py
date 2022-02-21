from math import sqrt


class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.x = 0
        self.y = 0


p1 = Point(3, 4)
p2 = Point(-54, 32)
p3 = Point()


class Point:

    list_points = []

    def __init__(self, x=0, y=0):
        self.move_to(x, y)
        Point.list_points.append(self)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'Точка с координатами ({self.x}, {self.y})')

    def calc_distance(self, another_point):
        if not isinstance(another_point, Point):
            raise ValueError('Аргумент должен принадлежать классу Point')
        return sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)


p4 = Point(4)
p4.move_to(8, 8)
p4.go_home()
print(p4)

p5 = Point()
p5.print_point()
p5.move_to(7, -43)
p5.print_point()

p7 = Point(6, 0)
p8 = Point(0, 8)
# p7.calc_distance(90)  # ValueError: Аргумент должен принадлежать классу Point
print(p7.calc_distance(p8))

p9 = Point()
print(Point.list_points)
print(p9)

p10 = Point(4, 5)
print(Point.list_points[-1])
print(Point.list_points[-1].x, Point.list_points[-1].y)
print(p10.__dict__)
