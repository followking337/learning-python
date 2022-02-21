print('\nStepik and Egoroff HomeWork')

print('\nЗадача 1')
n = 15
# n = int(input())
if n % 3 == 0:
    if n % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)
print('Fizz' * (not n % 3) + 'Buzz' * (not n % 5) or n)
print((n, 'Fizz', 'Buzz', 'FizzBuzz')[(not n % 3) + 2 * (not n % 5)])
d = {(1, 0): 'Fizz', (0, 1): 'Buzz', (1, 1): 'FizzBuzz'}
print(d.get((n % 3 == 0, n % 5 == 0), n))

print('\nЗадача №296. Количество равных из трех')
a, b, c = 7, 8, 7
# a, b, c = [int(input()) for i in range(3)]
if a == b == c:
    print(3)
elif a != b != c and a != c:
    print(0)
else:
    print(2)

print('\nЗадача 3')
m = 4
# m = int(input())
if 0 < m <= 12:
    if m == 1:
        print('Январь')
    elif m == 2:
        print('Февраль')
    elif m == 3:
        print('Март')
    elif m == 4:
        print('Апрель')
    elif m == 5:
        print('Май')
    elif m == 6:
        print('Июнь')
    elif m == 7:
        print('Июль')
    elif m == 8:
        print('Август')
    elif m == 9:
        print('Сентябрь')
    elif m == 10:
        print('Октябрь')
    elif m == 11:
        print('Ноябрь')
    else:
        print('Декабрь')
else:
    print('error')

month = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
         'Декабрь']
print(month[m - 1])
month = [0, 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
         'Декабрь']
print(month[m])

print('\nЗадача 4 (1)')
a = 100
# a = int(input())
if 0 < a <= 100:
    if a < 2:
        print('Младенец')
    elif a < 4:
        print('Малыш')
    elif a < 12:
        print('Ребенок')
    elif a < 19:
        print('Подросток')
    elif a < 65:
        print('Взрослый человек')
    else:
        print('Пожилой человек')
else:
    print('error')

print('Младенец' if a < 2 else 'Малыш' if a < 4 else 'Ребенок' if a < 12 else 'Подросток' if a < 19 else
'Взрослый человек' if a < 65 else 'Пожилой человек')

print('\nЗадача 5')
a = 3.5
b = 2
s = '/'
# a = float(input())
# b = float(input())
# s = input()
if s == '+':
    print(a + b)
elif s == '-':
    print(a - b)
elif s == '*':
    print(a * b)
elif s == '/' and b != 0:
    print(a / b)
else:
    print('Неизвестно')

print('\nЗадача 6')
s = 'qwerty123'
t = 'qwerty'
# s, t = [input() for i in range(2)]
if len(s) < 7:
    print('Short')
elif s == t:
    print('OK')
else:
    print('Difference')
