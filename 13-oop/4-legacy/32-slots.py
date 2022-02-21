"""
SLOTS
    С помощью slots можно задать определенные атрибуты экземплярам класса.

        Преимущества:
        1. Ограничение атрибутов: нельзя создать атрибуты не состоящие в коллекции slots,
            можно только изменять и удалять атрибуты из данной коллекции.
        2. Объекты занимают меньше памяти.
        3. Операции над объектами гораздо быстрее.
"""
from timeit import timeit


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


print('\n1. Ограничение атрибутов:')

p1 = Point(2, 3)

print('\n\tБез __slots__ (без ограничений):')
print(p1.x, p1.y)
p1.q = 100
print(p1.__dict__)


class PointSlots:

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


p2 = PointSlots(3, 4)

print('\n\tС __slots__ (с ограничениями):')
print(p2.x, p2.y)
p2.y = 100
print(p2.x, p2.y)
# p2.q = 500          # AttributeError: 'PointSlots' object has no attribute 'q'
# print(p2.__dict__)  # AttributeError: 'PointSlots' object has no attribute '__dict__'

print('\n2. Объекты занимают меньше памяти:')
print(p1.__sizeof__(), p1.__dict__.__sizeof__())
print(p2.__sizeof__(), p2.__slots__.__sizeof__())

print('\n3. Операции над объектами гораздо быстрее.')


def make_class_Point():
    s = Point(3, 4)
    s.x = 100
    del s.x


def make_class_PointSlots():
    s = PointSlots(3, 4)
    s.x = 100
    del s.x


print(timeit(make_class_Point))
print(timeit(make_class_PointSlots))
