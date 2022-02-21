class MyException(Exception):
    """this is my first Exception"""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        print('__str__ called')
        if self.message:
            return f'MyException {self.message}'
        else:
            return 'MyException is empty'


# raise MyException                      # __main__.MyException
# raise MyException('MyError')           # __main__.MyException: MyError
# raise MyException('MyError', 1, 2, 3)  # __main__.MyException: ('MyError', 1, 2, 3)

try:
    raise MyException
except MyException:
# except Exception:
# except AttributeError:
    # исключение AttributeError не проскакивает поскольку оно на одном уровне иерархии с MyException
    print('done')

# raise MyException                      # __main__.MyException: MyException is empty
# raise MyException('MyError', 1, 2, 3)  # __main__.MyException: MyException MyError

print('\n\tСвоя Созданная Иерархия:')


class SnakeExceptionBase(Exception):
    """Основной класс ошибок змейки"""


class SnakeBorderException(SnakeExceptionBase):
    """Ошибка соприкосновения змеи со стенкой"""


class SnakeTailException(SnakeBorderException):
    """Соприкосновение змейки с ее телом"""
