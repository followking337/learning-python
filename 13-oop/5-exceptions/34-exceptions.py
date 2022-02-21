"""
EXCEPTIONS (Исключения)
    Событие которое выдает сообщение об ошибки при исполнении кода

    · Код выполняется до исключения.
    · Код НЕ выполняется после исключения.
    · Логические ошибки (исключения): не выдают ошибки но работают не верно (не так как предусмотрено).
    · Все исключения --> классы.
    · Родительский класс всех исключений BaseException

"""

# 'hello'[9]  # IndexError: string index out of range
# a + b       # NameError: name 'a' is not defined

print('\n\tValueError:')
try:
    int('hello')  # ValueError: invalid literal for int() with base 10: 'hello'
except ValueError:
    print('Неправильное преобразование')

print('\n\tLookupError and IndexError:')
try:
    [1, 2][5]
except IndexError:
    print('Неправильный индекс')

try:
    {}[5]
except LookupError:
    print('Неправильный индекс')

print('\n\tIndexError:')
t = IndexError()
print(isinstance(t, IndexError))
print(isinstance(t, LookupError))
print(isinstance(t, TypeError))
print(isinstance(t, Exception))

print('\n\traise:')
# raise ValueError
# raise ValueError('Неправильное значение')
