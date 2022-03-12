print('\nКак ввести список с клавиатуры:')

print('\nlist(int):')
a = input().split()
print(a)                    # -> list

print(map(int, a))          # -> map object
print(list(map(int, a)))    # -> list

print('\nlist(float):')
b = input().split()
print(b)                    # -> list

print(map(float, b))        # -> map object
print(list(map(float, b)))  # -> list
