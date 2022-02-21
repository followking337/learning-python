print('\nwhile:')

print('\nde 1 a 6:')
i = 1
while i < 6:
    print(i)
    i = i + 1

print('\nde 1 a 20:')
i = 1
while i < 20:
    print(i)
    i = i + 2

print('\nde 1 a 600:')
i = 1
while i < 600:
    print(i)
    i = i * 2

print('\nde 1 a n:')
n = 7
i = 1
while i < n + 1:
    print('hello')
    i = i + 1

print('\nde 20 a 10:')
i = 20
while i >= 10:
    print(i)
    i = i - 1

# a = int(input())
# while a != 0:
#     a = int(input('Повторите ввод: '))

# guess = input()
# password = 'qwerty'
# count = 0
# while guess != password:
#     count += 1
#     guess = input('Пароль не правильный, повторите: ')
# print('Сделано', count, 'попыток')

print('\n.remove():')
a = [1, 2, 3] * 5
print(a)
a.remove(3)
print(a)

print('\n.remove() with while:')
while 3 in a:
    a.remove(3)
    print(a)

print('\n5 no esta en la lista pero no da error porque simplemente no cumple la condicion de while:')
while 5 in a:
    a.remove(5)
print(a)

print('\nwhile in str (1):')
s = 'privet'
while len(s) > 0:
    print(s[0], s[1:])
    s = s[1:]

print('\nwhile in str (2):')
s = 'sgJFie6+5+5wefFAE56+5'
while len(s) > 0:
    bukva = s[0]
    if 'a' <= bukva <= 'z':
        print(bukva, 'small')
    elif 'A' <= bukva <= 'Z':
        print(bukva, 'big')
    elif bukva.isdigit():
        print(bukva, 'digit')
    else:
        print(bukva, 'symbol')
    s = s[1:]
