print('\nStepik HomeWork')

print('\nЗадача 1')
s = 'ManY mUcH'
# s = input()
print(s.upper())

print('\nЗадача 2')
s = 'TheRe is NO spOOn'
# s = input()
print(s.lower())

print('\nЗадача 3')
s = 'Helen'
# s = input()
print(s.lower().count('e'))

print('\nЗадача 4')
s = "what's up?"
# s = input()
print(s.replace('w', '').replace('z', ''))

print('\nЗадача 5')
s = "dog"
# s = input()
print(s.find('a'))

print('\nЗадача 6')
s = "banana"
# s = input()
print(s.rfind('a'))

print('\nЗадача 7')
s = "Hello my friend"
# s = input()
print(len(s.split()))

print('\nЗадача 8')
s = "Smells Like Teen Spirit"
# s = input()
print(s.replace(' ', ','))

print('\nЗадача 9')
s = "Codeforces"
# s = input()
print(s.lower().replace('a', '').replace('e', '').replace('o', '').replace('u', '').replace('i', '').replace('y', '').
      replace('', '.')[:-1])

for i in 'aeouiy':
    s = s.replace(i, '')
s = '.'.join(s)
print('.' + s)
