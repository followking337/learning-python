import random

print('\nlist:')
a = [
    ('Sidorov', 1995),
    ('Lukov', 2002),
    ('Petrov', 1991),
    ('Gorbachev', 1984),
    ('Kostin', 2000),
    ('Isaev', 2005),
    ('Eliseev', 1999),
    ('Kozlov', 2004),
    ('Bukov', 1995),
    ('Gavrilov', 1980),
    ('Efremov', 2006)
]
print([i[0] for i in a])
print([i[1] for i in a])
print([i[0] for i in a if i[0].startswith(('E', 'K'))])
print([i[0] for i in a if i[1] > 2000])
print([i[0][0] for i in a if i[1] > 2000])

print('\ndict:')
b = {
    'Sidorov': {'age': 1995, 'hobby': 'soccer', 'car': 'BMW'},
    'Lukov': {'age': 2002, 'hobby': 'basketball', 'car': 'Opel'},
    'Petrov': {'age': 1991, 'hobby': 'chess', 'car': 'BMW'},
    'Gorbachev': {'age': 1984, 'hobby': 'tennis', 'car': 'BMW'},
    'Kostin': {'age': 2000, 'hobby': 'swimming', 'car': 'Audi'},
    'Isaev': {'age': 2005, 'hobby': 'music', 'car': 'BMW'},
    'Eliseev': {'age': 1999, 'hobby': 'chess', 'car': 'Audi'},
    'Kozlov': {'age': 2004, 'hobby': 'soccer', 'car': 'Opel'},
    'Bukov': {'age': 1995, 'hobby': 'basketball', 'car': 'Audi'},
}
print([i for i in b])
print([b[i]['car'] for i in b])
print([b[i]['hobby'] for i in b])
print([b[i]['car'] for i in b if b[i]['age'] < 2000])
print([(i, b[i]['car']) for i in b if b[i]['age'] < 2000])
print([(i, b[i]['car']) for i in b if b[i]['age'] < 2000 and b[i]['hobby'] == 'soccer'])

print('\nstr:')
s = 'eorijdjgt348u590384jgj3849'
print([i for i in s if i.isdigit()])
print([int(i) for i in s if i.isdigit()])
print([i for i in s if i.isalpha()])

print('\nnested list coprehension for nested array:')
n, m = 5, 5
a = [[random.randint(1, 6) for j in range(m)] for i in range(n)]
# для каждого значения i формируется внутренний генератор повторяющийся m раз где формируются random числа от 1 до 6.
for i in a:
    print(i)

b = [a[i][j] for i in range(n) for j in range(m) if i == j]
print('diagonal:', b)

c = [a[2][j] for j in range(m)]
print('2 row:', c)

d = [a[i][3] for i in range(n)]
print('3 column:', d)

print('\nmultiplication table:')
n, m = 7, 7
a = [[i * j for j in range(1, m+1)] for i in range(1, n+1)]  # result: nested array

# printing table
for i in a:
    for j in i:
        print(str(j).rjust(2, ' ') if 0 < j < 10 else str(j), end=' ')
    print()
