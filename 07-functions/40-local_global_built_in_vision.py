"""
Область видимости – место, где определяются переменные и где выполняется их поиск (встроенная, локальная и глобальная).
    Правила поиска имен видимости: Local -> Enclosing -> Global -> Built In

    Всякий раз, когда в программе используется некоторое имя, интерпретатор создает, изменяет или отыскивает
    это имя в пространстве имен – в области, где находятся имена.

    Если переменная создается внутри функции, то она будет называться локальной переменной и принадлежать локальной
    области видимости.

    Теже правила переменных работают с областями видимости функций.

    Built In - входят все встроенные функции, объекты и переменные. Полный список: Ctrl + Space

    global {variable} - назначает переменную глобально, Local --> Global
    nonlocal {variable} - назначает переменную объемлимо, Local --> Enclosing
        инструкция допустима только когда есть функция внутри функции.
"""
print('\nexample1():')


def example1():
    # print(w, id(w))  # UnboundLocalError: local variable 'w' referenced before assignment
    a, b, c = 1, 2, 3  # локольные переменные (видны только внутри функции).
    w = 'HELLO'  # если нет локальной переменной, исчет глобальную переменную
    print(a, b, c)
    print(w, id(w))


w, y = 'hello', 100  # глобальные переменные
example1()
print('---------')
print(w, id(w), y)

print('\n#########################')

print('\nexample2():')


def example2():
    a = 11
    b = 22
    # c = 33
    print(a, b, c, 'local')


a = 100
b = 200
c = 300

example2()
print(a, b, c, 'global')

print('\n#########################')

print('\nexample3():')


def example3(a, b, c):
    a = 30
    print(a, b, c, 'local')


a = 100
b = 200
c = 300

example3(a, b, c)
print(a, b, c, 'global')

print('\n#########################')

print('\nexample4():')


def example4(a, b, c):
    a[1] = 100
    print(a, b, c, 'local')


a = [1, 2, 3, 4, 5]
b = 200
c = 300

example4(a, b, c)
print(a, b, c, 'global')

print('\n#########################')

print('\nexample5():')


def example5():
    global a  # назначает переменную глобально
    a = 30
    print(a, 'local')


a = [1, 2, 3, 4, 5]

example5()
print(a, 'global')


def q():  # глобальныя функция
    example5()  # локольная функция


print('\n#########################')

print('\nВстроенная область видимости:')

print('\n#########################')


def z():
    abs = 10  # переназначаем функцию abs() внутри функции локально
    print(abs)


def w(x):
    return x ** 2


z()
abs = w  # переназначаем функцию abs() глобально
print(abs(-7), abs(5))
# False = 54  # SyntaxError: cannot assign to False (нельзя переназначать keywords)
min, max = max, min
a = [1, 100, 34]
print(min(a), max(a))

print('\n#########################')


# def example2():
#     abs = 200  # Enclosing
#     # c = 200  # Enclosing
#
#     def q():
#         # nonlocal abs
#         abs = 'hello'  # Local
#         print(abs, c, 'q()')  # c нет в Local, переходит искать в Enclosing
#     q()
#     print(abs, c, 'example2()')
#
#
# abs = [1, 2, 3]  # Global
# c = 333  # Global
# example2()


def a():
    global x
    abs = 'Enclosing'
    x = 'Enclosing'

    def b():
        nonlocal abs
        abs = 'Local'
        print(abs, x, 'b()')
    b()

    print(abs, x, 'a()')


abs = 'Global'
x = 'Global'
a()
print(abs, x, 'Global')
