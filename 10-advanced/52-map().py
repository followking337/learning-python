"""
map(__func, __iter1, __iter2, ...) --> iterator, map object

    Make an iterator that computes the function
    using arguments from each of the iterables.
"""
a = [-1, 2, -3, 4, 5]

print('\nmap():')
print(list(map(abs, a)))
print(type(map(abs, a)))
print(map(abs, a))

print('\niterator map():')
rez = map(abs, a)
for i in rez:
    print(i)
print('-------')
for i in rez:
    print(i)

print('\nfor i in map():')
for i in map(abs, a):
    print(i)

print('\n1. Встроенные функции:')
print('abs')
a = [-1, 2, -3, 4, 5]
print(map(abs, a))
print(list(map(abs, a)))  # к каждому элементу применилась функция abs.
print([abs(i) for i in a])  # аналогично: через гениратор списка.

print('\nlen')
a = ['hello', 'hi', 'good morning']
print(list(map(len, a)))

print('\nlist')
b = list(map(list, a))
print(b)

print('\nsorted()')
print(list(map(sorted, b)))

print('\n2. Свои функции:')
a = [-1, 2, -3, 4, 5]


def f(x):  # только 1 аргумент для функции map().
    return x ** 2


print(list(map(f, a)))  # собственная функция f() без аргументов и скобок

print('\n3. Методы:')

print('.upper')
a = ['hello', 'hi', 'good morning']
print(list(map(str.upper, a)))

print('\n4. Анонимные функции lambda:')
a = ['hello', 'hi', 'good morning']
print(list(map(lambda x: x[::-1], a)))
print([i[::-1] for i in a])
print(list(map(lambda x: x + '!!!', a)))
