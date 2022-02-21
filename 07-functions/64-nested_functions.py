def colors():
    y = 'yellow'
    # g = 'green'  # приоритет идет локальной области видиммости, затем глобальной (в отсуствие локальной).

    def print_red():
        r = 'red'  # локальная переменная
        print(r, y, g)  # поскольку y нет в функции print_red(), она будет искаться на уровень выше, def colors().

    def print_blue():
        b = 'blue'
        print(b, y, g)
        # print(r)  # NameError: name 'r' is not defined

    # print(r, b)  # NameError: name 'r' is not defined --> r, b локальные переменные функций print_red() и print_blue()
    print_red()
    print_blue()


g = 'gray'  # g будет искаться в глобальном уровне видиммости
colors()
# print_red()  # NameError: name 'print_red' is not defined

print('--------------------------------')


def colors():
    y = 'yellow'
    g = 'green'

    def print_red():
        nonlocal y
        r = 'red'
        print(r, y, g)
        y = 'was changed'

    def print_blue():
        b = 'blue'
        print(b, y, g)

    print_red()
    print_blue()


colors()

print('--------------------------------')


def colors(color='r'):

    def print_red():
        r = 'red'
        print(r)

    def print_blue():
        b = 'blue'
        print(b)

    if color == 'r':
        print_red()
    elif color == 'b':
        print_blue()
    else:
        print('I don´t know this color')


colors()
colors('b')
colors('g')
