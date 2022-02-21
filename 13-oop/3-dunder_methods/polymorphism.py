"""
Полиморфизм – это возможность обработки разных типов данных, то есть принадлежащих к разным классам, с помощью
    одного и того же имени метода. Мы делаем у разных классов метод с одинаковым названием. С виду после этого у разных
    объектов будет вызываться один и тот же метод, но при этом логика реализации самого метода в разных классах будет своя.
"""


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Rectangle {self.a}x{self.b}'

    def get_rect_area(self):
        return self.a * self.b

    def get_area(self):
        return self.a * self.b


class Square:

    def __init__(self, a):
        self.a = a

    def __str__(self):
        return f'Square {self.a}x{self.a}'

    def get_sq_area(self):
        return self.a ** 2

    def get_area(self):
        return self.a ** 2


class Circle:

    def __init__(self, r):
        self.r = r

    def __str__(self):
        return f'Circle radius={self.r}'

    def get_cir_area(self):
        return 3.14 * self.r ** 2

    def get_area(self):
        return 3.14 * self.r ** 2
