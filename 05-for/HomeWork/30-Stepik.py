print('\nЗадача 1.1')
res = 0
for i in range(1000, 10000):
    x = i
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    if s == 20:
        res += i
    # print(i, summa)
print(res)

print('\nЗадача 1.2')
s = 0
for i in range(1, 10):
    for j in range(10):
        for x in range(10):
            for z in range(10):
                if i + j + x + z == 20:
                    s += int(str(i) + str(j) + str(x) + str(z))
print(s)

print('\nЗадача 2.1')
n = 3
# n = int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=' ')
    print()

print('\nЗадача 2.2')
for i in range(1, n+1):
    print(*range(1, i+1))

print('\nПостулат Бертрана (1)')
n = 2
# n = int(input())
count = 0
for p in range(n+1, 2*n):
    if p % 2 == 0 and p != 2 or p == 1:
        continue
    d = 3
    is_plain = True
    while d * d <= p:
        if p % d == 0:
            is_plain = False
            break
        d += 2
    if is_plain:
        print(p)
        count += 1
print(count)

print('\nПостулат Бертрана (2)')
n = 2
# n = int(input())
count = 0
for p in range(n+1, 2*n):
    for i in range(2, int(p**0.5)+1):
        if p % i == 0:
            break
    else:
        count += 1
        # print(p)
print(count)

print('\nЗадача 4')
a = [3, 7, 1, 10, 8]
# a = list(map(int, input().split()))
for i in a:
    print(i * '*')

print('\nСортировка пузырьком (1)')
n = 7
a = [8, 5, 3, 1, 4, 7, 9]
# n = int(input())
# a = list(map(int, input().split()))
count = 0
for j in range(n-1):
    for i in range(n-1-j):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            count += 1
print(*a)
print(count)

print('\nСортировка пузырьком (2)')
n = 7
a = [8, 5, 3, 1, 4, 7, 9]
# n = int(input())
# a = list(map(int, input().split()))
count = 0
flag = True
while flag:
    flag = False
    for i in range(n-1):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
            count += 1
            flag = True
print(*a)
print(count)

print('\nСортировка вставками (1)')
n = 6
a = [5, 4, 2, 15, 6, 6]
# n = int(input())
# a = list(map(int, input().split()))
for i in range(1, n):
    while a[i] < a[i - 1] and i != 0:
        a[i], a[i - 1] = a[i - 1], a[i]
        i -= 1
print(*a)

print('\nСортировка вставками (2)')
n = 6
a = [5, 4, 2, 15, 6, 6]
# n = int(input())
# a = list(map(int, input().split()))
for j in range(n-1):
    for i in range(n-1-j):
        if a[i] > a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print(*a)

print('\nСортировка вставками (3)')
n = 6
a = [5, 4, 2, 15, 6, 6]
# n = int(input())
# a = list(map(int, input().split()))
for j in range(n-1):
    for i in range(1, n):
        if a[i-1] > a[i]:
            a[i-1], a[i] = a[i], a[i-1]
print(*a)
