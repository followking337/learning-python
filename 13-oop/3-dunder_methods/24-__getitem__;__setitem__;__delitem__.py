"""
DOUBLE UNDERSCORE (dunder) METHODS
    Магические Методы
    __method__ --> методы внутри класса
        · Вызываются (срабатывают):
            1. автоматически в определенный момент времени.
            2. вручную через [instance].__method__()

        __getitem__ --> обращение по индексу к экземпляру:
            - instance[item]
            - instance.__getitem__(item)

        __setitem__ --> присвоение значения по индексу у экземпляра:
            - instance[key] = value
            - instance.__setitem__(key, value)

        __delitem__ --> удаление значения по индексу у экземпляра:
            - del instance[key]
            - instance.__delitem__(key)
"""


class Vector:

    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        # if 0 <= item < len(self.values):
        #     return self.values[item]
        if 1 <= item <= len(self.values):
            return self.values[item - 1]
        else:
            raise IndexError('Индекс за границами коллекции')

    def __setitem__(self, key, value):
        # if 0 <= key < len(self.values):
        #     self.values[key] = value
        if 1 <= key <= len(self.values):
            self.values[key - 1] = value
        elif key > len(self.values):
            diff = key - len(self.values)
            self.values.extend([0] * diff)
            self.values[key - 1] = value
        else:
            raise IndexError('Индекс за границами коллекции')

    def __delitem__(self, key):
        if 0 <= key < len(self.values):
            del self.values[key]
        else:
            raise IndexError('Индекс за границами коллекции')


v1 = Vector(4, 3, 54, 5, 32, 2)
v2 = Vector(1, 2, 3)

print('\n\t__getitem__:')
print(v1)
print(v1.values)
print(v1[1])
print(v1.__getitem__(1))
print(v1[3])
print(v1.__getitem__(3))
# print(v1[6])     # IndexError: Индекс за границами коллекции
# print(v1['hi'])  # TypeError: '<=' not supported between instances of 'int' and 'str'

print('\n\t__setitem__:')
v1[2] = 100  # TypeError: 'Vector' object does not support item assignment (когда метод __setitem__ не определен)
print(v1)
v1.__setitem__(2, 2000)
print(v1)
v2[10] = 200  # IndexError: Индекс за границами коллекции
print(v2)

print('\n\t__delitem__:')
del v1[2]  # AttributeError: __delitem__
print(v1)
v1.__delitem__(2)
print(v1)
