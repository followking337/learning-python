print('\nStepik and Egoroff HomeWork')

print('\nБольше-меньше')
A = 5
B = 9
# A = int(input())
# B = int(input())
if A > B:
    print('>')
else:
    if A == B:
        print('=')
    else:
        print('<')

print('\nЗадача №294. Максимум из трех')
a = 5
b = 7
c = 21
# a = int(input())
# b = int(input())
# c = int(input())
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)

print('\nТорт')
N = 6
# N = int(input())
if N % 2 == 0:
    print(N // 2)
else:
    if N == 1:
        print(0)
    else:
        print(N)

print('\nЗарплата')
a, b, c = 40, 30, 35
# a, b, c = map(int, input().split())
a1 = abs(a - b)
b1 = abs(a - c)
c1 = abs(b - c)
if a1 > b1:
    if a1 > c1:
        print(a1)
    else:
        print(c1)
else:
    if b1 > c1:
        print(b1)
    else:
        print(c1)

# a, b, c = sorted(map(int, input().split()))
# print(c - a)

if c < b:
    c, b = b, c
if a > c:
    a, c = c, a
if a > b:
    a, b = b, a
print(c - a)

print('\nПетя и строки')
s = 'abcdefg'
t = 'AbCdEfF'
# s = input()
# t = input()
if s.lower() < t.lower():
    print(-1)
else:
    if s.lower() == t.lower():
        print(0)
    else:
        print(1)
print(int(s.lower() > t.lower()) - int(s.lower() < t.lower()))

print('\nКнопочные гонки')
s, v1, v2, t1, t2 = 3, 3, 1, 1, 1
# s, v1, v2, t1, t2 = map(int, input().split())
r1 = s * v1 + 2 * t1
r2 = s * v2 + 2 * t2
if r1 < r2:
    print('First')
else:
    if r1 > r2:
        print('Second')
    else:
        print('Friendship')

print('First' if r1 < r2 else 'Second' if r1 > r2 else 'Friendship')

print('\nГорода')
s = 'ЛОНДОН'
t = 'Норильск'
# s = input()
# t = input()
if s[-1].lower() == t[0].lower():
    print('Good')
else:
    if s[-1].lower() == 'ь' and s[-2].lower() == t[0].lower():
        print('Good')
    else:
        print('Bad')

print('\nБаскетбол')
# x = [[int(j) for j in input().split()] for i in range(4)]
# a = 0
# b = 0
# for i in x:
#     a += i[0]
#     b += i[1]
# print(1 if a > b else 2 if b > a else 'DRAW')

print('\nA. Арбуз')
w = 8
# w = int(input())
print('YES' if w % 2 == 0 and w > 2 else 'NO')

print('\nA. Чет и нечет')
n, k = 11, 7
# n, k = map(int, input().split())
a = []
b = []
for i in range(1, n+1):
    if i % 2 == 1:
        a.append(i)
    else:
        b.append(i)
print((a + b)[k-1])
print(a + b)

if k <= n // 2 + (n % 2 == 1):
    print(2 * k - 1)
else:
    print(2 * (k - n // 2 - (n % 2 == 1)))
