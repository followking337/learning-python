import pprint
import calendar
import math

"""
Атрибуты модулей:
    1. Имя модуля.
    2. Путь модуля.
    3. Пространство имен модуля.

Синтаксис:
    1. import [module] as [alias]
    2. from [module] import [varibles, functions, ...] as [alias]
    3. from [module] import *
    
PEP8 модулей:
    1. import производится вверху в самом начале.
    2. import --> на новой строчке.
    3. from import --> через запятую.
    
Процесс import:
    1. import находит имя и путь модуля.
    2. превращает в bycode.
    3. запускает импортированный модуль 1 раз.
"""


def say_hello(name):
    print(f'Hello, {name}')


def summa(*args):
    return sum(args)


def factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return f'my func: {pr}'


my_str = 'YO ARE BREATHTAKING'
my_num1 = 2
my_num2 = 3

print('\nimport:')  # импортируется все пространство имен модуля
pprint.pprint(locals())  # locals() выводит список переменных в пространстве имен этого модуля.
print(calendar.TextCalendar().formatyear(2021))
print(dir(math))  # dir() просмотреть пространтсво имен модуля math.
print(math.e)
print(math.pi)
print(math.factorial(10))

print('\nimport as:')
import math as m  # as дает псевдоним
print(m.e)
print(m.pi)
print(m.factorial(10))

print('\nfrom import:')
from math import e, pi, factorial as fact
# from math import *  # import all
print(e)
print(pi)
print(fact(10))  # function factorial from math defined as fact
print(factorial(10))  # my function
