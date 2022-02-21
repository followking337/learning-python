"""
Замыкание (closure) - ситуация когда вложенная функция пользуется переменными не объявленными в её теле,
    после отработки главной функции, локальная переменная находившиеся в главной функции не будет удалена.

    Для создания замыкания нам понадобиться создать вложенную функцию, которая будет использовать переменную,
    объявленную за ее пределами.
"""


def main_func():
    name = 'Ivan'  # для замыкания не хватает переменной.

    def inner_func():
        print('hello my friend', name)  # пользуемся локальной переменной из главной функции во вложеной функции.

    return inner_func  # inner_func() --> если return нет в теле функции, по умолчанию будет значение None.


print('\nivan():')
ivan = main_func()  # <function main_func.<locals>.inner_func at 0x7fee15eb6790>
print(ivan)         # ссылается на inner_func который находится в main_func
ivan()              # теперь переменная а() является самой функцией

print('\nivan2():')
ivan2 = main_func()
print(ivan2)
ivan2()

print('\nПрименение:')


def main_func(value):
    name = value

    def inner_func():
        print('hello my friend', name)

    return inner_func


print('\nmisha():')
misha = main_func('Misha')  # каждый раз когда вызываем main_func(), мы создаем отдельную область видимости,
# в которых хранятся свои значения, отдельные от других областей видимости вызванные main_func().
misha()  # в этой области видимости хранится 'Misha'

print('\nvasya():')
vasya = main_func('Vasya')
vasya()  # в этой области видимости хранится 'Vasya'

print('\nУпрощение:')


def main_func(name):

    def inner_func():
        print('hello my friend', name)

    return inner_func


print('\nyulia():')
yulia = main_func('Yulia')  # в этой области видимости хранится 'Yulia'
yulia()

print('\nadder():')


def adder(x):

    def inner(y):
        return x + y

    return inner


print('\na2():')
a2 = adder(2)  # scope с переменной x = 2 сохраняется в переменной a2.
print(a2(7))
print(a2(10))

print('\na5():')
a5 = adder(5)
print(a5(7))
print(a5(10))

print('\ncounter():')


def counter():  # считает сколько раз вызывалась функция
    count = 0   # --> переменная которая будет изменятся

    def inner():
        nonlocal count  # указывает на переменную count чтоб возможно было изменить её в другой области видиммости.
        count += 1      # изменяем переменную count
        return count    # возвращаем новое значение переменной count

    return inner


print('\nq():')
q = counter()
print(q())
print(q())
print(q())
print(q())

print('\nr():')
r = counter()
print(r())
print(r())
print(r())
