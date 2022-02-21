from datetime import datetime
from time import perf_counter


def average_numbers():
    numbers = []

    def inner(number):
        numbers.append(number)
        print(numbers)
        return sum(numbers) / len(numbers)

    return inner


print('\naverage_numbers():')
r = average_numbers()  # первая область видиммости.
print(r(5))
print(r(10))
print(r(15))
print()
d = average_numbers()  # другая (вторая) область видиммости.
print(d(1))
print(d(10))
print(d(13))


def average_numbers():
    summa = 0
    count = 0

    def inner(number):
        nonlocal summa, count
        # nonlocal count
        summa += number
        count += 1
        return summa / count

    return inner


print('\naverage_numbers():')
k = average_numbers()
print(k(10))
print(k(20))
print(k(30))


def timer():
    start = datetime.now()

    def inner():
        return datetime.now() - start

    return inner


print('\ntimer():')
t = timer()
print(t())
print(t())
print(t())


def timer():
    start = perf_counter()

    def inner():
        return perf_counter() - start

    return inner


print('\ntimer():')
perf = timer()
print(perf())
print(perf())
print(perf())


def add(a, b):
    return a + b


def multiply(a, b, c):
    return a * b * c


def counter(func):
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f'функция {func.__name__} вызывалась {count} раз')
        return func(*args, **kwargs)

    return inner


print(abs.__name__)

print('\ncounter(add):')
q = counter(add)
print(q(10, 20))
print(q(4, 3))

print('\ncounter(multiply):')
m = counter(multiply)
print(m(12, 3, 4))
print(m(4, 3, 2))
