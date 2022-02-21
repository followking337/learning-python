print('\nHomeWork')

print('\nЗадача 1')
s = 'Я стану крутым программистом!'
print(s, s, s, sep='\n')
print('Я стану крутым программистом!\n' * 3)
for i in range(3):
    print(s)

print('\nЗадача 2')
s = 'Hello!'
t = 'Hi!'
# s = input()
# t = input()
print(s, t, sep='\n')
s = s + '\n'
t = t + '\n'
print(s, t, sep='')

print('\nЗадача 3')
s = 'Привет!'
t = 'Артем'
v = 'Как дела?'
# s = input()
# t = input()
# v = input()
print(v, t, s, sep='\n')
print("{2}\n{1}\n{0}".format(s, t, v))

print('\nЗадача 4')
s = 'ХА'
# s = input() + ' '
print(s, s, s, s, sep=' ')
print((s + ' ') * 4, sep=' ')
print('{0} {0} {0} {0}'.format(s))

print('\nЗадача 5')
s = 'Один,два,три'
# s = input()
print(len(s))

print('\nЗадача 6')
s = 'Один'
t = 'Два'
# s = input()
# t = input()
print(t + s)

print('\nЗадача 7')
s = 'Hello'
# s = input()
print(s * 3)

print('\nЗадача 8')
s = 'Лев Николаевич Толстой написал "Война и мир"'
print(s)
