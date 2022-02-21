print('\nrange():')
print(range(5))
print(type(range(5)))
print(list(range(5)))
print(list(range(11)))
print(list(range(3)))
print(len(list(range(3))))
print(list(range(0)))
print(list(range(-6)))
print(list(range(10, 21)))

print('\nВсе двухзначные числа')
print(list(range(10, 100)))
print(list(range(1, 100, 10)))
print(list(range(1, 102, 10)))
print(list(range(0, 100, 2)))

print('\nВ обратном порядке')
print(list(range(10, 0, -1)))

print('\nТри способа вызова range()')
print(list(range(10)))
print(list(range(10, 20)))
print(list(range(10, 20, 3)))

print('\nМатематическое использование')
print(sum(range(1, 101)))
print(sum(range(1, 4)))

print('\nДлина')
print(list(range(5, 15, 5)))
print(len(range(5, 15, 5)))

print('\nПрисвоение к переменным')
a, b, c = range(5, 8)
# a, b, c = range(5, 9)  # ValueError: too many values to unpack (expected 3)
print(a, b, c)

print('\nСохранить range() в переменную')
r = range(1, 7)
print(list(r))
print(len(r))
print(r[1])

print('\nITERABLE')
# Объект который возвращает функцию range() или сам объект range() явлеется ИТЕРИРУЕМЫМ (ITERABLE).
# Итерируемый объект -  объект, предоставляющий возможность поочерёдного прохода по своим элементам.
# С помощью функции iter() можно создать из итерируемого объекта итератор и при помощи вызова функции next()
# обойти поочередно все элементы итерируемого объета.

print('\niterator range():')
v = iter(range(5))  # через iter() создаем итератор, который запоминает на каком элементе итерируемого объекта стоит.
print(v)
print(next(v))
print(next(v))
print(next(v))
print(next(v))
print(v.__next__())
# print(v.__next__())  # error: StopIteration

print('\niterator str:')
s = iter('hi')  # через iter() создаем итератор
print(s)
print(next(s))
print(s.__next__())

print('\niterator list:')
n = iter([43, True, 'hello'])  # через iter() создаем итератор
print(n)
print(next(n))
print(next(n))
print(n.__next__())
# print(v.__next__())  # error: StopIteration

print('\nint')
# m = iter(456)  # TypeError: 'int' object is not iterable

print('\nfor')  # for использует только итерируемые объекты, за нас вызывает функцию next()
for i in range(4):
    print(i)
