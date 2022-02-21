"""
SLOTS
    with:

    · Property:
        - Для использования свойства, они должны быть заданы в переменной __slots__

    · Inheritance:
        - Переменная __slots__ не наследуется дочерним классом, а значит в нем возможно определять любые атрибуты.
        - Если в дочернем классе определяем переменную __slots__:
            1. Расширение: __slots__ = 'color' --> не нужно повторять значения от класса родитель, а добавить новые.
            2. Наследование: __slots__ = tuple() --> назначаем пустую коллекцию,
                наследуем значения от родителя без добавления новых.

"""


class Rectangle:

    __slots__ = 'width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def perimetr(self):
        return (self.width + self.height) * 2

    @property
    def area(self):
        return self.width * self.height


print('\n\tSlots:')
a = Rectangle(4, 5)
print(a.width, a.height)
# a.zz = 100         # AttributeError: 'Rectangle' object has no attribute 'zz'
print(a.area)
print(a.perimetr)
# a.zz = 100         # AttributeError: 'Rectangle' object has no attribute 'zz'
# print(a.__dict__)  # AttributeError: 'Rectangle' object has no attribute '__dict__'


class Rectangle:

    __slots__ = '__width', 'height'

    def __init__(self, a, b):
        self.width = a
        self.height = b

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value


print('\n\tProperty:')
b = Rectangle(5, 6)
print(b.width, b.height)              # width --> property  height --> attribute
print(b._Rectangle__width, b.height)  # width --> private attribute

print('\n\tInheritance:')


class Square(Rectangle):
    pass


print('\n\twithout slots:')
s = Square(5, 5)
s.zz = 100
print(s.__dict__)


class Square(Rectangle):

    __slots__ = 'color'  # разширяя переменную
    # __slots__ = tuple()  # не разширяя переменную

    def __init__(self, a, b, color):
        super().__init__(a, b)
        self.color = color


print('\n\twith slots:')
d = Square(4, 4, 'red')
print(d.width, d.height, d.color)
# print(d.__dict__)  # AttributeError: 'Square' object has no attribute '__dict__'
# d.zz = 100         # AttributeError: 'Square' object has no attribute 'zz'
