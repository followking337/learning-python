# Алгоритм Евклида позволяет найти НОД -> Наибольший Общий Делитель, для двух чисел
# Если НОД (a, b) = 1, то a и b взаимопростые числа.
print('\nВариант 1:')
a, b = 21, 35
# a, b = map(int, input().split())
while a != b:
    if a > b:
        a = a - b
    elif a < b:
        b = b - a
print(a)

print('\nВариант 2:')
a, b = 1000000000000, 2
# a, b = map(int, input().split())
while b > 0:
    # c = a % b
    # a = b
    # b = c
    a, b = b, a % b
print(a)

# НОК -> Найменьшее Общее Кратное
# a * b = НОД * НОК
# НОК = a * b / НОД
