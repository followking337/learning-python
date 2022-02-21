"""
PROPAGATION EXCEPTIONS
    Через stack вызов
"""
# error --> (third() обработана) --> second() --> first()


def third():
    print('start third')
    try:
        1/0
    except ZeroDivisionError:
        print('handling')
    print('finish third')


def second():
    print('start second')
    third()  # stack
    print('finish second')


def first():
    print('start first')
    second()  # stack
    print('finish first')


first()

print('-' * 20)

# error --> third() --> second() --> (first() обработана)


def third():
    print('start third')
    1/0
    print('finish third')


def second():
    print('start second')
    third()  # stack
    print('finish second')


def first():
    print('start first')
    try:
        second()  # stack
    except ZeroDivisionError:
        print('handling')
    print('finish first')


first()
