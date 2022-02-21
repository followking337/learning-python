"""
DOUBLE UNDERSCORE (dunder) METHODS
    Магические Методы
    __method__ --> методы внутри класса
        · Вызываются (срабатывают):
            1. автоматически в определенный момент времени.
            2. вручную через [instance].__method__()

        · При создании объекта, к нему привязываются определенные методы:

            __eq__   --> если метод не определен, по умолчанию сравнивает по id

            __hash__ --> математическое односторонние преобразование из объекта в числовое значение
                - если метод не определен, по умолчанию считается по id
                - hash функция для одинаковых значений дает одинаковый hash
                - hash(object)      --> int
                - object.__hash__() --> int
                - если метод __eq__ переопределен, то метод __hash__ слетает, и нужно переопределить вручную
                - hashable objects являются НЕ изменяемыми объектами (у изменяемых нет hash)
                - и значит могут быть ключами в dict
"""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


print('\n\tclass Point (empty):')
p1 = Point(1, 2)
p2 = Point(1, 2)
print(isinstance(p1, object))
print(p1 == p2)
print(id(p1), id(p2))
print(hash(p1), hash(p2))
print(p1.__hash__(), p2.__hash__())


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


print('\n\tclass Point (with __eq__ and __hash__):')
p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)
print(p1 == p2)
print(p1 == p3)
print(hash(p1), hash(p2), hash(p3))
print(p1.__hash__(), p2.__hash__(), p3.__hash__())
d = {p1: 100}  # после определения hash экземпляр может быть ключом в dict
print(d)
