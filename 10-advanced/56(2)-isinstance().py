"""
isinstance(__obj, __class_or_tuple)  --> True or False

    Позволяет проверить к какому типу объекта принадлежит значение.
"""
print('\nisinstance():')
a = [5, 3, 'hello', [3, 4], ' world', [5], 10.5]

s_str = ''
s_list = []
s_numbers = 0

for i in a:
    if isinstance(i, str):
        s_str += i
    elif isinstance(i, list):
        s_list += i
    elif isinstance(i, (int, float)):  # elif isinstance(i, int) or isinstance(i, float):
        s_numbers += i

print(s_str)
print(s_list)
print(s_numbers)
