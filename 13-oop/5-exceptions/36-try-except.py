"""
TRY EXCEPT
    Обработка исключений

    · После первого исключения в блоке try код ниже не идет в этом блоке, а переходит сразу в блок except

    -Полная форма:
        try:
            {code}
            {code}
            {code}
        except TypeError:  --> может быть несколько except
            {code}
        except (IndexError, KeyError) as alias:
            {code}
        else:              --> выполняется только если в try НЕ было исключений
            {code}
        finally:           --> выполняется всегда (в независимости от исключений и их присутствия/отсутствия)
            {code}

    - Форма try-except:
        try:
            {code}
        except:
            {code}

    - Форма try-finally:
        try:
            {code}
        finally:
            {code}
"""

print('\n\tПример 1')

try:
    # int('hello')
    print('123')
    # 1/0
    a + b
except ValueError:
    print('error ValueError')
except ZeroDivisionError:
    print('error ZeroDivisionError')
except NameError:
    print('error NameError')
else:
    print('good')
finally:
    print('end')

print('-' * 25)

print('\n\tПример 2')

try:
    # 'hello'[6]
    {}['key']
    # print('try')
# except IndexError:
#     print('error IndexError')
# except KeyError:
#     print('error KeyError')
# except LookupError:
#     print('error LookupError')
except (IndexError, KeyError):
    print('error LookupError')
except Exception:
    print('error Exception')
except:  # except BaseException:
    print('error BaseException')
else:
    print('good')
finally:
    print('end')

print('\n\tПример 3')

try:
    # 1/0
    # {}['k']
    [1, 2, 3][15]
except (KeyError, IndexError) as error:
    print('LookupError')
    print(f'Logging error: {error} - {repr(error)}')  # Logging error: 'k' KeyError('k')
except ZeroDivisionError as err:
    print('ZeroDivisionError')
    print(f'Logging error: {err} - {repr(err)}')      # Logging error: division by zero - \
    # ZeroDivisionError('division by zero')
