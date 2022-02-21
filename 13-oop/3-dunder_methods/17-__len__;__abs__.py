"""
DOUBLE UNDERSCORE (dunder) METHODS
    Магические Методы
    __method__ --> методы внутри класса
        · Вызываются (срабатывают):
            1. автоматически в определенный момент времени.
            2. вручную через [instance].__method__()

        __abs__ --> поддерживает числа, срабатывает когда вызывается:
            - abs(instance)
            - [instance].__abs__()

            · У чисел в реализации есть магический метод __abs__ --> int.__abs__()
            · Может возвращать объект любого типа или ничего не возвращать (return None).
            · TypeError: bad operand type for abs(): 'class.__name__' --> когда метод __abs__ не определен

        __len__ --> поддерживает строки, срабатывает когда вызывается:
            - len(instance).
            - [instance].__len__()

            · У строк в реализации есть магический метод __len__ --> str.__len__()
            · ValueError: __len__() should return >= 0 --> обязательно должен возвращать число >= 0: return int >= 0.
            · TypeError: object of type 'class.__name__' has no len() --> когда метод __len__ не определен
"""


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __len__(self):
        return len(self.name + self.surname)


print('hello'.__len__())
print((-78).__abs__())

print('\n__len__:')
a = Person('Victor', 'Robles')
b = Person('David', 'Martinez')
print(len(a))
print(a.__len__())
print(len(b))
print(b.__len__())


class Otrezok:

    def __init__(self, point1, point2):
        self.x1 = point1
        self.x2 = point2

    def __len__(self):
        return abs(self)  # self.__abs__()

    def __abs__(self):
        return abs(self.x2 - self.x1)


a = Otrezok(3, 9)
b = Otrezok(10, 2)

print('\n__len__:')
print(len(a))
print(a.__len__())
print(len(b))
print(b.__len__())

print('\n__abs__:')
print(abs(a))
print(a.__abs__())
print(abs(b))
print(b.__abs__())
