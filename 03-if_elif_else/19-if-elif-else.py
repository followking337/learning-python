print('\n----- if elif else -----')

print('\nif is correct:')
if 5 > 1:
    print(1)
    print(2)
elif 3 > 2:
    print(3)
    print(4)
elif 6 > 4:
    print(5)
    print(6)
elif 6 > 4:
    print(7)
    print(8)

print('\nelif 1 is correct:')
if 5 > 5:
    print(1)
    print(2)
elif 3 > 2:
    print(3)
    print(4)
elif 6 > 4:
    print(5)
    print(6)
elif 6 > 4:
    print(7)
    print(8)

print('\nelif 3 is correct:')
if 5 > 5:
    print(1)
    print(2)
elif 3 > 6:
    print(3)
    print(4)
elif 6 < 4:
    print(5)
    print(6)
elif 6 > 4:
    print(7)
    print(8)

print('\nelse is correct:')
if 5 > 5:
    print(1)
    print(2)
elif 3 > 6:
    print(3)
    print(4)
elif 6 < 4:
    print(5)
    print(6)
elif 5 > 7:
    print(7)
    print(8)
else:
    print(9)
    print(10)

print('\nДорога:')
road = 5
if road == 1:
    print('Дорога 1')
elif road == 2:
    print('Дорога 2')
elif road == 3:
    print('Дорога 3')
else:
    print('error')

print('\nWeek:')
day = 7
if day == 1:
    print('Monday')
elif day == 2:
    print('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
elif day == 7:
    print('Sunday')
else:
    print('error')

print('\nNumber 1:')
a = 456
if a < 0 or a > 10000:
    print('error')
elif a < 10:
    print('1 digit')
elif a < 100:
    print('2 digits')
elif a < 1000:
    print('3 digits')
elif a < 10000:
    print('4 digits')

print('\nNumber 2:')
a = 9
if a < 0 or a > 10000:
    print('error')
elif a < 10:
    if a % 2 == 0:
        print('1 digit и четное')
    else:
        print('1 digit и не четное')
elif a < 100:
    print('2 digits')
elif a < 1000:
    print('3 digits')
elif a < 10000:
    print('4 digits')
