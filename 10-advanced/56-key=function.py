print('\nkey=function:')
a = [4, -10, 43, -300, 54, 289, -34, -8, 749]

print('\n1. Встроенная функция')
print(sorted(a, key=abs))

print('\n2. Собственная функция (сортировка по 1 значению)')
a = [4, 10, 43, 300, 54, 289, 34, 8, 749]


def f(x):
    return x % 10  # return -(x % 10)  сортировка по убыванию


print(sorted(a, key=f))

print('\n2. Собственная функция (сортировка по 2 значениям)')


def f(x):
    return x % 10, x // 10 % 10
    # сперва сортируется по последней цыфре, в случае если они одинаковые, сортируется по второй.


print(sorted(a, key=f))

print('\n3. Методы объектов')
a = ['ZZZ', 'aaa', 'eee', 'DDD', 'BBB', 'www']
print(sorted(a))  # все большие буквы будут впереди всех маленьких.
print(sorted(a, key=str.lower))  # сортируется по буквам алфавита независимо от больших либо маленьких букв.

print('\n4. Анонимные функции lambda (сортировка по 1 значению)')
a = ['ZZZ 79', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 5', 'www 14']
print(sorted(a, key=lambda x: int(x.split()[1])))

print('\n4. Анонимные функции lambda (сортировка по 2 значениям)')
a = ['ZZZ 800', 'aaa 45', 'eee 43', 'DDD 800', 'BBB 43', 'www 14']
print(sorted(a, key=lambda x: (int(x.split()[1]), x.split()[0])))  # по возрастанию по числам, затем по буквам.

a = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'BBB 43', 'www 14']
print(sorted(a, key=lambda x: (-int(x.split()[1]), x.split()[0].lower())))  # по убыванию по числам, затем по буквам.

a = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'AaA 43', 'aaa 14']
print(sorted(a, key=lambda x: (x.split()[0].lower(), int(x.split()[1]))))  # по возрастанию по буквам, затем по числам.

# по убыванию по буквам, затем по возрастанию по числам.
a = ['ZZZ 800', 'aaa 45', 'eee 43', 'ddd 800', 'AaA 43', 'aaa 14']
a = sorted(a, key=lambda x: int(x.split()[1]))  # 1. по возрастанию по числам.
a = sorted(a, key=lambda x: x.split()[0].lower(), reverse=True)  # 2. по убыванию по буквам (приоритет).
print(a)
