print('\nКак ввести список с клавиатуры:')

print('\nlist(int):')
a = input().split()
print(a)

print(map(int, a))
print(list(map(int, a)))

print('\nlist(float):')
b = input().split()
print(b)

print(map(float, b))
print(list(map(float, b)))
