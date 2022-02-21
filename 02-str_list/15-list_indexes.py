print('\nlist:')

a = [43, 54, 2, 54, 32]
b = [3, 4, 5, 6, 7, 8, 9, 10, 11]

print('\nИндексы:')
print(a[0])
print(a[4])
# print(a[7])  IndexError: list index out of range
print(a[-1])
print(a[-2])
print(b[-1])

print('\nСрезы:')
print(b[1:4])
print(b[1:5])
print(b[2:-1])
print(b[2:999])
print(b[2:])
print(b[:2])
print(b[:])

print('\nСрезы с третим параметром:')
print(b[::2])
print(b[1::2])
print(b[3:7:3])
print(b[3:6:3])
print(b[::-1])
print(b[::-2])

print('\nИзменять элементы:')  # list является изменяемым объектом.
b[2] = 100
print(b)
b[3:4] = 34, 23
print(b)
b[2:5] = 47, 33
print(b)

print('\nУдалять элементы:')
del b[2]
print(b)

print('\nОсобенность списков:')  # Две переменные ссылаются на один и тотже объект.
a = [1, 2, 3]
b = a
print(a, b)
b[1] = 100
print(a, b)

print('\nДублируем список:')  # Две переменные ссылаются на два разных объекта (один точная копия другого).
a = [1, 2, 3]
b = a[:]
print(a, b)
b[1] = 100
print(a, b)
