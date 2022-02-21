print('\nstr:')

print('\nМетоды:')
# Методы - это функция, связанная с определенным типом объекта. То есть методы являются специфичными функциями
# для каждого отдельного типа. Вызов метода: объект.метод(аргумент).

print('\n.upper()')
s = 'Hello World'
print(s.upper())  # выводит результат но не меняет строку, поскольку str являются не изменяемыми объектами.
s = s.upper()  # сохраняет результат в переменную, обновляя её

print('\n.lower()')
print(s.lower())  # выводит результат но не меняет строку, поскольку str являются не изменяемыми объектами.
s = s.lower()  # сохраняет результат в переменную, обновляя её

print('\n.count()')
print(s.count('o'))  # требует как минимум один аргумент
print(s.count('o', 6))
print(s.count('o', 8))
print(s.count('l', 1, 3))
print(s.count('l', 1, 4))

print('\n.find()')
print(s.find('e'))
print(s.find('wor'))
print(s.find('z'))  # не существует такого значения, результат -1
print(s.find('o'))
print(s.rfind('o'))
print(s.find('o', 6))
print(s.find('o', 5))

print('\n.index()')
print(s.index('o'))
# print(s.index('z'))  ValueError: substring not found

print('\n.replace()')
print(s.replace('o', '???'))
print(s.replace('l', ' '))
print(s.replace('l', ''))
print(s.replace(' ', ''))
print(s.replace('l', '', 2))

print('\nМетоды которые проверяют из каких символов состоит строка:')
print(s.isalpha())  # состоит ли строка целиком из букв? нет, есть пробел
print('elkgnmeklALFKNEMNSEglemf'.isalpha())  # данная строка состоит целиком из букв
print('16548946'.isdigit())  # состоит ли строка целиком из цыфр? да
print('1654 894 6'.isdigit())  # состоит ли строка целиком из цыфр? нет, присутствуют пробелы
print(int('432'))
# print(int('43 2'))  # ValueError: invalid literal for int()

print('\n.rjust() and .ljust()')
d = '111'
print(d.rjust(10, '0'))
print(d.ljust(10, '0'))
print(d.ljust(10, '-'))
# print(d.rjust(10, '--'))  # TypeError: The fill character must be exactly one character long

print('\n.split()')  # при помощи метода split мы можем из строки получить список
w = 'Ivanov Ivan Ivanovich'
print(w.split())  # w.split(' ')
print(w.split('n'))
print('16516,616468,3154894'.split(','))

print('\n.join()')  # при помощи метода join мы может из списка получить строку
a = ['16516', '616468', '3154894']
print('='.join(a))
print('hello'.join(a))
b = [16516, 616468, 3154894]  # используется только с списками которые состоят из строк
# print('='.join(b))  # TypeError: sequence item 0: expected str instance, int found
# сперва нужно приобразовать элементы списка b в строки через генератор списков или через фунцию map
print('#'.join([str(i) for i in b]))
print(', '.join(w.split()))

print('\n.strip')
q = '     hello      \n'
print(q)
print(q.strip())  # метод удаляет знаки пробелов и знаки переноса на новую строку как слева так и справа
print(q.rstrip())  # метод удаляет знаки пробелов и знаки переноса на новую строку справа
print(q.lstrip())  # метод удаляет знаки пробелов и знаки переноса на новую строку слева

print('\nВыводить методы цепочкой:')
# s = input().upper()
print(s)
print(s.lower().replace('e', 'w').upper())
