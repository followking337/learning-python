print('\nStepik and Egoroff HomeWork')

print('\nЗадача 1')
s = 'Zemfira'
# s = input()
print(s[0])

print('\nЗадача 2')
s = 'Billie Eilish'
# s = input()
print(s[-1])
print(s[len(s)-1])

print('\nЗадача 3')
s = 'Макгрегор'
# s = input()
print(s[:4])

print('\nЗадача 4')
s = 'Манчестер сити'
# s = input()
print(s[-4:])

print('\nЗадача 5')
s = 'Монти Пайтон'
# s = input()
print(s[::2])

print('\nЗадача 6')
s = 'Donald Trump'
# s = input()
print(s[1::2])

print('\nЗадача 7')
s = 'leetcode.com'
# s = input()
print(s[::-1])

print('\nЗадача 8')
s = 'The Big Bang Theory'
# s = input()
print(s[::-3])

print('\nЗадача 9')
s = 'become'
# s = input()
print(s[-1] + s[:-1])

print('\nЗадача №3735. Делаем срезы')
s = 'Abrakadabra'
# s = input()
print(s[2])
print(s[-2])
print(s[:5])
print(s[:-2])
print(s[::2])
print(s[1::2])
print(s[::-1])
print(s[::-2])
print(len(s))

print('\nНайти сумму первой и последней цифр:')
s = '10265'
# s = input()
print(int(s[0]) + int(s[-1]))

print('\nЗадача №3737. Две половинки')
s = 'Hello'
# s = input()
s = s[int(len(s) / 2) + (len(s) % 2 == 1):] + s[:int(len(s) / 2) + (len(s) % 2 == 1)]
print(s)
