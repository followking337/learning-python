from string import ascii_lowercase

print('\nЗадача 1')
n = 20
# n = int(input())
d = {}
for i in range(1, n + 1):
    d[i] = i * i
print(d)
d = {i: i * i for i in range(1, n + 1)}
print(d)

print('\nЗадача 2')
print(ascii_lowercase)
alphabet = {}
count = 1
for i in ascii_lowercase:
    alphabet[i] = count
    count += 1
# alphabet = {i: count for i in ascii_lowercase}
for key, value in alphabet.items():
    print(key, value)

print('\nЗадача 3')
d1 = {'a': 100, 'b': 200, 'c': 333}
d2 = {'x': 300, 'y': 200, 'z': 777}
# rez = d1 + d2  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
rez = {}
for i in d1:
    rez[i] = d1[i]
for i in d2:
    rez[i] = d2[i]
print(rez)

rez = {}
rez = {**d1, **d2}
print(rez)

rez = {}
rez = d1
for key, value in d2.items():
    rez[key] = value
print(rez)

rez = {}
d1.update(d2)  # rez.update(d1)
rez = d1  # rez.update(d2)
print(rez)

print('\nC. Система регистрации (1)')
# n = int(input())
# register = {}
# for i in range(n):
#     name = input()
#     if name not in register:
#         print('OK')
#         register[name] = 1
#     elif name in register:
#         print(name + str(register[name]))
#         # print(f'{name}{register[name]}')
#         register[name] += 1

print('\nC. Система регистрации (2)')
# d = {}
# for _ in range(int(input())):
#     s = input()
#     z = d.get(s, 0)
#     print(f'{s}{z}' if z else 'OK')
#     d[s] = z + 1
