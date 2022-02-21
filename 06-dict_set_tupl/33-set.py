"""
Множество (set) — неупорядоченная коллекция уникальных элементов (отсутствуют повторяющиеся значения),
    хранящая набор уникальных значений и поддерживающая для них операции добавления (add , update),
    удаления (remove,discard,pop) и определения вхождения.

    Как правило, для множеств поддерживаются операции, аналогичные операциям с математическими множествами:
    объединение, пересечение, симметричная разность множеств.

    Множество может хранить только не изменяемые объекты (int, float, bool, str, tuple).
"""
print('\nСозднания множества:')
print('\nСпособ 1')
a = {1, 2, 3}
print(a, type(a))
a = {1, 2, 3, 2, 3, 4, 1, 1, 2, 3}
print(a, type(a))
a = {'hi', 'ha', 'hi', 'he', 'he', 'ha', 'hi', 'ho'}
print(a, type(a))

print('\nСпособ 2')
a = set('abracadabra')
print(a, type(a))
a = set([4, 3, 3, 1, 2, 1])
print(a, type(a))
a = set(range(5))
print(a, type(a))

print('\nПустое множество')
a = set()
print(a, type(a))

print('\nУдаление дублей в списке')
a = [1, 2, 3, 2, 3, 4, 1, 1, 2, 3]
a = list(set(a))
print(a, type(a))

print('\nДобавление в множество')
a = {54, 32, 54, 3, 4, 2}
print(a, type(a))
# a = a.add(9)  # Function 'add' doesn't return anything
a.add(9)
a.add(4)  # 4 no se añade, ya que existe
print(a)
a.update([5, 6, 7, 3])  # = a.add(5), a.add(6), a.add(7), 3 no se añade, ya que existe
print(a)
a.update('hello')
print(a)
a.update(range(5, 10))
print(a)
a.update({4, 5, 6})
print(a)

print('\nУдаление из множества')
a = {54, 32, 54, 3, 4, 2}
print(a, type(a))
a.discard(4)
a.discard(4)  # al eliminar un elemento que no existe, no hará nada ni devolverá ningun error
print(a)
a.remove(3)
# a.remove(3)  # KeyError: 3
print(a)
print(a.pop())  # elimina cualquier valor
print(a.pop())
print(a.pop())
print(a, type(a))
# print(a.pop())  # KeyError: 'pop from an empty set'
a = {54, 32, 54, 3, 4, 2}
print(a, type(a))
a.clear()
print(a, type(a))

print('\nОперации над множествами')
a = {54, 32, 54, 3, 4, 2}
print(a)
print(len(a))
print(4 in a, 7 in a, 9 not in a)

print('\nПересечение множеств без изменений')
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
c = {10, 11, 12}
print(a & b)
print(a & c)
print(a, c)  # a, c не изменились
print(a.intersection(b))
print(a, b)

print('\nПересечение множеств с изменением')
a &= b
print(a, b)
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
a.intersection_update(b)
print(a, b)

print('\nОбъединение множест без изменений')
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
c = {10, 11, 12}
print(a | b)
print(a | c)
print(a, b, c)
print(a.union(b))
print(a)

print('\nОбъединение множест с изменением')
a |= b
print(a, b)
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
a = a.union(b)
print(a, b)

print('\nУдаление пересечений множеств без изменений')
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a - b)
print(b - a)
print(a, b)

print('\nУдаление пересечений множеств с изменением')
a -= b
print(a, b)

print('\nСиметричная разница без изменений')
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a ^ b)

print('\nСравнение без изменений')
a = {4, 3, 2, 1}
b = {3, 4, 5, 6, 7}
print(a == b)  # False
a = {4, 3, 2, 1}
b = {3, 4, 1, 2, 4, 4}
print(a == b)  # True
print(a, b)
a = {4, 3, 2, 1}
b = {1, 2, 3}
print(a < b)  # False
print(a > b)  # True
a = {4, 3, 2, 1}
b = {1, 2, 5}
print(a > b, a < b)  # False False
a = {4, 3, 2, 1}
b = {1, 2, 4}
print(a >= b, a <= b)  # True False

print('\nfor')
a = {4, 3, 2, 1}
for i in a:            # единственный вариант пройти set, пройти по значениям
    print(i, end=' ')  # невозможно проходить по индексам, set не поддерживает индексы
print()
# print(a[1])  # TypeError: 'set' object is not subscriptable

print('\nУпражнение')
text = input()
a = set()
while text != '':
    slova = text.split()
    a.update(slova)
    print(a)
    text = input()
print(len(a))
