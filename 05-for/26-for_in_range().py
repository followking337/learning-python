from random import randint

print('\nИспользования for')

print('\n1й вариант: обход заданной последованности:')
for i in range(4):  # i - переменная цыкла
    print(i)
    i = 'hello'
    print(i)

print('\nПоследние значение переменной цыкла запоминается:')
for i in range(4):
    print('inside', i)
print('outside', i)

print('\nПо условию if:')
for i in range(10, 100):
    if i % 2 == 0 and i % 7 == 0:
        print(i)

print('\nВыводим квадрат чисел:')
for i in range(1, 11):
    print(i, i**2)

print('\nСумма всех чисел:')
s = 0
for i in range(1, 6):
    s += i
print(s)

print('\nФакториал числа 4!:')  # 4! = 1 * 2 * 3 * 4
pr = 1
for i in range(1, 5):
    pr *= i
print(pr)

print('\nФакториал числа n!:')  # n! = 1 * 2 * ... * (n-1) * n
# n = int(input())
# pr = 1
# for i in range(1, n+1):
#     pr *= i
# print(pr)

print('\n2й вариант: повторять действия какоето количество раз:')  # где i не задействована в блоке for
for i in range(4):
    print('hello')

print('\nСумма рандомных чисел:')
s = 0
for i in range(3):
    a = randint(1, 10)
    s += a
    print(a, end=' ')
print()
print(s)

print('\nЕлочка:')
for i in range(1, 11):
    print('*' * i)

print('\nСтепень двойки:')
for i in range(1, 11):
    print(2**i)

print('\nСумма введенных чисел:')
# n = int(input())
# s = 0
# for i in range(n):
#     a = int(input())
#     s += a
#     print('Current summa =', s)
# print('Total =', s)
# print(s / n)
