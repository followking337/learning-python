n = 36
# n = int(input())
print('\nПоиск всех делителей числа: Вариант 1')
i = 1
while i <= n:
    if n % i == 0:
        print(i, end=' ')
    i += 1

print('\n\nПоиск всех делителей числа: Вариант 2. Сокращаем цикл в два раза')
i = 1
while i <= n // 2:
    if n % i == 0:
        print(i, end=' ')
    i += 1
print(n)

print('\nПоиск всех делителей числа: Вариант 3.1')
i = 1
while i * i <= n:  # i <= n**0.5
    if n % i == 0:
        if i == n // i:
            print(i)
        else:
            print(i, n // i)
    i += 1

print('\nПоиск всех делителей числа: Вариант 3.2')
i = 1
a = []
while i * i <= n:  # i <= n**0.5
    if n % i == 0:
        if i == n // i:
            a.append(i)
        else:
            a.append(i)
            a.append(n // i)
    i += 1
a.sort()
print(a)

print('\nПоиск всех делителей числа: Вариант 3.3')
i = 1
a = []
while i * i <= n:  # i <= n**0.5
    if n % i == 0:
        a.append(i)
        if i != n // i:
            a.append(n // i)
    i += 1
a.sort()
print(a)
