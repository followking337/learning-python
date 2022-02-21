from random import randint
"""
Сортировка подсчётом (counting sort) — алгоритм сортировки, в котором используется диапазон чисел сортируемого списка
для подсчёта совпадающих элементов. Применение сортировки подсчётом целесообразно лишь тогда, когда сортируемые числа
имеют диапазон возможных значений, который достаточно мал по сравнению с сортируемым множеством.

Идея сортировки: подсчитываем сколько раз в массиве встречается каждое значение и заполняем массив подсчитанными
элементами в соответствующих количествах.

Ограничения:
    1. Знать заранее диапазон чисел.
    2. Если этот диапазан большой алгоритм не эффективен.
    2. Иметь ввиду смищение.
"""


print('\nПодсчет и сортировка цыфр в списке')
a = [0, 1, 2, 3, 2, 1, 2, 3, 3, 2, 4, 3, 5, 3, 2]
print(a)
count = [0] * 6
print(count)
for i in a:
    count[i] += 1
print(count)
for i in range(len(count)):
    # print(i, count[i])
    print((str(i) + ' ') * count[i], end='')

print('\n\nПодсчет и сортировка цыфр в списке без некоторых цыфр')
a = [2, 1, 2, 3, 2, 1, 2, 3, 3, 2, 5, 3, 5, 3, 2]
print(a)
count = [0] * 6
print(count)
for i in a:
    count[i] += 1
print(count)
for i in range(len(count)):
    if count[i] > 0:
        print(i, count[i])
        # print((str(i) + ' ') * count[i], end='')

print('\n\nПодсчет и сортировка букв в строке с смищением')
s = 'abczjhdf aaajqkfYGg jhgkdf 543 *(^^$&*#'
count = [0] * 26
for i in s.lower():
    if 'a' <= i <= 'z':
        number = ord(i) - 97
        # print(i, number)
        count[number] += 1
for i in range(len(count)):
    if count[i] > 0:
        print(chr(97 + i), count[i])
        # print(chr(97 + i) * letters[i], end='')

print('\n\nПодсчет и сортировка цыфр в списке с смищением')
a = [randint(-10, 10) for i in range(10)]
print(a)
count = [0] * 21
for i in a:
    count[i + 10] += 1
for i in range(len(count)):
    if count[i] > 0:
        print(i - 10, count[i])
        # print((str(i - 10) + ' ') * count[i], end='')
