print('\nstr:')

print('\nОперации:')
print('''hello
world
456''')
print('hello\nworld\n456')
s = 'hello'
print(s)
d = ' '
e = ''
print(d, e)
r = 'world'
print(s, r)
x = 'a'
print(x * 5)
print(s * 3)
# print(s * 2.5) error
# print('abc' + 23) error
print('abc' + str(23))

print('\nlen():')
print(len('abc'))
print(len(''))
print(len(' '))
print(len(s))
q = 'qwerty'
print('Вы ввели', len(q), 'символов')

print('\nKeyword: in')
w = '!@#$4567'
print('4' in w)
print('45' in w)
print('54' in w)

print('\nСравнение строк:')
print('aaa' == 'aaa')
print('AAA' == 'aaa')
print('abc' > 'r')

print('\nascii code table')
print(ord('a'))
print(ord('b'))
print(ord('c'))
print(ord('r'))
print(ord('A'))
print('WELORGFWS' < 'kefnksfng')
print('abc' < 'abcd')
print('input' == 'input ')
