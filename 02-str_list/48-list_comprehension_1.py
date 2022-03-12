"""
LIST COMPREHENSION
    [code for variable in collection]                                -> list
    [code for variable in collection if condition]                   -> list (with condition)
    [code if condition else code for variable in collection]         -> list (with multiple conditions)
    [code for variable1 in collection1 for variable2 in collection1] -> list (nested for)
    [[code for variable in collection] for variable in collection]   -> lists in list (nested array)
"""

import random

# [code for variable in collection]
print('\nrange():')
print([0 for i in range(7)])
print([2 for j in range(6)])
print([i for i in range(10)])
print([i for i in range(1, 11)])
print([i ** 2 for i in range(10)])
print([i % 4 for i in range(1, 15)])

print('\nstr:')
print([i for i in 'hello'])
print([i * 5 for i in 'hello'])
print([ord(i) for i in 'abcde'])

print('\nrandint():')
a = [random.randint(-10, 10) for i in range(10)]
print(a)
b = [abs(i) for i in a]
print(b)
a = [i + 1 for i in a]  # изменяет начальный список
print(a)

print('\nif:')
# [code for variable in collection if condition]
print([i for i in a if i % 2 == 0])
print([i for i in a if i % 2 == 0 and i % 3 == 0])

print('\nif else:')
# [code if condition else code for variable in collection]
a = [1, 2, -3, 4, -5, -6]
print([i + 10 for i in a if i > 0])
print([i + 10 if i > 0 else i * 10 for i in a])

print('\ninput():')
# print([int(i) for i in input().split()])

print('\nnested array:')
n, m = 5, 4
a = [[0] * m for i in range(n)]
a[2][1] = 1
for i in a:
    print(i)

# [code for variable1 in collection1 for variable2 in collection1]
print('\nnested for:')
a = [(i, j) for i in 'abc' for j in [1, 2, 3]]
print(a)

a = [i * j for i in [2, 3, 4, 5] for j in [1, 2, 3] if i * j >= 10]
print(a)
