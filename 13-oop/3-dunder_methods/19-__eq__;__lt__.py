"""
DOUBLE UNDERSCORE (dunder) METHODS
    Магические Методы
    __method__ --> методы внутри класса
        · Вызываются (срабатывают):
            1. автоматически в определенный момент времени.
            2. вручную через [instance].__method__()

        Методы сравнения, срабатывает когда экземпляр класса участвует в операции сравнения с другим экземпляром:

        __eq__ == (equal)          --> __ne__ != (not equal)
        __lt__ <  (less than)      --> __gt__ >  (
        __le__ <= (less and equal) --> __ge__ >= (

        · Не стоит реализовать все 6 методов, можно обойтись __eq__ (==) и __lt__ (<),
        · Из них получаем противоположные __ne__ (!=) и __gt__ (>),
        · Также комбинируя первые два можем получить __le__ (<=),
        · Имея предыдущий получаем __ge__ (>=)
"""


class Rectangle:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        print('__eq__ called:')
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        print('__lt__ called:')
        if isinstance(other, Rectangle):
            return self.area < other.area
        elif isinstance(other, (int, float)):
            return self.area < other

    def __le__(self, other):
        return self == other or self < other


a = Rectangle(1, 2)
b = Rectangle(1, 2)
c = Rectangle(4, 5)
d = Rectangle(1, 4)
# print(a > b)  # TypeError: '>' not supported between instances of 'Rectangle' and 'Rectangle'
# print(b > 5)  # TypeError: '>' not supported between instances of 'Rectangle' and 'int'
print('\n\tОпределенные методы:')
print(a == b)  # False --> сравнивает id() когда метода __eq__ не определен
print(a == c)
print(b < c)
print(c < b)
print(a <= b)
print(a <= c)
print('\n\tСравнение с числами:')
print(c.area)
print(c < 10)
print(c < 25)
print('\n\tНе определенные методы:')
print(d > c)  # операция > не определенна, python проверяет на операцию <, которая есть.
print(b == d)
print(b != d)  # проверяет на not(b == d)
print(c >= a)
