print('\nlist:')

print('\nОперации:')
marks = [4, 5, 3, 4, 5]
june_temper = [20, 24, 30, 43, 12, 23]
a = [True, 43, 'hello', 5.4, [4, 5, 6]]
b = []
print(type(b))

print('\nlen():')
print(len([1, 2, 3]))
print(len(a))
print(len(b))

print('\nСложение:')
print([12, 23] + [1, 2, 3])
print(a + [4])  # a = a + 4 TypeError: can only concatenate list (not "int") to list
print(['hi'] + a)
print([0] * 5)
print([1, 2, 3] * 5)  # print([1, 2, 3] * 5.4) TypeError: can't multiply sequence by non-int of type 'float'

print('\nKeyword: in')
print(5.4 in a)
print(False in a)
print([4, 5, 6] in a)
print([4, 5] in a)

print('\nsum(), max(), min():')
w = [43, 54, 65, 3, 4, 65, -43, 22]
print(max(w))
print(min(w))
print(sum(w))
print(sum([1, 2, 3, 4]))
# print(sum([1, 2, 3, 'segr'])) TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(max([1, 2, 3, 'segr'])) TypeError: '>' not supported between instances of 'str' and 'int'

print('\nsorted():')
print(sorted(w))
print(sorted(w, reverse=True))

print('\nСравнение:')
print([100, 54] > [34, 543, 654, 43])  # Сравнивает по первому элементу.
print([1, 2, 3] == [1, 2, 3])
print([1, 2, 3] == [1, 2, 'wegm'])
# print([1, 2, 3] > [1, 2, 'wegm']) TypeError: '>' not supported between instances of 'int' and 'str'
print(sum(marks)/len(marks))
