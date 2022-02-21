"""
DOUBLE UNDERSCORE (dunder) METHODS
    Магические Методы
    __method__ --> методы внутри класса
        · Вызываются (срабатывают):
            1. автоматически в определенный момент времени.
            2. вручную через [instance].__method__()

        __bool__ --> возвращает правдивость объектов True / False
            - bool(instance)
            - [instance].__bool__()
            - if [condition]

        · если метод __bool__ не реализован, смотрит метод __len__
        · если метод __bool__ и метод __len__ не реализованы, выдаст всегда True
        · return True / False
"""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('call __len__')
        return abs(self.x - self.y)


print('\n\twith __len__:')
p1 = Point(1, 2)
p2 = Point(-3, 0)
p3 = Point(0, 0)
p4 = Point(4, 4)
print(bool(p1))
print(bool(p2))
print(bool(p3))
print(bool(p4))
print(p1.__len__())
# print(p1.__bool__())  # AttributeError: 'Point' object has no attribute '__bool__'


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('call __len__')
        return abs(self.x - self.y)

    def __bool__(self):
        print('call __bool__')
        return self.x != 0 or self.y != 0


print('\n\twith __bool__:')
p1 = Point(1, 2)
p2 = Point(-3, 0)
p3 = Point(0, 0)
p4 = Point(4, 4)
print(bool(p1))
print(bool(p2))
print(bool(p3))
print(bool(p4))
print(p1.__len__())
print(p1.__bool__())

print('\n\tif:')
if p2:  # к объекту p2 вызван метод __bool__
    print('hello')
if p3:  # к объекту p3 вызван метод __bool__
    print('hi')
