"""
При помощи оператора return можно вернуть значение из функции, которое подставится на место вызова.
Если в функции отсутствует оператор return, функция по умолчанию возвращает значение None.
"""
a = abs(-7)
b = max(4, abs(-90), 5, min(80, 200))
print(a)
print(b)

print('\nsquare() with print():')


def square(x):
    print(x**2)
    return None


a = square(6)
print('-------')
print(a)

print('\nsquare() with return:')


def square(x):
    return x**2


a = square(5)
print(a)
a = square(square(3))
print(a)

print('\nexample() with print() and return:')


def example():
    print(1)
    print(2)
    return 'hello'  # return внутри функции работает как break в цыкле - выход из функции
    print(3)
    print(4)


example()
print('-------')
print(example())
print('-------')
a = example()
print('-----')
print(a)

print('\nexample() with 3 returns:')


def example():
    return 1
    return 2
    return 3


print(example())

print('\neven() with return(s):')


def even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def even(x):
    if x % 2 == 0:
        return True
    return False


def even(x):
    return x % 2 == 0


for i in range(1, 11):
    print(i, even(i))

print('\nЧисло сочетаний n по k:')


def factorial(x):
    pr = 1
    for i in range(2, x + 1):
        pr *= i
    return pr


for i in range(1, 8):
    print(i, factorial(i))


def sochet(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


print(sochet(5, 3))

print('\nsquare_and_perimeter() (1):')


def square_and_perimeter(a, b):
    return a * b, 2 * (a + b)  # в случае если возвращается несколько значений, значения возвращаются в виде кортежа.


print(square_and_perimeter(3, 6), type(square_and_perimeter(3, 6)))
square, perimeter = square_and_perimeter(2, 5)
print(square, perimeter)

print('\nsquare_and_perimeter() (2):')


def square_and_perimeter(a, b):
    mas = [a * b, 2 * (a + b)]
    return mas


print(square_and_perimeter(2, 6))
