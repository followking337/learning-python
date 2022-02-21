print('\nЗадача №113655.')


def string(s):
    if len(s) == 1:
        return s
    if len(s) == 2:
        return s[0] + '*' + s[1]
    return s[0] + '*' + string(s[1:-1]) + '*' + s[-1]


# print(string(input()))
print(len('LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO'))
print(string('LItBeoFLcSGBOFQxMHoIuDDWcqcVgkcRoAeocXO'))

print('\nНумеролог')


def shazam(s, count=0):
    if len(s) == 1:
        print(s, count)
    else:
        accumulative = 0
        for i in s:
            accumulative += int(i)
        return shazam(str(accumulative), count + 1)  # se puede omitir return


shazam('1')
shazam('10')
shazam('99')

"""
Задачи данного блока можно решить с помощью циклов, однако, рекомендуем попробовать решить их с помощью рекурсивных
функций, для тренировки. Известно, что любой цикл можно заменить рекурсией.
"""
print('\nЗадача №113657. (1)')


def mirror(s, t=''):
    if len(s) == 1:
        if s == '(':
            return ')'
        return s
    else:
        if s[-1] == '(':
            t += ')' + mirror(s[:-1])
        t += s[-1] + mirror(s[:-1])
    return t


# s = input()
# print(s[:-1] + mirror(s))
print(mirror('(abc(def(g'))

print('\nЗадача №113657. (2)')


def mirror(s, t=''):
    if len(s) == 1:
        return s
    t += s[0] + mirror(s[1:], t)
    return t


print(mirror('(abc(def(g'))

print('\nЗадача №89. Разбиение на невозрастающие слагаемые, лексикографический порядок')


# def numbers(n, i=1):
#     if i == n:
#         return n
#     return numbers(n, i) + numbers(n, i)
#
#
# print(numbers(5))
