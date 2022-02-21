"""
DOUBLE UNDERSCORE (dunder) METHODS
    Магические Методы
    __method__ --> методы внутри класса
        · Вызываются (срабатывают):
            1. автоматически в определенный момент времени.
            2. вручную через [instance].__method__()

        __iter__ --> делает класс итерабельным:
            - iter(instance)
            - instance.__iter__()

        __next__ --> вызывает функцию next() у экземпляра класса, который после вызова __iter__ является итератором:
            - next(instance)
            - instance.__next__()

        · При обходе в цикле for, в случае:
            - отсутствие __iter__ и __next__, наличие __getitem__ --> пользуется последним.
            - наличие __getitem__ и __iter__, отсутствие __next__ --> пользуется __iter__, а __next__ вызывается
                внутри объекта встроенного класса (str, list, ...) а не в созданном классе.
            - наличие __iter__ и __next__ --> пользуется всеми методами внутри созданного класса.

"""


class Mark:

    def __init__(self, values):
        self.value = values
        self.index = 0

    def __iter__(self):
        print('call __iter__ from Mark')
        return self

    def __next__(self):
        print('call __next__ from Mark')
        if self.index >= len(self.value):
            self.index = 0
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter


class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __getitem__(self, item):
        return self.name[item]

    def __iter__(self):
        print('call __iter__ from Student')
        self.index = 0
        # return iter(self.name)    # __next__ вызывается от встроенного класса str
        # return self               # __next__ вызывается от созданного класса Student
        return iter(self.marks)   # __next__ вызывается от созданного класса Mark

    def __next__(self):
        print('call __next__ from Student')
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


m = Mark([3, 4, 5, 6, 3])
igor = Student('Igor', 'Nikolaev', m)

print('\n\tFunctions:')
print(igor)
igor.__iter__()
print(igor)
print(next(igor))
print(next(igor))
print(igor.__next__())
print(igor.__next__())

print('\n\tFor:')
for i in igor:
    print(i)
