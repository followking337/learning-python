"""
def f(*args):  --> type(args) == tuple
    {code}

def f(**kwargs):  --> type(kwargs) == dict
    {code}
"""
print('\nПрисваивание переменным значения:')
a, b, c = True, 7, 'hello'
print(a, b, c)

print('\nСписок == Элементы')
a, b, c = [True, 7, 'hello']
# a, b, c = [True, 7, 'hello', 9]  # ValueError: too many values to unpack (expected 3)
# a, b = [True, 7, 'hello']  # ValueError: too many values to unpack (expected 2)
print(a, b, c)

print('\nСписок != Элементы')
*a, b, c = [True, 7, 'hello', 9, '54', 67, 4, 3]
print(a, b, c)
a, *b, c = [True, 7, 'hello', 9, '54', 67, 4, 3]
print(a, b, c)
a, *b, c = (True, 7, 'hello', 9, '54', 67, 4, 3)
print(a, b, c)
a, *b, c = 'hello world'
print(a, b, c)
a, *b, c = [2, 3]  # как минимум два значения если есть оператор *
print(a, b, c)
# a, *b, c = [2]  # ValueError: not enough values to unpack (expected at least 2, got 1)
a, b, *c = [True, 7, 'hello', 9, '54', 67, 4, 3]
print(a, b, c)

print('\nrange():')
print(list(range(1, 5)))
s = [4, -1, -1]
# print(list(range(s)))  # TypeError: 'list' object cannot be interpreted as an integer
print(list(range(*s)))  # print(list(range(4, 10)

print('\nf(a, b, c, d):')


def f(a, b, c, d):
    print(a, b, c, d)


f(1, 2, 3, 4)
a = ('hello', True, 78, [3, 4, 5])
# f(a)  # TypeError: f() missing 3 required positional arguments: 'b', 'c', and 'd'
f(*a)

print('\nf(*args):')


def f(*args):  # при помощи оператор * можно передать в функцию не определенное количество не именованых аргументов
    print(args, type(args))


f(1, 2, 3, 4, 5, 6)
f(1, 2)
f()

print('\nf(*args) for:')


def f(*args):
    s = 0
    for i in args:
        s += i
    return s


print(f(1, 2, 3, 4, 5, 6))
print(f(1, 2))

print('\nf(**kwargs):')


def f(**kwargs):  # при помощи оператор ** можно передать в функцию не определенное количество именованых аргументов
    print(kwargs, type(kwargs))  # (пара ключ-значение).


f(a=1, b=5, c=6)

print('\nf(**kwargs) for:')


def f(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


f(a=1, b=5, c=6, name=89)

print('\nf(*args, **kwargs):')


def f(*args, **kwargs):
    print(args, type(args), kwargs, type(kwargs))


f(5, 4, 3, 5, 7, 7, a=5, b=8, c=6, d='hello')  # вначале передаются не именованные аргументы, затем именованные

print('\nout_print():')  # не определенные не именованные аргументы, определенные именованные аргументы


def out_print(*args, sep='#', end='@'):
    print(args, sep, end)


out_print(1, 2, 3, 4, 5, sep='90')
out_print(1, 2, end=111)
out_print(1, 2)
