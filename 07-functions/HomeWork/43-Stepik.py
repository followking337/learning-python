n = 5
a = [5, 9, 3, 2, 7]
# n = int(input())
# a = list(map(int, input().split()))
print('\nЗадача 1.1')


def reverse(a):
    if len(a) == 1:
        return a[0]
    print(a[-1], end=' ')
    return reverse(a[:-1])


print(reverse(a))
# reverse(a)

print('\nЗадача 1.2')


def reverse(a):
    if a:
        print(a[-1], end=' ')
        reverse(a[:-1])


reverse(a)
print()

print('\nЗадача 1.3')


def rec(x):
    if x < n:
        rec(x + 1)
        print(a[x], end=' ')


rec(0)
print()

print('\nЗадача 2')


def fibonacci(k):
    if k < 2:
        return k
    return fibonacci(k - 1) + fibonacci(k - 2)


print(fibonacci(7))
print(fibonacci(10))

print('\nЗадача 3')


def list_sum_recursive(a):
    if len(a) == 0:
        return 0
    return a[0] + list_sum_recursive(a[1:])
    # return a[0] + list_sum_recursive(a[1:]) if a else 0


a = [1, 2, 3]
print(list_sum_recursive(a))

print('\nЗадача 4.1')


def flatten(a, b=None):
    if b is None:
        b = []
    for i in a:
        if type(i) == list:
            flatten(i, b)
        else:
            b.append(i)
    return b


print(flatten([1, [2, 3, [4]], 5]))
print(flatten([1, [2, 3], [[2], 5], 6]))
print(flatten([[[[9]]], [1, 2], [[8]]]))

print('\nЗадача 4.2')


def flatten(a):
    if not a:
        return []
    if isinstance(a[0], list):
        return flatten(a[0]) + flatten(a[1:])
    return a[:1] + flatten(a[1:])


print(flatten([1, [2, 3, [4]], 5]))
print(flatten([1, [2, 3], [[2], 5], 6]))
print(flatten([[[[9]]], [1, 2], [[8]]]))
