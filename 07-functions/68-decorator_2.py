"""
Проблема:
    При обычном создании декоратора теряеться имя и документация оригинальной функции.
"""
from functools import wraps


def table(func):  # декоратор

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


def sqr(x):  # функция которую декорируем
    """
    Функция возводит в квадрат x
    :param x:
    :return:
    """
    print(x ** 2)


print('\nBefore Decorating:')
print(sqr)
print(sqr.__name__)
print(sqr.__doc__)
help(sqr)

print('\nAfter Decorating:')
sqr = table(sqr)
print(sqr)  # теперь функция sqr() ссылается на функцию inner() из функции table()
print(sqr.__name__)  # функция inner()
print(sqr.__doc__)
help(sqr)

print('\n2. Решение:')
print('\n2.1. Вручную:')


def table(func):  # декоратор

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    inner.__name__ = func.__name__  # вне функции inner(), а перед тем как её вернуть return.
    inner.__doc__ = func.__doc__

    return inner


def sqr(x):  # функция которую декорируем
    """
    Функция возводит в квадрат x
    :param x:
    :return:
    """
    print(x ** 2)


print('\nBefore Decorating:')
print(sqr)
print(sqr.__name__)
print(sqr.__doc__)
help(sqr)

print('\nAfter Decorating:')
sqr = table(sqr)
sqr(2)
print(sqr)
print(sqr.__name__)
print(sqr.__doc__)
help(sqr)

print('\n2.2. Декоратор wraps:')


def table(func):  # декоратор

    @wraps(func)  # декоратор wraps за нас сохранил первоначальные переменные имя и доки оригинальной функции.
    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


def sqr(x):  # функция которую декорируем
    """
    Функция возводит в квадрат x
    :param x:
    :return:
    """
    print(x ** 2)


print('\nBefore Decorating:')
print(sqr)
print(sqr.__name__)
print(sqr.__doc__)
help(sqr)

print('\nAfter Decorating:')
sqr = table(sqr)
sqr(2)
print(sqr)
print(sqr.__name__)
print(sqr.__doc__)
help(sqr)
