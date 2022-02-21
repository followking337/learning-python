print('\nЗадача 1')
# guess = int(input())
# while guess != 0:
#     guess = int(input())

print('\nМишка и старший брат (1)')
a, b = 4, 9
# a, b = map(int, input().split())
years = 0
while a <= b:
    years += 1
    a *= 3
    b *= 2
print(years)

print('\nМишка и старший брат (2)')
a, b = 4, 9
# a, b = map(int, input().split())
year = 0
x = True
while x:
    a *= 3
    b *= 2
    year += 1
    if a > b:
        x = False
print(year)

print('\nЗадача 3')
s = 'Правильность'
# s = input()
print(s)
count = 0
while len(s) > 2:
    s = s[1:-1]
    print(s)
    count += 1
print(count)

print('\nЗадача №113. Список квадратов (1)')
N = 15
# N = int(input())
i = 2
res = 1
while res <= N:
    print(res)
    res = i ** 2
    i += 1

print('\nЗадача №113. Список квадратов (2)')
N = 15
# N = int(input())
i = 1
while i * i <= N:
    print(i * i)
    i += 1

print('\nЗадача №3062. Утренняя пробежка 5')
a, b = 10, 20
# a, b = map(int, input().split())
i = 1
while a < b:
    i += 1
    a *= 1.15
    print(i, a)
print(i)

print('\nВася и носки (1)')
n = 9
m = 3
# n, m = map(int, input().split())
i = 0
while n > 0:
    i += 1
    if i % m == 0:
        n = n
    else:
        n -= 1
print(i)

print('\nВася и носки (2)')
n = 9
m = 3
# n, m = map(int, input().split())
day = 0
while n > 0:
    day += 1
    n -= 1
    if day % m == 0:
        n += 1
print(day)

print('\nЗимний вечер в Бурсе (1)')
n = 8
# n = int(input())
while int(str(n)[0]) != 1 and n < 1000000000:
    n *= int(str(n)[0])  # n = n * int(str(n)[0])
print(n)

print('\nЗимний вечер в Бурсе (2)')
a = '8'
# a = input()
while int(a[0]) != 1 and len(a) < 10:
    a = str(int(a[0]) * int(a))
print(a)

print('\nСтепень двойки? (1)')
n = 8
# n = int(input())
m = 0
while 2 ** m < n:
    m += 1
if 2 ** m == n:
    print(m)
else:
    print('НЕТ')

print('\nСтепень двойки? (2)')
n = 3
# n = int(input())
m = 0
while n >= 1 and n % 2 == 0:
    n //= 2  # n = n // 2
    m += 1
print(m if n == 1 else 'НЕТ')

print('\nБал в БерлГУ')
n = 5
a = sorted([1, 1, 1, 1, 1])
m = 3
b = sorted([1, 2, 3])
# n = int(input())
# a = sorted(list(map(int, input().split())))
# m = int(input())
# b = sorted(list(map(int, input().split())))
i, j, p = 0, 0, 0
while i < n and j < m:
    if abs(a[i] - b[j]) < 2:
        i += 1
        j += 1
        p += 1
    elif a[i] < b[j]:
        i += 1
    else:
        j += 1
print(p)

print('\nВаня и кубики (1)')
n = 25
# n = int(input())
accumulative = 0
row = 0
i = 0
while n - accumulative >= row + (i + 1):
    i += 1
    row += i
    accumulative += row
    print(i, row, accumulative)
print(i)

print('\nВаня и кубики (2)')
n = 25
# n = int(input())
row = 0
i = 0
while n >= row + (i + 1):
    i += 1
    row += i
    n -= row
print(i)

print('\nСистема уравнений (1)')
n, m = 9, 3
# n, m = map(int, input().split())
a = 0
count = 0
while a ** 2 <= n:
    b = n - a ** 2
    print('a:', a, 'b:', b)
    if b >= 0 and a + b ** 2 == m:  # if a + (n - a ** 2) ** 2 == m:
        count += 1
        print(a, b)
    a += 1
print(count)

print('\nСистема уравнений (2)')
n, m = 9, 3
# n, m = map(int, input().split())
b = 0
a = 0
count = 0
while b <= n:
    while a <= m:
        if a ** 2 + b == n and a + b ** 2 == m:
            count += 1
        a += 1
    b += 1
    a = 0
print(count)

print('\nНовогодние свечки')
a, b = 7, 3
# a, b = map(int, input().split())
i = 0
while a > 0:
    a -= 1
    i += 1
    print(a, i)
    if i % b == 0:
        a += 1
print(i)

print('\nНовый год и спешка')
n, k = 3, 222
# n, k = map(int, input().split())
i = 0
remain = 240 - k
print(i, remain)
while remain >= 5 * (i + 1) and i < n:
    i += 1
    remain -= 5 * i
    print(i, remain, 5 * i)
print(i)

print('\nСлияние списков (1)')
n, m = 2, 3
a = [3, 9]
b = [2, 3, 6]
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
c = []
i = 0
while i <= len(a):
    if len(b) == 0 and i == len(a):
        break
    elif len(b) == 0:
        c.append(a[i])
        i += 1
    elif i == len(a):
        c.append(min(b))
        b.remove(min(b))
    else:
        if a[i] < min(b):
            c.append(a[i])
            i += 1
        elif a[i] >= min(b):
            c.append(min(b))
            b.remove(min(b))
    # print(i, b, c)
# print(c)
i = 0
while i < len(c):
    print(c[i], end=' ')
    i += 1

print('\n\nСлияние списков (2)')
n, m = 2, 3
a = [3, 9]
b = [2, 3, 6]
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
c = []
d = a + b
while len(d) > 0:
    c.append(min(d))
    d.remove(min(d))
print(*c)

print('\nСлияние списков (3)')
n, m = 2, 3
a = [3, 9]
b = [2, 3, 6]
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
c = []
while len(a) and len(b) > 0:
    if a[0] > b[0]:
        c.append(b[0])
        b = b[1:]
    else:
        c.append(a[0])
        a = a[1:]
c += a + b
print(*c)

print('\nСлияние списков (4)')
n, m = 2, 3
a = [3, 9]
b = [2, 3, 6]
ss = sorted
# input()
# b = list(map(int, input().split())) + list(map(int, input().split()))
print(*ss(a + b))

print('\nСлияние списков (5)')
n, m = 2, 3
a = [3, 9] + [2, 3, 6]
# n, m = map(int, input().split())
# a = list(map(int, input().split())) + list(map(int, input().split()))
b = []
for i in range(n + m):
    b.append(min(a))
    a.remove(min(a))
print(*b)

print('\nСлияние списков (6)')
n, m = 2, 3
a = [3, 9]
b = [2, 3, 6]
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
c = []
i = j = 0
while i < n and j < m:
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
while i < n:        # if i < n:
    c.append(a[i])  # c += a[i:]
    i += 1
while j < m:        # if j < m:
    c.append(b[j])  # c += b[j:]
    j += 1
for i in c:
    print(i, end=' ')

print('\n\nДело о нулях и единицах (1)')
n = 8
s = '11101111'
# n = int(input())
# s = input()
i = 0
while '1' in s and '0' in s:
    if s[i] == s[i + 1]:
        i += 1
    else:
        s = s[:i] + s[i + 1 + 1:]
        i = 0
print(len(s))

print('\nДело о нулях и единицах (2)')
n = 8
s = '11101111'
# n = int(input())
# s = input()
i = 0
while '01' in s or '10' in s:
    s = s.replace('01', '')
    s = s.replace('10', '')
print(len(s))

print('\nДело о нулях и единицах (3) CodeForces: OK')
n = 8
s = '11101111'
# n = int(input())
# s = input()
print(abs(s.count('1') - s.count('0')))

print('\nДело о нулях и единицах (4)')
n = 4
s = [1, 1, 0, 0]
# n = int(input())
# s = list(map(int, input()))
while 0 in s:
    s.remove(0)
    n -= 2
print(abs(n))
