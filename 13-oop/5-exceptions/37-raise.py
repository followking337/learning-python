"""
RAISE
    Инструкция возбуждает исключения указывая тип исключения

        1. Встроенные исключения (наследники BaseException).
            - raise Exception
            - raise Exception('Message')
            - raise Exception(*args)

        2. Экземпляры исключений.
            instance = Exception()
            instance = Exception('Message')
            instance = Exception(*args)
            - raise instance

        3. Custom исключения.
            class MyException(Exception):
                {code}
            - raise MyException
            - raise MyException('Message')
            - raise MyException(*args)

    · Нельзя вызывать исключения от классов которые не являются BaseException
    · Custom исключения наследовать от Exception

    · raise в форме try-except:
        try:
            {code}                      --> error
        except (Exception1, Exception2) as alias:
            raise                       --> Exception
            raise alias                 --> 2 линии ошибок
            raise Exception3            --> 2 линии ошибок
            raise Exception3 from None  --> 1 линия ошибок (последняя ошибка)
            raise Exception3 from alias --> 2 линии ошибок
"""

# raise Exception                          # Exception
# raise Exception('Big ERROR')             # Exception: Big ERROR
# raise Exception('Big ERROR', 1, 2, 3)    # Exception: ('Big ERROR', 1, 2, 3)

# a = TypeError()
# raise a          # TypeError

# err = TypeError('Big ERROR')
# print(err)       # Big ERROR
# print(err.args)  # ('Big ERROR',)
# raise err        # TypeError: Big ERROR

# b = TypeError(1, 2, 3)
# print(b)         # (1, 2, 3)
# print(b.args)    # (1, 2, 3)
# raise b          # TypeError: (1, 2, 3)

try:
    [1, 2, 3][15]
except (KeyError, IndexError) as error:
    print(f'Logging error: {repr(error)}')
    # raise                                         # IndexError: list index out of range
    # raise error                                   # 2 линии ошибок
    # raise TypeError('Ошибка Типа')                # 2 линии ошибок
    # raise TypeError('Ошибка Типа') from None      # 1 линия ошибок (последняя ошибка)
    # raise TypeError('Ошибка Типа') from error     # 2 линии ошибок

try:
    raise ValueError('Ошибка Значения')
except ValueError as first:
    try:
        raise TypeError('Ошибка Типа')
    except TypeError as second:
        # raise Exception('Big ERROR')              # 3 линии ошибок
        # raise Exception('Big ERROR') from None    # 1 линия ошибок (последняя ошибка)
        # raise Exception('Big ERROR') from second  # 3 линии ошибок
        # raise Exception('Big ERROR') from first   # 2 линии ошибок
        print('end')
