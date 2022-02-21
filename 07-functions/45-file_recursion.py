import os

print('\npath:')
path = '/Users/dani/Documents/Learning Python/Basic/7-functions/Movies'
url1 = os.path.abspath('./')
url2 = os.path.abspath('../')
print(path)
print(url1)
print(url2)

print('\npath list:')
print(os.listdir(path))

print('\npath for:')
for i in os.listdir(path):
    print(i, type(i), path + '/' + i, os.path.isfile(path + '/' + i))

print('\nfile_recursion():')


def file_recursion(path, level=1):
    print('level:', level, 'content:', os.listdir(path))
    for i in os.listdir(path):
        if os.path.isdir(path + '/' + i):
            print('Спускаемся в', path + '/' + i)
            file_recursion(path + '/' + i, level+1)
            print('Возвращаемся в', path)


file_recursion(path)

print('\nHomeWork')
print('\nfile_recursion2():')


def file_recursion2(path, name, level=1):
    for i in os.listdir(path):
        if i == name:
            print(path + '/' + i, 'level:', level)
        if os.path.isdir(path + '/' + i):
            file_recursion2(path + '/' + i, name, level+1)


file_recursion2(path, name='hello.rtf')
file_recursion2(path, name='актреры.rtf')
file_recursion2(path, name='Travolta.jpg')
file_recursion2(path, name='DiCaprio.jpg')
file_recursion2(path, name='actor2.rtf')
