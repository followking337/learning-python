print('\nA. Точки в отрезках')
# n, m = map(int, input().split())
# dots = []
# for i in range(1, m+1):
#     dots.append(i)
# for i in range(1, n+1):
#     l, r = map(int, input().split())
#     for j in range(1, m+1):
#         if l <= j <= r and j in dots:
#             dots.remove(j)
# print(len(dots))
# print(*dots)

print('\nA. Таблица умножения (1)')
n, x = 6, 12
# n, x = map(int, input().split())
count = 0
for i in range(1, n+1):
    for j in range(i, n+1):
        if i * j == x and i == j:
            count += 1
        elif i * j == x:
            count += 2
print(count)

print('\nA. Таблица умножения (2)')
n, x = 6, 12
# n, x = map(int, input().split())
i = 1
count = 0
while i * i <= x:
    if x % i == 0 and i <= n and x//i <= n:
        # print(i, x//i)
        if i != x//i:
            count += 2
        else:
            count += 1
    i += 1
print(count)

print('\nСистема уравнений')
n, m = 9, 3
# n, m = map(int, input().split())
count = 0
for a in range(n+1):
    for b in range(n+1):
        if a**2 + b == n and a + b**2 == m:
            count += 1
print(count)

print('\nA. Лиса и змейка')
n, m = 9, 8
# n, m = map(int, input().split())
turn = 0
for i in range(1, n+1):
    if i % 2 == 1:
        for j in range(1, m + 1):
            print('#', end='')
    elif i % 2 == 0:
        turn += 1
        for j in range(1, m + 1):
            if j == 1 and turn % 2 == 0:
                print('#', end='')
            elif j == m and turn % 2 == 1:
                print('#', end='')
            else:
                print('.', end='')
    print()
print(turn)

print('\nB. Подарок от Лены (1)')
n = 3
# n = int(input())
print('\nIII(- +)\n IV(- -)')
for i in range(n+1):
    print((2*(n-i)) * ' ', end='')
    for j in range(i+1):
        print(j, end=' ')
    print()
for i in range(n-1, -1, -1):
    print((2*(n-i)) * ' ', end='')
    for j in range(i+1):
        print(j, end=' ')
    print()

print('\n I(+ +)\nII(+ -)')
for i in range(n+1):
    for j in range(i, -1, -1):
        print(j, end=' ')
    print()
for i in range(n-1, -1, -1):
    for j in range(i, -1, -1):
        print(j, end=' ')
    print()

print('\nB. Подарок от Лены (2)')
n = 5
# n = int(input())
spaces = 2 * n
for i in range(n+1):
    s = []
    for j in range(i):
        s.append(j)
    print(' ' * spaces, end='')
    print(*s, i, *s[::-1])
    spaces -= 2
spaces = 2
for i in range(n-1, -1, -1):
    s = []
    for j in range(i):
        s.append(j)
    print(' ' * spaces, end='')
    print(*s, i, *s[::-1])
    spaces += 2

print('\nB. Подарок от Лены (3)')
n = 3
# n = int(input())
for i in range(n+1):
    print((2*(n-i)) * ' ', end='')
    for j in range(i+1):
        if i == 0:
            print(j, end='')
        else:
            print(j, end=' ')
        if j == i and j > 0:
            for y in range(j-1, -1, -1):
                if y == 0:
                    print(y, end='')
                else:
                    print(y, end=' ')
    print()
for i in range(n-1, -1, -1):
    print((2*(n-i)) * ' ', end='')
    for j in range(i+1):
        if i == 0:
            print(j, end='')
        else:
            print(j, end=' ')
        if j == i and j > 0:
            for y in range(j-1, -1, -1):
                if y == 0:
                    print(y, end='')
                else:
                    print(y, end=' ')
    print()

print('\nВолосатый бизнес (1)')
n = 5
c = [73, 31, 96, 24, 46]
# n = int(input())
# c = list(map(int, input().split()))
cm_on_max_price_day = 0
profit = 0
day_max_price = -1
for j in range(n):
    cm = 0
    max_price = 0
    for i in range(day_max_price+1, n):
        cm += 1
        if c[i] > max_price:
            max_price = c[i]
            day_max_price = i
            cm_on_max_price_day = cm
    if max_price == 0:
        break
    else:
        profit += max_price * cm_on_max_price_day
    # print(j, max_price, profit)
print(profit)

print('\nВолосатый бизнес (2)')
n = 5
c = [73, 31, 96, 24, 46]
# n = int(input())
# c = list(map(int, input().split()))
profit = 0
i = 0
while i < n:
    max_price = c[i]
    for j in range(i+1, n):
        if c[j] > max_price:
            max_price = c[j]
    profit += max_price
    print(i, max_price, profit)
    i += 1
print(profit)

print('\nВолосатый бизнес (3)')
n = 5
c = [73, 31, 96, 24, 46]
# n = int(input())
# c = list(map(int, input().split()))
i = n - 1
max_price = 0
profit = 0
while i >= 0:
    if c[i] > max_price:
        max_price = c[i]
    profit += max_price
    print(i, max_price, profit)
    i -= 1
print(profit)
