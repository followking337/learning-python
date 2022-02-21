print('\nИсходная программа:')
x = 587
while x > 0:
    last = x % 10
    print(last)
    x = x // 10

print('\nИнфо о цифрах:')
x = 159
count = 0
pares = 0
total = 0
pr = 1
maxim = 0
minim = 9
while x > 0:
    last = x % 10
    count += 1
    if last % 2 == 0:
        pares += 1
    total += last
    pr *= last
    if last > maxim:
        maxim = last
    if last < minim:
        minim = last
    x = x // 10
print('Всего цифр:', count)
print('Всего четных цифр:', pares)
print('Сумма всех цифр:', total)
print('Произведение всех цифр:', pr)
print('Максимальная цифра:', maxim)
print('Минимальная цифра:', minim)

print('\n10ая запись:')
x = 587
last = 0
while x > 0:
    last = x % 10
    print(last)
    x = x // 10

print('\n2ая запись (степени двоек):')  # 1 2 4 8 16
x = 14
last = 0
while x > 0:
    last = x % 2
    print(last)
    x = x // 2

print('\n5ая запись (степени пятерок):')  # 1 5 25
x = 43
last = 0
while x > 0:
    last = x % 5
    print(last)
    x = x // 5
