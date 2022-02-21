"""
Рекурсия  - это когда функция вызывает саму себя.
    - Функция должна иметь выход (условие для выхода из рекурсии).
"""


def rec(x):
    print(x)
    rec(x + 1)


# rec(1)  # RecursionError: maximum recursion depth exceeded while calling a Python object

print('\nСтэк вызова:')


def rec(x):
    if x < 4:  # условие для выхода из рекурсии
        print(x)
        rec(x + 1)
        print(x)


rec(1)

print('\nFactorial:')


def factorial(x):
    if x == 1:
        return 1
    return factorial(x - 1) * x


print(factorial(4))
print(factorial(10))

print('\nFibonacci:')


def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
# print(fibonacci(70))  # too much time

print('\nПолиндром:')
a = ['шалаш', 'asdffdsa', '', 'a']


def polindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return polindrom(s[1:-1])


print(polindrom('шалаш'))
print(polindrom('шала'))
print(polindrom('ш'))
print(polindrom('шш'))
print(polindrom(''))
