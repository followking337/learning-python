"""
zip(__iter1, __iter2, ...) --> iterator zip object

    Функция возвращает объект, который генерирует кортежи по индексу [i] (индекс элемента [i] в итерируемом объекте),
    состоящие из n элементов - количество n итерируемых объектов (имеющие одинаковый индекс).
    Функция должна обязательно принимать итерируемую коллекцию (list, tuple, dict, set, str, range()).
"""
a = [5, 6, 7, 8]
b = [100, 200, 300, 400]

print('\nfor:')
for i in range(4):
    print(a[i], b[i])  # IndexError: list index out of range (in case if one of arrays is shorter then another).

print('\nzip():')
a = [5, 6, 7]
b = [100, 200, 300, 400]
print(list(zip(a, b)))  # определяет найменшую длину списков и выводит пары значений (по индексам) передоваемых списков.
print(type(zip(a, b)))  # class zip
print(zip(a, b))  # zip object, iterator

print('\niterator zip():')
rez = zip(a, b)
for i in rez:
    print(i)
print('-------')
for i in rez:  # элементы итератора можно итерировать (обходить) только один раз.
    print(i)
# Ограничения Итераторов:
# print(len(rez))  # TypeError: object of type 'zip' has no len()
# print(len(rez[0]))  # TypeError: 'zip' object is not subscriptable

print('\n3 аргумента:')
a = [5, 6, 7, 8]
b = [100, 200, 300, 400]
c = 'abcd'
print(list(zip(a, b, c)))  # количество кортежей определяется минимальной длинной всех коллекций в функции zip.
a = [5, 6, 7, 8]
b = [100, 200, 300]
c = 'abcd'
print(list(zip(a, b, c)))

print('\nfor i in zip():')
for t1, t2, t3 in zip(a, b, c):
    print(t1, t2, t3)
print('-------------')
for i in zip(a, b, c):
    print(*i)

print('\nОбратно:')
a = [5, 6, 7, 8]
b = [100, 200, 300, 400]
c = 'abcd'
rez = zip(a, b, c)
# print(*list(rez))
a, b, c = zip(*rez)
print(a, b, c)
