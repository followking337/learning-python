print('\n----- if (if else) else -----')
print('\nnumber:')
a = 3
if a % 5 == 0:
    if 9 < a < 100:
        print(1)
        print(2)
    else:
        print(3)
        print(4)
else:
    if a % 2 == 0:
        print(5)
        print(6)
    else:
        print(7)
        print(8)
print('end')

print('\nМеньшее из трех чисел:')
a, b, c = 5, 6, 5
if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)

print('\nКоординаты:')
x, y = 6, -7
if x > 0:  # 1 or 4
    if y > 0:
        print(1)
    else:
        print(4)
else:  # 2 or 3
    if y > 0:
        print(2)
    else:
        print(3)

print('\nОстатки:')
a = 21
if a % 4 == 0:
    print('остаток 0')
else:
    if a % 4 == 1:
        print('остаток 1')
    else:
        if a % 4 == 2:
            print('остаток 2')
        else:
            print('остаток 3')
