"""
Для использования Рекурсии необходимо 2 условия:
    1. Когда есть простое решение (выход из рекурсии).
    2. Может сводится к более мелкой подзадачей, которая в свою очередь сводится к еще более мелкой, в конце концов
        сводится к выходу.
"""
print('\nЗадача №113656.')


def rec(s):
    if 1 <= len(s) <= 2:
        return s
    return s[0] + '(' + rec(s[1:-1]) + ')' + s[-1]


print(rec('pumba'))
print(rec('malina'))

print('\nСтепень числа')


def power(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(x, -n)
    if n % 2 == 0:
        return power(x, n//2) * power(x, n//2)
    if n % 2 == 1:
        return power(x, n-1) * x


print(power(2, 10))
print(power(3, 5))
print(power(5, -2))
print(power(2, -1))
print(power(3, 4))

print('\nПроизвольная вложеность списков')


def rec(a, level=1):
    print(*a, 'level = ', level)
    for i in a:
        if type(i) == list:
            rec(i, level + 1)


a = [1, [3, [4, [3, 4]], [2, 3, [4]]], 2, [2, 3, 4, [3, 4, [2, 3], 5]]]
rec(a)
