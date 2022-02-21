"""
.sort(key, reverse=True/False) - стандартный метод списка, применяется только к спискам, изменяет начальный список.
sorted(__iterable, key, reverse=True/False) - встроенная функция, применяется ко всем итерабельным объектам,
        не изменяет начальную коллекцию.
    Элементы должны иметь возможность быть сравненными между собой, к примеру: либо только числа, либо только строки,
    но числа со строками не могут быть сравнены: c = ('hi', 'zero', 'abracadabra', 'pikachu', 457)
    TypeError: '<' not supported between instances of 'int' and 'str'
"""
a = [4, -10, 43, -3000, 54, 89, -34]
b = 'hello world'
c = ('hi', 'zero', 'abracadabra', 'pikachu')

print('\n.sort():')
a.sort()  # изменяет начальный список.
# a = a.sort()  # None (метод вызова списка делается без присвоения, иначе мы теряем значения).
# b.sort()  # AttributeError: 'str' object has no attribute 'sort'
# c.sort()  # AttributeError: 'tuple' object has no attribute 'sort'
print(a)

print('\nsorted():')
print(sorted(a))
print(sorted(b))  # не изменяет начальную коллекцию: b = 'hello world', превращает в список.
print(sorted(c))  # не изменяет начальную коллекцию, превращает в список.
c = sorted(c)  # чтоб изменить коллекцию требуется присвоить к переменной.
print(c)

print('\nreverse=False:')
# c = sorted(c, key=function, reverse=True/False)
# a.sort(key=function, reverse=True/False)
c = ('hi', 'zero', 'abracadabra', 'pikachu')
c = sorted(c, reverse=False)  # по умолчанию: reverse=False (сортировка по возростанию).
print(c)  # возвращает список несмотря на то что был кортеж.
c = ('hi', 'zero', 'abracadabra', 'pikachu')
c = sorted(c, reverse=True)  # reverse=True (сортировка по убыванию).
print(c)

print('\nkey=function:')  # key принимает функцию, определяет по какому ключу будет производится сортировка.
print(sorted(c, key=lambda i: i[-1]))
print(sorted(c, key=lambda i: i[-1], reverse=True))
