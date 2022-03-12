print('\nMethods:')
a = [12, 43, 54, 65, 76, 3]

print('\n.append():')
a.append(46)       # ничего не выводит (None) но меняет список, поскольку list являются изменяемыми объектами.
print(a)           # выводит ранее измененный список.
a = a.append(46)   # присвоение результата метода который ничего не выводит (None).
print(a)           # при присвоении были потеряны все значения списка
a = [12, 43, 54, 65, 76, 3]
print(a)
a.append('hello')  # метод может добавлять только одно значение.
a.append([1, 2, 3])
print(a)
# a.append(1, 2)  TypeError: list.append() takes exactly one argument (2 given)

print('\n.clear():')
a.clear()
print(a)

print('\n.copy():')
a = [12, 43, 54, 65, 76, 3]
b = a.copy()  # b = a[:]
print(a)
print(b)

print('\n.count():')
print(a)
print(a.count(12))
a.append(12)
print(a.count(12))
print(a.count(32))  # числа которого нет в списке

print('\n.index():')
print(a)
print(a.index(54))
print(a.index(12))
print(a.index(12, 3))
# print(a.index(12, 3, 5))  ValueError: 12 is not in list
print(12 in a[3:5])

print('\n.insert():')
print(b)
b.insert(2, 100)
print(b)
b.insert(0, 100)
print(b)
# b.insert(0, 100, 200)  TypeError: insert expected 2 arguments, got 3

print('\n.pop():')
print(b)
print(b.pop())  # выводит удаленный элемент.
print(b)
print(b.pop(3))
print(b)

print('\n.remove():')  # удаляет по значению
print(b)
b.remove(100)  # ничего не выводит (None) но меняет список, поскольку list являются изменяемыми объектами.
print(b)
# b.remove(100)  ValueError: list.remove(x): x not in list
b.append(43)
print(b)
b.remove(43)
print(b)  # удаляет первый найденное значение, если хотим удалить все используем цикл while

print('\n.reverse():')
print(b)
b.reverse()
print(b)
b.reverse()
print(b)

print('\n.sort():')
b.sort()
print(b)
b.reverse()
print(b)
b.sort()
print(b)
b.sort(reverse=True)
print(b)
