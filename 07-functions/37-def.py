"""
Функции – это многократно используемые фрагменты программы. При помощи функций можно объединить несколько инструкций
    в один блок, присвоить этому блоку имя и затем, обращаясь по имени этого блока, выполнить инструкции внутри него
    в любом месте программы необходимое число раз.
"""
# Определение функции (осуществляется при помощи инструкции def):


def say_hello():
    print('hello')
    print('world')
    print('and everybody')


def square(x):
    print('Квадрат числа ', x, '=', x ** 2)


def multiply(a, b):
    print(a * b)


def even(a):
    if a % 2 == 0:
        print(a, 'четное')
    else:
        print(a, 'не четное')


def factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr *= i
    print(pr)


print('\nВызов функции:')  # Чтобы вызвать функцию необходимо после ее определения обратиться по ее имени.

print('\nsay_hello():')
say_hello()
print('pause')
say_hello()

print('\nsquare(x):')
square(5)
square(10)
for i in range(1, 11):
    square(i)
# square(3, 4)  # TypeError: square() takes 1 positional argument but 2 were given
# square()      # TypeError: square() missing 1 required positional argument: 'x'

print('\nmultiply(a, b):')
multiply(3, 5)
multiply(70, 100)

print('\neven(a):')
for i in range(20, 31):
    even(i)

print('\nfactorial(n):')
factorial(4)
factorial(5)

print('\nif:')
a, b = 2, 5
if a > b:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')

primer()

print('\nПерезапись функции:')


def primer():
    print('hello')


def primer():
    print('HELLO')


def primer():
    print('hi')


primer()
