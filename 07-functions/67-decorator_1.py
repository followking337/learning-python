"""
Декоратор - это функция, которая в качестве аргумента принимает другую функцию и возвращает функцию-замыкание.
    Декораторы нужны для расширения функционала переданной функции за счет обертки в замыкании.
    Декорируем - это когда подменяем название переменной названием функции которую декорируем.
"""


def decorator(func):

    def inner():
        print('start decorator...')
        func()  # нельзя использовать return бо функция выйдет и не выполнится код ниже.
        print('finish decorator...')

    return inner


def say():      # если хотим разширить функционал функции say() за счет вызова функции decorator(func).
    print('hello world')


def bye():
    print('bye world')


print('\n1.1 Замыкание:')
print('\nd():')
d = decorator(say)
print(d)
d()

print('\nt():')
t = decorator(say)
print(t)
t()

print('\n1.2 inner():')
print('\nsay():')
say = decorator(say)  # декорируеи функцию say() и создаем переменную say() с вызовом.
print(say)            # замыкание, ссылка на функцию inner
say()                 # вызов декорируемой функции.

print('\nbye():')
bye = decorator(bye)
print(bye)
bye()


def decorator(func):

    def inner(n, m):
        print('start decorator...')
        func(n, m)
        print('finish decorator...')

    return inner


def say(name, surname):
    print('hello', name, surname)


print('\n1.3 inner(n, m):')
say = decorator(say)
say('Ivan', 'Ivanov')


def decorator(func):

    def inner(*args, **kwargs):
        print('start decorator...')
        func(*args, **kwargs)
        print('finish decorator...')

    return inner


def say(name, surname, age):
    print('hello', name, surname, age)


print('\n1.4 inner(*args, **kwargs):')
say = decorator(say)
say('Ivan', 'Ivanov', 30)


def header(func):

    def inner(*args, **kwargs):
        print('<h1>')
        func(*args, **kwargs)
        print('</h1>')

    return inner


def say(name, surname, age):
    print('hello', name, surname, age)


print('\n2. header(say):')
say = header(say)
say('Ivan', 'Ivanov', 30)


def table(func):

    def inner(*args, **kwargs):
        print('<table>')
        func(*args, **kwargs)
        print('</table>')

    return inner


def say(name, surname, age):
    print('hello', name, surname, age)


print('\n3. header(table(say)):')
say = header(table(say))  # функцию не декарируют таким образом, а декораторы навышивают.
say('Ivan', 'Ivanov', 30)

print('\n4. Навешевание декораторов:')


@header  # --> say = header(say)
def say(name, surname, age):
    print('hello', name, surname, age)


print('\n4.1. @header:')
say('Ivan', 'Ivanov', 30)


@table  # --> say = table(say)
def say(name, surname, age):
    print('hello', name, surname, age)


print('\n4.2. @table:')
say('Ivan', 'Ivanov', 30)


@header
@table  # --> say = header(table(say))
def say(name, surname, age):
    print('hello', name, surname, age)


print('\n4.3. Вложеные навешевания:')
say('Ivan', 'Ivanov', 30)
