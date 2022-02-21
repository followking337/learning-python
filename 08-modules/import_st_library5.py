def say_hello(name):
    print(f'Hello, {name}')


def summa(*args):
    return sum(args)


def factorial(n):
    print('my func')
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


my_str = 'YO ARE BREATHTAKING'
my_num1 = 2
my_num2 = 3

if __name__ == '__main__':  # конструкция позволяет не запускать код в случае импорта.
    print(123)              # код запускается только когда запускается сам этот модуль.
    print('hello')
