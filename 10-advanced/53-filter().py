"""
filter(func or None, *iterables) --> iterator filter object

    Return an iterator yielding those items of iterable for which function(item) is true.
    If function is None, return the items that are True.
    Все функции должны возвращать True or False.
    Filter возвращает итератор, в который войдут только те элементы из итерируемой коллекции,
    для которых функция возвращает True.
"""
a = [14, 0, 5, '', 'hello', [5], ' ', 0, [], 471]

print('\nfilter():')
print(list(filter(bool, a)))
print(type(filter(bool, a)))
print(filter(bool, a))

print('\niterator filter():')
rez = filter(bool, a)
for i in rez:
    print(i)
print('-------')
for i in rez:
    print(i)

print('\nfor i in filter():')
for i in filter(bool, a):
    print(i)

print('\n1. Встроенные функции:')
a = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]
print(list(filter(bool, a)))
print([i for i in a if bool(i)])
b = [14, 0, 5, '', 'hello', [5], ' ', 0, [], 471]
print(list(filter(bool, b)))
print([i for i in b if bool(i)])
print(list(filter(None, b)))
# если None, вернуться только те значения которые могут быть приобразованны к True, для которых bool() возвращает True.

print('\n2. Свои функции:')
a = [14, 0, 5, 79, 645, 7952, 18, 0, 192, 471]

print('\n2.1. x > 10:')


def f(x):
    if x > 10:  # return x > 10
        return True
    else:
        return False


print(filter(f, a))
print(list(filter(f, a)))
print([i for i in a if i > 10])

print('\n2.2. x % 2 == 0:')


def f(x):
    return x % 2 == 0


print(list(filter(f, a)))
print([i for i in a if i % 2 == 0])

print('\n2.3. 9 < x < 100:')


def f(x):
    return 9 < x < 100


print(list(filter(f, a)))
print([i for i in a if 9 < i < 100])

print('\n2.4. x % 10 == 2:')


def f(x):
    return x % 10 == 2


print(list(filter(f, a)))
print([i for i in a if i % 10 == 2])

print('\n3. Методы:')
a = '432jfdsHFDS343f'

print(list(filter(str.isdigit, a)))
print(list(filter(str.isalpha, a)))
print(list(filter(str.isupper, a)))

print('\n4. Анонимные функции lambda:')
a = ['world', 'hello', '3243', 'potato', 'carrot', 'hi', 'good morning']

print(list(filter(lambda x: len(x) > 4, a)))
print([i for i in a if len(i) > 4])

d = {
    'Moscow': 800,
    'Boston': 750,
    'LA': 400,
    'SF': 900,
    'Chicago': 650,
    'SP': 600
}

print(list(filter(lambda x: d[x] > 700, d)))
