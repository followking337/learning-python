print('\nYouTube HomeWork')

print('\nЗадача №2938. Дележ яблок - 1 и 2')
n = 3
k = 14
# n = int(input())
# k = int(input())
print(k // n, 'яблок каждому школьнику')
print(k % n, 'яблок останется в корзинке')

number = 179
# number = int(input())

print('\nЗадача №2941. Последняя цифра')
print(number % 10)

print('\nЗадача №2943. Число десятков')
print(number // 10 % 10)

print('\nЗадача №2944. Сумма цифр')
a = number // 100
b = number // 10 % 10
c = number % 10
print(a + b + c)
# print(sum(list(map(int, list(input())))))

print('\nЗадача №3475. Автопробег')
n = 700
m = 750
# n = int(input())
# m = int(input())
print(int(m / n) + (m % n > 0))
print(m // n + (m % n > 0))

print('\nЗадача №3473. Стоимость покупки')
a = 10
b = 15
n = 2
# a = 2
# b = 50
# n = 4
# a = int(input())
# b = int(input())
# n = int(input())
rubles = n * a + n * b // 100
kop = n * b % 100
print(rubles, kop, sep=', ')

print('\nЗадача №2945. Следующее четное')
n = 7
# n = int(input())
print((n + 1) + (n % 2 == 0))  # (n + 2) - (n % 2)  # 2 * (n // 2 + 1)  # (n + 2) // 2 * 2

print('\nЗадача №2947. Электронные часы - 1')
n = 1441
# n = int(input())
print(n // 60 % 24, n % 60, sep=':')
n = n % 1440
print(n // 60, n % 60, sep=':')

print('\nЗадача №3467. Парты')
a = 20
b = 21
c = 21
# a = int(input())
# b = int(input())
# c = int(input())
print((a // 2 + (a % 2 == 1)) + (b // 2 + (b % 2 == 1)) + (c // 2 + (c % 2 == 1)))

print('\nХипстер Вася')
a = 7
b = 3
# a, b = map(int, input().split())
print(min(a, b), (max(a, b) - min(a, b)) // 2)

print('\nЗадача №3469. Электронные часы - 2 (1)')
n = 129700
# n = int(input())
# h = n % 86400 // 60 // 60
h = n // 60 // 60 % 24
# mm = n % 86400 // 60 % 60
mm = n // 60 % 60
ss = n % 86400 % 60
print(h, str(mm).zfill(2), str(ss).zfill(2), sep=':')

print('\nЗадача №3469. Электронные часы - 2 (2)')
n = 129700
# n = int(input())
h = (n // 3600) % 24
mm = n % 3600 // 60
ss = n % 3600 % 60
print(h, ":", mm // 10, mm % 10, ":", ss // 10, ss % 10, sep="")

print('\nВыиграть в лотерею')

print('\n(1)')
n = 476
# n = int(input())
k100 = n // 100
n = n - 100 * k100
k20 = n // 20
n = n - 20 * k20
k10 = n // 10
n = n - 10 * k10
k5 = n // 5
n = n - 5 * k5
print(k100 + k20 + k10 + k5 + n)

print('\n(2)')
n = 476
# n = int(input())
n1 = n // 100  # купюры по 100
n2 = n % 100 // 20  # купюры по 20, после выдачи купюр по 100
n3 = n % 20 // 10  # купюры по 10, после выдачи купюр по 20
n4 = n % 10 // 5  # купюры по 5, после выдачи купюр по 10
n5 = n % 5 // 1  # купюры по 1, после выдачи купюр по 5
print('100:', n1, '20:', n2, '10:', n3, '5:', n4, '1:', n5)
print(n1 + n2 + n3 + n4 + n5)

print('\n(3)')
n = 476
# n = int(input())
k100 = n // 100
n = n % 100
k20 = n // 20
n = n % 20
k10 = n // 10
n = n % 10
k5 = n // 5
n = n % 5
print(k100 + k20 + k10 + k5 + n)

print('\n(4)')
n = 476
# n = int(input())
k = n // 100
n = n % 100
k += n // 20
n = n % 20
k += n // 10
n = n % 10
k += n // 5
n = n % 5
print(k + n)

print('\n(5)')
n = 476
k = 0
for i in [100, 20, 10, 5, 1]:
    k += n // i  # k = k + n // i
    n %= i  # n = n % i
    # print('k:', k, 'n:', n)
print(k)

print('\nПеревод Бит')
n = 8804682956799
tb = n // 8 // 1024 // 1024 // 1024 // 1024
gb = n // 8 // 1024 // 1024 // 1024 % 1024
mb = n // 8 // 1024 // 1024 % 1024
kb = n // 8 // 1024 % 1024
byte = n // 8 % 1024
bit = n % 8
print(tb, 'tb', gb, 'gb', mb, 'mb', kb, 'kb', byte, 'byte', bit, 'bit')

print('\nЗадача №3460. МКАД')
v = -1
t = 1
# v = int(input())
# t = int(input())
print((v * t) % 109)
