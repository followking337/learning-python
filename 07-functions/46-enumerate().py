"""
enumerate(__iterable, start: int) --> iterator enumerate object

    Функция возвращает объект, который генерирует кортежи,
    состоящие из двух элементов - индекса элемента и самого элемента.
    Функция должна обязательно принимать итерируемую коллекцию (list, tuple, dict, set, str, range()).
"""
a = [10, 20, 30, 40, 50, 60]

print('\nenumerate():')
print(list(enumerate(a)))
print(type(enumerate(a)))  # class enumerate
print(enumerate(a))  # enumerate object, iterator

print('\niterator enumerate():')
rez = enumerate(a)
for i in rez:
    print(i)
print('-------')
for i in rez:
    print(i)

print('\nfor i in enumerate():')
for t1, t2 in enumerate(a):
    print(t1, t2)
print('-------------')
for i in enumerate(a):
    print(*i)

print('\nlist for par')
for i in enumerate(a):
    print(i)

print('\nlist for index, value')
for index, value in enumerate(a):
    print(index, value)

print('\nlist for index, value; if')
for index, value in enumerate(a):
    if value % 20 == 0:
        print(index, value)

print('\nlist for index, value')
for index, value in enumerate(a):
    # value += 1  # не меняет значение в списке
    a[index] = value + 1  # меняет значение в списке; a[index] += 1
print(a)

print('\nstr')
s = 'hello'
for index, value in enumerate(s):
    print(index, value)

print('\ntuple')
t = ('apple', 'banana', 'mango')
for index, value in enumerate(t):
    print(index, value)

print('\ndict')
d = {'a': 1, 'b': 2, 'c': 3}
for index, value in enumerate(d):
    print(index, value)

print('\nrange()')
for index, value in enumerate(range(10, 20)):
    print(index, value)

print('\nstart index')
for index, value in enumerate(t, 10):
    print(index, value)
print()
for index, value in enumerate(a, 100):
    print(index, value)
print()
for index, value in enumerate(a, 1):
    print(index, value)
print()
