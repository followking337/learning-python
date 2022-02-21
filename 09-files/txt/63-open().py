"""
file = open(file, mode, encoding)
    Аргументы:
    1. Имя файла (обязательный параметр) или путь к файлу (относительный или абсолютный).
        Если файл находится в корне модуля, указывать путь не нужно.
    2. Режим "r" (по умолчанию), "w", "a", "a+", в котором открывается файл.
        'w' и 'a' невозможно одновременно и записывать и считывать.
            'w' перезаписывает весь файл.
            'a' дописывает в конец файла.
        'a+' считывает и дописывает.
    3. Encoding отвечает за кодировку файла (необязательный параметр).
        Для возможности работы с кириллицей необходимо поставить encoding в значение utf-8.

    open()
        {обработка}
        <ошибки>  --> в случае ошибок файл не закроется, рекомендация: 1. try - except 2. manager контекстов
    close() --> файл нужно закрывать после его обработки, таким образом память переменной освобождается.
"""
file = open('111.txt')
# file = open(r'/Volumes/GoogleDrive/Mi unidad/Aprendizaje/Data Scientist/Egoroff/Main/9. files/111.txt')
# file = open('111.txt', 'r', encoding='utf-8')  # работает без utf-8.

print('\nЧтение файла --> mode: "r"')

print('\n.read():')
# print(file.read())  # считывает файл целеком
print(file.read(3))   # считывает число символов заданные в параметре
print(file.read(3))   # запоминает на каком символе остановился предедущий .read(n)
print(file.read(4))

print('\n.seek():')
file.seek(0)  # откатывает .read(n) в начало
print(file.read(3))

print('\n.readline():')
file.seek(0)
print(file.readline(), end='')  # после вывода линии, запоминает на какой линии остановился
print(file.readline(), end='')

print('\nfor --> lines:')
file.seek(0)
for i in file:  # i --> line of file
    print(i, end='')

print('\n\nnested for --> letters:')
file.seek(0)
for row in file:
    for letter in row:
        print(letter, end='/')

print('\n\n.readlines():')
file.seek(0)
s = file.readlines()  # метод создает список с элементами строк файла
print(s)
file.close()

print('\nЗапись файла --> mode: "w"')
file = open('222.txt', 'w', encoding='utf-8')
# print(file.read())  # io.UnsupportedOperation: not readable
print('.write():')
file.write('hello from mode "w" 1\n')
file.write('hello from mode "w" 2\n')
file.write('hello from mode "w" 3\n')
file.close()

print('\nДопись файла --> mode: "a"')
file = open('222.txt', 'a', encoding='utf-8')
# print(file.read())  # io.UnsupportedOperation: not readable
file.write('goodbye from mode "a"\n')
file.close()

print('\nДопись и чтение файла --> mode: "a+"')
file = open('222.txt', 'a+', encoding='utf-8')
file.write('goodbye from mode "a+"')
file.seek(0)
print(file.read())
file.close()
