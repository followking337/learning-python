"""
Функция генератор: могут возвращать значение и приостанавливать свою работу,
    а позднее продолжить свою работу с места остановки.

    Для создания функции генератора используется ключевое слово yield.
"""
print('\nFunction Generator Функция генератор:')


def genf():
    for i in [43, 65, 32]:
        yield i  # yield возвращает значение и замораживает функцию со всеми локальными переменными на этом месте.
# ...и когда вновь запускаем функцию генератор она будет запускаться со следующей строчке после yield.


s = genf()
print(s)
print(next(s))
print(next(s))
print(next(s))
# print(next(s))  # StopIteration

print('\nИтерация через цыкл for:')
for i in genf():
    print(i)

print('\nФункция-генератор:')
# Функция-генератор выдает по одному значению, замораживает свое выполнение, и затем,
# при новом вызове, стартует где она остановилась.


def genf():
    s = 7
    for i in [43, 65, 32]:
        yield i
        print(s)
        s = s * 10 + 7


print(next(genf()))
print(next(genf()))  # генератор запускается заного
print('------------')
g = genf()
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # StopIteration

print('\nПрименение:')


def factorial(n):
    pr = 1
    a = []
    for i in range(1, n + 1):
        pr *= i
        a.append(pr)
    return a


print(factorial(10))  # минус: выделяется память для хранения всех этих чисел.


def factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
        yield pr


print(next(factorial(10)))
print(next(factorial(10)))  # генератор запускается заного
print('------------')
f = factorial(10)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
for i in factorial(10):
    print(i, end=' ')
