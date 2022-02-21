"""
DOUBLE UNDERSCORE (dunder) METHODS
    Магические Методы
    __method__ --> методы внутри класса
        · Вызываются (срабатывают):
            1. автоматически в определенный момент времени.
            2. вручную через [instance].__method__()

        __call__ --> делает экземпляры вызываемыми:
            - instance()
            - [instance].__call__()

            · при помощи метода __call__ создаем:
                1. Экземпляр вызываемый
                2. Замыкание
                3. Декоратор

"""
from time import perf_counter


class Counter:

    def __init__(self):
        print('init object', self)

    def __call__(self, *args, **kwargs):
        print('call object', self)


print('\n\t1. Экземпляр вызываемый:')
a = Counter()
a()
a.__call__()


class Counter:

    def __init__(self):
        self.counter = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f'наш экземпляр вызывался {self.counter} раз')


print('\n\t2.1 Замыкание:')
b = Counter()
b()
b()
b()


class Counter:

    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'наш экземпляр вызывался {self.counter} раз')

    def average(self):
        return self.summa / self.length


print('\n\t2.2 Замыкание:')
c = Counter()
print(c.counter, c.summa, c.length)
c(3, 4, 5)
print(c.counter, c.summa, c.length)
c(1, 2)
print(c.counter, c.summa, c.length)
print(c.average())


class Timer:

    def __init__(self, func):
        self.fn = func

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        print(f'Вызывается функция {self.fn.__name__}')
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Функция отработала за {finish - start}')
        return result


@Timer  # fact = Timer(fact)
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


# @Timer  # fib = Timer(fib)
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print('\n\t3.1 Декоратор:')
print(fact(7))

print('\n\t3.2 Декоратор:')
a = Timer(fib)(7)
print(a)
print(fib(7))
b = Timer(fib)(20)
print(b)
