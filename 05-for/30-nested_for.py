print('\nВыводим *')
for i in range(3):
    for j in range(5):
        print('*', end='')
    print()

print('\nВыводим i')
for i in range(3):
    for j in range(5):
        print(i, end='')
    print()

print('\nВыводим j')
for i in range(3):
    for j in range(5):
        print(j, end='')
    print()

print('\nВыводим j в зависимотси от i')
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, end='')
    print()

print('\nВыводим i и j из цыфр')
for i in range(1, 4):
    for j in range(10, 13):
        print(i, j)  # i x j

print('\nВыводим i и j из букв')
for i in 'ab':
    for j in 'cdef':
        print(i, j)  # i x j

print('\nДлина пароля 3')
# from string import printable
# for b1 in printable:
#     for b2 in printable:
#         for b3 in printable:
#             print(b1, b2, b3)

print('\nТаблица умножения')
for j in range(1, 11):
    for i in range(1, 10):
        print(f'{i} x {j} = {i * j}', end=' ')
    print()

print('\nТЫКВА')
k = 0
for b1 in 'tukva':
    for b2 in 'tukva':
        for b3 in 'tukva':
            for b4 in 'tukva':
                for b5 in 'tukva':
                    for b6 in 'tukva':
                        res = b1 + b2 + b3 + b4 + b5 + b6
                        if res[0] in 'tkv' and res[-1] in 'tkv':
                            if res.count('a') + res.count('u') == 2:
                                k += 1
print(5**6)  # 15625 комбинаций слов из 5ти букв в 6ти буквенных словах
print(k)  # ответ по условиям 1944 слов верных из 15625

print('\nЦыкл while внутри цыкла for')
for i in range(150, 176):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    print(i, s)
