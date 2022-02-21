print('\nEgoroff HomeWork')

print('\nТаблица умножения (1)')
n, x = 6, 12
# n, x = map(int, input().split())
i = j = 1
count = 0
while i <= n:
    while j <= n:
        if i * j == x:
            count += 1
        j += 1
    i += 1
    j = 0
print(count)

print('\nТаблица умножения (2)')
n, x = 6, 12
# n, x = map(int, input().split())
i = j = 1
count = 0
while i <= n:
    while j <= n:
        if i * j == x:
            count += 1
            if i != j:
                count += 1
        j += 1
    i += 1
    j = i
print(count)

print('\nТаблица умножения (3)')
n, x = 6, 12
# n, x = map(int, input().split())
i = 1
count = 0  # a = []
while i * i <= x:
    if x % i == 0 and (i <= n and x//i <= n):  # условие 2 - делители i и x//i должны находится в таблице размером n x n
        print(i, x//i)
        count += 1  # a.append(i)
        if i != x//i:
            count += 1  # a.append(x//i)
    i += 1
print(count)  # print(len(a.sort()))
