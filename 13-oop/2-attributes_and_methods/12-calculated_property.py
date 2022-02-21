"""
CALCULATED PROPERTY

    · Функцию декорируем свойством
        - В случае если свойство пустое, делаем вычисление.
        - В случае если свойство НЕ пустое, выводим свойство.
    · Когда изменяем атрибут (уже тоже свойство) от которого зависит первая функция (уже тоже свойство) через setter,
        то в нем обнуляем свойство из функции.
"""


class Square:

    def __init__(self, s):
        self.__side = s
        self.__area = None
        self.__perimeter = None

    @property  # getter property
    def side(self):
        return self.__side

    @side.setter  # setter property
    def side(self, value):
        self.__side = value
        self.__area = None
        self.__perimeter = None

    @property  # getter property
    def area(self):
        if self.__area is None:
            print('calculated area')
            self.__area = self.side ** 2
        return self.__area

    @property  # getter property
    def perimeter(self):
        if self.__perimeter is None:
            print('calculated perimeter')
            self.__perimeter = self.side * 4
        return self.__perimeter


a = Square(7)
print(a.area)  # при первом обращении к свойству делает вычисление
print(a.area)  # при втором и последующих обращениях к свойству обращается уже к свойству
a.side = 3
print(a.area)
print(a.perimeter)
print(a.perimeter)
a.side = 10
print(a.area)
print(a.perimeter)
