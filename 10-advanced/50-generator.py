"""
Выражение генератор: не хранит в памяти все свои элементы, а выдает их по одному по мере надобности.
            ({code} for variable in collection)  --> iterator, generator object
Генератор: итератор, элементы которого можно итерировать только один раз.
Итератор: объект, который поддерживает функцию next(). Помнит о том, какой элемент будет браться следующим.
Итерируемый объект: объект, который предоставляет возможность обойти поочередно свои элементы.
    Может быть преобразован к итератору.
"""
print('\nList Comprehension:')
a = [i ** 2 for i in range(1, 6)]
print(a)

print('\nGenerator Expression (Generator Comprehension) Выражение генератор:')
a = (i ** 2 for i in range(1, 6))
print(a)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
# print(next(a))  # StopIteration

print('\nfor:')
b = (i ** 2 for i in range(1, 6))
print('before iteration')
for i in b:
    print(i)
print('after iteration')
for i in b:  # генераторы, как и итераторы, обходятся только один раз.
    print(i)

print('\nsum()')
c = (i ** 2 for i in range(1, 6))
print(sum(c))
print(sum(c))  # генераторы обходятся только один раз.

print('\nПрименение:')  # Элементы генератора не хранятся в памяти все вместе, а формируются на лету.
# c = list(range(1000000000000000000))  # MemoryError
# c = [i for i in range(1000000000000000000)]  # MemoryError
c = (i for i in range(1000000000000000000))  # переменная c не хранит все элементы.

print('\nОграничения:')
a = (i ** 2 for i in range(1, 6))  # i ** 2 for i in range(1, 6) or [(i ** 2 for i in range(1, 6))] can't use.
print(a)
print(list(a))  # посути замена генератора списка
print(list(a))  # [] empty list --> генераторы обходятся только один раз.
# print(len(a))  # TypeError: object of type 'generator' has no len()
# print(a[3])  # TypeError: 'generator' object is not subscriptable
