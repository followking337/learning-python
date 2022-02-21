print('\nДвумерный список')
a = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, 17, 19]]
print(a)
print(len(a))
print(a[2])
print(a[2][3])
print(a[0][3])
print(a[0][1])

print('\nТрехмерный список')
b = [[0, 2, 4, 6], [1, 5, 9, 13], [3, 10, [4, 5, 7, 11], 17, 19]]
print(b)
print(b[2])
print(b[2][2][1])

print('\nСписок из строк')
c = ['hello', 'hi', 'world']
print(c[2])
print(c[2][0])
print(c[2][-1])

# Двумерный список как матрица (таблица)
a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]

print('\nСпособы обхода матрицы:')

print('\n1. По элементам')
for i in a:
    for j in i:
        j += 10
        print(j, end=' ')
    print()
print(a)  # Нет индекса и невозможно изменить значения элементов

print('\n2.1 По индексам (фиксируем ряд и обходим по столбцам')
for i in range(3):
    for j in range(4):
        a[i][j] += 10
        print(a[i][j], end=' ')
    print()
print(a)  # Есть индекс и возможно изменить значения элементов

a = [
    [0, 2, 4, 6],
    [1, 5, 9, 13],
    [3, 10, 17, 19]
]

print('\n2.2 По индексам (фиксируем столбцы и обходим по рядам')
for j in range(4):
    for i in range(3):
        print(a[i][j], end=' ')
    print()

print('\n2.3 По индексам (фиксируем ряд и обходим по столбцам справа налево снизу вверх')
for i in range(2, -1, -1):
    for j in range(3, -1, -1):
        print(a[i][j], end=' ')
    print()

print('\nСумма всех строк')
for i in range(3):
    s = 0
    for j in range(4):
        s += a[i][j]
    print(s)

print('\nСумма всех столбцов')
for j in range(4):
    s = 0
    for i in range(3):
        s += a[i][j]
    print(s)

print('\nЗаполнить список')
a = []
n, m = 5, 2  # filas x columnas
# n, m = map(int, input().split())
for i in range(n):
    a.append([1] * m)
for i in a:
    print(i)

print('\nЗаполнить список значениями из клавиатуры')
# a = []
# n, m = map(int, input().split())
# for i in range(n):
#     b = []
#     for j in range(m):
#         b.append(int(input()))
#     a.append(b)
# for i in a:
#     print(i)

print('\nКвадратная матрица')
a = []
n = 5
# n = int(input())
print('Цыкл для заполнения матрицы')
for i in range(n):
    a.append([0] * n)
for i in a:
    print(i)
print('Цыкл для обработки матрицы')
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 10
        elif i > j:
            a[i][j] = 3
        elif i < j:
            a[i][j] = 5
print('Цыкл для вывода матрицы')
for i in a:
    print(i)
