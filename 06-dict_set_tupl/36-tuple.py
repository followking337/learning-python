"""
Кортеж(tuple) — неизменяемая последовательность, обычно используемая для хранения разнотипных объектов.
Кортеж очень похож на список, разница в них в том, что кортеж является неизменяемым объектом.
    Кортежи полезно использовать в следующих ситуациях:
        1. Нужно обеспечить целостность данных внутри коллекции.
        2. Занимают меньше памяти и обрабатываються быстрей, в отличии от списков.
        3. Могут использоваться в качестве ключей в словаре, в отличии от списков.
"""
print('\nСозднания кортежа:')
print('\nСпособ 1')
a = (1, 2, 3, 4, 5)
print(a, type(a))

print('\nСпособ 2')
a = 1, 2, 3, 4, 5
b = 1, 2
c = 1,
d = 1
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print('\nСпособ 3')  # итерабельная последованность
a = tuple(range(5))
print(a, type(a))
a = tuple([1, 2, 3])
print(a, type(a))
a = tuple((1, 2, 3))
print(a, type(a))

print('\nПустой кортеж')
a = ()
print(a, type(a))
a = tuple()
print(a, type(a))

print('\nОперации кортежей')  # сходство со списками
a = (1, 2, 3)
b = 4, 5, 6
c = ()
print(len(a), len(b), len(c))
print(2 in a, 2 in b, 5 in a, 6 not in a)
print(a + b)
print(b + a)
print(a * 3)
print(min(b), max(b))
print(sum(b))

print('\nОбращение по индексу')
a = 1, 'hello', 3, 54, False, 5
print(a[1])
print(a[4])
print(a[-1])

print('\nМетоды')
print('\n.index()')
print(a.index(54))
print(a.index(False))
# print(a.index(6))  # ValueError: tuple.index(x): x not in tuple
print('\n.count()')
print(a.count(3))
print(a.count(6))

print('\nВложеный изменяемый элемент')
a = 1, 'hello', 3, [10, 20, 30], False, 5
print(a[3])
a[3].append(100)
print(a)

print('\n1. Нужно обеспечить целостность данных внутри коллекции')
a = [1, 'hello', 3, [10, 20, 30], False, 5]
b = a
print(a)
print(b)
b[2] = 100
print(a)
print(b)

a = (1, 'hello', 3, [10, 20, 30], False, 5)
b = a
print(a)
print(b)
# b[2] = 100  # TypeError: 'tuple' object does not support item assignment

print('\n2. Занимают меньше памяти и обрабатываються быстрей, в отличии от списков')
a = (1, 'hello', 3, [10, 20, 30], False, 5)
b = [1, 'hello', 3, [10, 20, 30], False, 5]
print(a.__sizeof__())  # bytes
print(b.__sizeof__())  # bytes

print('\n3. Могут использоваться в качестве ключей в словаре, в отличии от списков')
a = (1, 2, 3)
b = [1, 2, 3]
d = {}
d[a] = 'hello'
# d[b] = 'hi'  # TypeError: unhashable type: 'list'
print(d)

print('\nПриобразовать кортеж')
a = (1, 2, 3)
a = list(a)
print(a, type(a))
a.append(100)
a.reverse()
print(a, type(a))
a = tuple(a)
print(a, type(a))

print('\nfor')
a = (1, 'hello', 3, [10, 20, 30], False, 5)
for i in a:
    print(i, end=' ')
print()
for i in range(len(a)):
    print(a[i], end=' ')
print()
