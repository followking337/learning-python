print('\nEgoroff HomeWork')

print('\nA. Bit++')
# n = int(input())
# x = 0
# for i in range(n):
#     s = input()
#     if '++' in s:
#         x += 1
#     else:
#         x -= 1
# print(x)

print('\nA. Трамвай')
# n = int(input())
# persons = 0
# stops = []
# for i in range(n):
#     a, b = map(int, input().split())
#     persons = persons - a + b
#     stops.append(persons)
# print(max(stops))

print('\nA. Юра и заселение')
# n = int(input())
# count = 0
# for i in range(n):
#     p, q = map(int, input().split())
#     if q - p >= 2:
#         count += 1
# print(count)

print('\nA. Солдат и бананы')
k, n, w = 3, 17, 4
# k, n, w = map(int, input().split())
to_pay = 0
for i in range(1, w+1):
    to_pay += i * k
print(to_pay - n if to_pay > n else 0)
print(to_pay)

print('\nA. Неправильное вычитание')
n, k = 512, 4
# n, k = map(int, input().split())
for i in range(k):
    if n % 10 == 0:
        n //= 10
    else:
        n -= 1
print(n)

print('\nA. Средство от бессонницы')
k, l, m, n, d = 2, 3, 4, 5, 24
# k = int(input())
# l = int(input())
# m = int(input())
# n = int(input())
# d = int(input())
count = 0
for i in range(1, d+1):
    if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
        count += 1
print(count)

print('\nA. Халк')
n = 3
# n = int(input())
s = ''
for i in range(1, n+1):
    if i % 2 == 1:
        s += 'I hate that '
    elif i % 2 == 0:
        s += 'I love that '
print(s.rstrip('that ') + ' it')

print('\nA. Юный физик')
# x = 0
# y = 0
# z = 0
# n = int(input())
# for i in range(n):
#     a = list(map(int, input().split()))
#     x += a[0]
#     y += a[1]
#     z += a[2]
# print('YES' if x == y == z == 0 else 'NO')

print('\nA. Магниты')
# n = int(input())
# symbol = 2
# count = 1
# for i in range(n):
#     s = input()
#     if symbol == int(s[0]):
#         count += 1
#     symbol = int(s[1])
# print(count)

print('\nA. Завидный забор')
# n = int(input())
# for i in range(n):
#     a = int(input())
#     if (360 / (180 - a)) % 1 == 0:
#         print('YES')
#     else:
#         print('NO')
