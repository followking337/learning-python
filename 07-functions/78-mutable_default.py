"""
Использование изменяемых объектов (списков и словарей) в качестве аргументов по умолчанию внутри функции
(лучше не использовать в качестве аргументов по умолчанию).
"""
print('\nmy_list')


def append_to_list(value, my_list):
    my_list.append(value)
    print(my_list)


a = [1, 2, 3]
append_to_list(10, a)
append_to_list(15, a)

print('\nmy_list = []')


def append_to_list(value, my_list=[10, 20]):  # Default argument value is mutable
    my_list.append(value)
    print(my_list, id(my_list))


append_to_list(77)
append_to_list(99)
append_to_list(111)
append_to_list(111, [1, 2, 3])
append_to_list(111, [])

print('\nmy_list = None')


def append_to_list(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    print(my_list, id(my_list))


append_to_list(77)
append_to_list(99)
append_to_list(111)
append_to_list(111, [1, 2, 3])
append_to_list(111, [])

print('\nmy_dict = {}')


def append_to_dict(key, value, my_dict={}):  # Default argument value is mutable
    my_dict[key] = value
    print(my_dict)


append_to_dict(10, 100)
append_to_dict(20, 200)

print('\nmy_dict = None')


def append_to_dict(key, value, my_dict=None):
    if my_dict is None:
        my_dict = {}
    my_dict[key] = value
    print(my_dict)


append_to_dict(10, 100)
append_to_dict(20, 200)
append_to_dict(20, 200, {'a': 111})
