print('\n----- SET COMPREHENSION -----')
# {{code} for variable in collection}

print('\nrange:')
a = {i for i in range(1, 6)}
print(a, type(a))

print('\nlist:')
a = {i for i in [0, 1, 2, 0, 2]}
print(a)
a = {i for i in ['hello', 'hi', 'hello', 'qwerty'] if len(i) > 4}
print(a)

print('\nlist for:')
a = set()
for i in [0, 1, 2, 0, 2]:
    a.add(i)
print(a)

print('\nstr:')
a = {i for i in 'abracadabra'}
print(a)

print('\nnested for:')
a = {i + j for i in 'abc' for j in '123'}
print(a, type(a))
a = [i + j for i in 'abc' for j in '123']
print(a, type(a))
a = {(i, j) for i in 'aaa' for j in '123'}  # [i, j] TypeError: unhashable type: 'list'
print(a, type(a))                           # {i, j} TypeError: unhashable type: 'set'
a = [[i, j] for i in 'aaa' for j in '123']
print(a, type(a))
