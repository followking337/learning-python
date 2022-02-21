print('\nЗадача 1')


def count_args(*args):
    return len(args)


print(count_args(1, 2, 3, 4, 5, 6))

print('\nЗадача 2')


def print_goods(*args):
    j = 0
    for i in args:
        if type(i) == str and len(i) > 0:
            j += 1
            print(f'{j}. {i}')
    if j == 0:
        print('Нет товаров')


print_goods('apple', 'banana', 'orange')
print('----------')
print_goods(1, True, 'Грушечка', '', 'Pineapple')
print('----------')
print_goods([], {}, 1, 2)

print('\nЗадача 3')


def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
    # for key in sorted(kwargs):
        print(f'{key} = {value}')
        # print(f'{key} = {kwargs[key]}')


info_kwargs(first_name="John", last_name="Doe", age=33)
