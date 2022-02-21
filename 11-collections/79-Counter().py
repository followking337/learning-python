"""
package collections
    В модуле collections собраны специальные типы данных на основе втроенных.

    class Counter --> dict
        Позволяет посчитать количество вхождения каждого элемента переданной коллекции.
        keys --> bool, int, float, str, tuple
"""
from collections import Counter

s = 'abracadabra'
a = ['Donald', 'Mickey', 'Donald', 'Mickey', 'Mickey']

print('\nCounter():')
letters = Counter(s)
print(letters, type(letters))
words = Counter(a)
print(words, type(words))

print('\nkeys:')
print(words['Donald'], words['Mickey'], words['Arnold'])  # если ключа нет, возвращает 0, а не error

print('\n.items() .keys() .values():')
print(words.items(), type(words.items()))
print(words.keys(), type(words.keys()))
print(words.values(), type(words.values()))

print('\n.elements():')
print(words.elements(), type(words.elements()))
for i in words.elements():
    print(i)  # каждый ключ берется столько раз сколько он встретился
for i in letters.elements():
    print(i)

print('\n.most_common():')
print(words.most_common())  # упорядочный по частоте появления
print(letters.most_common())
print(letters.most_common(1))
print(letters.most_common(2))

print('\nСвойства:')
# r = {}
# for i in [1, 1, 1, 2, 2, 3, 3, 3, 3]:
#     r[i] += 1
# print(r, type(r))  # KeyError: 1

r = Counter()
for i in [1, 1, 1, 2, 2, 3, 3, 3, 3]:
    r[i] += 1
print(r, type(r))

d = Counter([2, 2, 2, 3, 3, 4, 4, 4, 4])
print(d, type(d))

print('\nr + d:')
print(r + d, type(r + d))

print('\nr - d:')
print(r - d, type(r - d))

print('\nd - r:')
print(d - r, type(d - r))

print('\nkeys:')
t = Counter()
print(t, type(t))
t[1] += 5
print(t, type(t))
t[(1, 2, 3)] = 4
print(t, type(t))
t[(1, 2, 3)] += 7
print(t, type(t))
