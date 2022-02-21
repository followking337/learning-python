print('\nЭкранированые Служебные символы:')
s = '''hello
world
hi
bye'''
print(s)

print('\n\\n:')
a = 'abc\ndef'
print(a)
print(len(a))

print('\n\\t:')
print('abc\tdef')

print('\nOther Symbols:')
print('abc\"def')
print('abc\
def')
# print('abc\')  SyntaxError: EOL while scanning string literal (строку нельзя закончить \)
print('abc\'')

print('\nФайлы:')
r = '/Users/dani/Google Drive/Aprendizaje/Programacion/Python'
r = r.replace('/', '\\')
print(r)
print('\nUsers\dani\tGoogle Drive\Aprendizaje\Programacion\Python')

print('\nr\':')  # r' убирает все служебные символы в строке
print(r'\nUsers\dani\tGoogle Drive\Aprendizaje\Programacion\Python')
print('abc\nre\tgfd\ngfd')
print(r'abc\nre\tgfd\ngfd')
print(len('abc\nre'))
print(len(r'abc\nre'))
