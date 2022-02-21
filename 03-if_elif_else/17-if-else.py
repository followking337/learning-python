print('\nEgoroff and Stepik HomeWork')

print('\nЗадача №292. Максимум из двух чисел')
# a = int(input())
# b = int(input())
a, b = 1, 2
if a > b:
    print(a)
else:
    print(b)

print('\nЗадача №293. Какое из чисел больше?')
# a = int(input())
# b = int(input())
a, b = 2, 2
if a > b:
    print(1)
else:
    if b > a:
        print(2)
    else:
        print(0)

print('\nАрифметика')
# a, b, c = map(int, input().split())
a, b, c = 8, 54, 432
if a * b == c:
    print('YES')
else:
    print('NO')

print('\nСчастливый билет(1)')
# n = int(input())
n = 5203
a = n // 100000
b = n // 10000 % 10
c = n // 1000 % 10
d = n // 100 % 10
e = n // 10 % 10
f = n % 10
if a + b + c == d + e + f:
    print('YES')
else:
    print('NO')

print('\nСчастливый билет(2)')
n = 5203
s = str(n)
# s = input()
s = s.rjust(6, '0')
print('YES' if sum(map(int, s[:3])) == sum(map(int, s[3:])) else 'NO')

print('\nСчастливый билет(3)')
a = [int(i) for i in '5203']
print(('NO', 'YES')[sum(a[:-3]) == sum(a[-3:])])

print('\nЛадья')
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
x1, y1 = 4, 3
x2, y2 = 7, 3
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

print('\nСлон')
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
x1, y1 = 5, 4
x2, y2 = 7, 2
if x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2:
    print('YES')
else:
    print('NO')

print('\nПодоходный налог')
n = 30000
# n = int(input())
if n >= 20000:
    n = n * (1 - 0.13)
print(n)

print('\nPython')
s = 'C++'
# s = input()
print('ДА' if s == 'Python' else 'НЕТ')

print('\nДва числа')
a = 50
b = 21
# a = int(input())
# b = int(input())
print(a if a > b else b)

print('\nПалиндром (1)')
N = 4554
# N = int(input())
a = N // 1000 % 10
b = N // 100 % 10
c = N // 10 % 10
d = N % 10
if str(N) == (str(d) + str(c) + str(b) + str(a)):
    print('YES')
else:
    print('NO')

print('\nПалиндром (2)')
N = '5432'
# N = input()
print('YES' if N == N[::-1] else 'NO')

print('\nТри натуральных числа')
a, b, c = 4, 5, 9
# a, b, c = map(int, input().split())
print('YES' if a + b == c else 'NO')

print('\nA. Перевод')
s = 'avtor'
t = 'rotva'
# s = input()
# t = input()
print('YES' if t == s[::-1] else 'NO')

print('\nНеворожденный треугольник')
a, b, c = 3, 4, 5
# a = int(input())
# b = int(input())
# c = int(input())
print('YES' if (a + b) > c and (a + c) > b and (b + c) > a else 'NO')

print('\nШахматы')
x = 'f5'
y = 'c3'
# x = input()
# y = input()
s = '_abcdefgh'
x = s.find(x[0]) + int(x[1])
y = s.find(y[0]) + int(y[1])
print('YES' if x % 2 == y % 2 else 'NO')

print('\nПодсчёт функции (1)')
n = 5
# n = int(input())
accumulative = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        accumulative += i
    else:
        accumulative -= i
print(accumulative)

print('\nПодсчёт функции (2)')
if n % 2 == 0:
    print(n // 2)
else:
    print(n // 2 - n)
    print(-(n // 2 + 1))
    print(-n // 2)

print('\nПодсчёт функции (3)')
print(n // 2 - n * (n % 2))
print((-1) ** n * n // 2)

print('\nA. Футбол')
s = '10000000'
# s = input()
flag = 'NO'
for i in range(7, len(s)):
    if '0' * i in s or '1' * i in s:
        flag = 'YES'
        break
print(flag)

print('\nA. Возведение в степень по модулю')
n = 99999999
m = 100000000
# n = int(input())
# m = int(input())
if m <= n:
    print(m)
elif m <= n:
    print(m)
else:
    print(m % (2 ** n))
print(65 % 64)
