"""
all(__iterable) --> True or False
any((__iterable) --> True or False

    all(), any() должны принимать коллекцию - объект состоящий из нескольких объектов.
    all() проверяет, все ли указанные элементы внутри коллекции принимают значение True.
        True когда все элементы коллекции не пустые, все элементы True.
        False когда хотябы один элемент из коллекции пустой, хотябы 1 элемент False.
    any() проверяет, есть ли среди указанных элементов коллекции хотя бы один, принимающий значение True.
        True когда хотябы один элемент из коллекции не пустой, хотябы 1 элемент True.
        False когда все элементы коллекции пустые, все элементы False.
"""
print('\nall():')
a = ['hello', 'hi', 'world']
print(all(a))
a = ['hello', '', 'world']
print(all(a))

print('\nany():')
a = ['hello', 'hi', 'world']
print(any(a))
a = ['hello', '', 'world']
print(any(a))
a = ['hello', '', '']
print(any(a))
a = ['', '', '']
print(any(a))

print('\nall(), any():')
a = [1, 2, 3]
print('all:', all(a))
print('any:', any(a))

a = [1, 0, 3]
print('all:', all(a))
print('any:', any(a))

a = [0, 0, 0]
print('all:', all(a))
print('any:', any(a))

print('\nthree conditions:')
a = 99
condition_1 = a % 2 == 0
condition_2 = a > 50
condition_3 = a < 1000
print('all:', all([condition_1, condition_2, condition_3]))  # чтоб три переменные стали коллекцией, обратили их в list
print('any:', any((condition_1, condition_2, condition_3)))  # чтоб три переменные стали коллекцией, обратили их в tuple
