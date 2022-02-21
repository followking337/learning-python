print('\n----- DICT COMPREHENSION -----')
# {key: {value} for variable in collection}

print('\nrange:')
a = {i: i ** 2 for i in range(1, 11)}
print(a, type(a))

print('\nrange for:')
b = {}
for i in range(1, 11):
    b[i] = i**2
print(b)

print('\nlist:')
a = {word: len(word) for word in ['hello', 'hi', 'www']}
print(a)

print('\ndict:')
data = {
    'JefF BeZos': '177',
    'IloN MAsk': '126',
    'bernar ArNo': '150',
    'BiLl GAtes': '124'
}
new_data = {key.title(): int(value) for key, value in data.items()}
print(data)
print(new_data)

print('\ndict for:')
new_data2 = {}
for key, value in data.items():
    new_data2[key.title()] = int(value)
print(data)
print(new_data2)

print('\ndict:')
users = [
    [0, 'Bob', 'password'],
    [1, 'code', 'python'],
    [2, 'Stack', 'overflow'],
    [3, 'username', '1234'],
    [51, 'qwerty', '1234']
]
new_users = {i[0]: i[1:] for i in users}
print(new_users)
print(new_users[51])
