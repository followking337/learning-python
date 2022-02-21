print('\nЗадача 1')


def factorial(n):
    pr = 1
    for i in range(2, n+1):
        pr *= i
    return pr


print(factorial(5))

print('\nЗадача 2.1')


def find_duplicate(a):
    d = {i: a.index(i) for i in set(a) if a.count(i) > 1}
    duplicates = [i[0] for i in sorted(d.items(), key=lambda par: par[1])]
    return duplicates


a = [6, 6, 4, 5, 2, 3, 2, 1, 4, 4]
# a = [2, 1, 1, 1, 1, 1, 2, 2, 2, 2]
print(find_duplicate(a))

print('\nЗадача 2.2')


def find_duplicate(a):
    duplicates = []
    for i in a:
        if a.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates


a = [6, 6, 4, 5, 2, 3, 2, 1, 4, 4]
# a = [2, 1, 1, 1, 1, 1, 2, 2, 2, 2]
print(find_duplicate(a))  # [6, 4, 2]
assert find_duplicate([1, 2, 2, 3]) == [2]
print(find_duplicate([1, 2, 2, 3]))  # [2]
assert find_duplicate([7, 7, 7]) == [7]
print(find_duplicate([7, 7, 7]))  # [7]
assert find_duplicate([3, 2, 1, 1, 3, 2]) == [3, 2, 1]
print(find_duplicate([3, 2, 1, 1, 3, 2]))  # [3, 2, 1]
assert find_duplicate([1, 2, 3]) == []
print(find_duplicate([1, 2, 3]))  # []

print('\nЗадача 3')


def first_unique_char(s):
    for i in s:
        if s.count(i) == 1:
            return s.find(i)
    return -1


assert first_unique_char('python') == 0
print(first_unique_char('python'))
assert first_unique_char('abracadabra') == 4
print(first_unique_char('abracadabra'))
assert first_unique_char('abcabc') == -1
print(first_unique_char('abcabc'))

print('\nЗадача 4')


def format_namelist(a):
    s = ''
    for i in range(len(a)):
        s += a[i]['name']
        if i + 1 == len(a):
            return s
        elif i + 2 == len(a):
            s += ' и '
        else:
            s += ', '
    return s


assert format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'
print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]))
assert format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'
print(format_namelist([{'name': 'Bart'}, {'name': 'Lisa'}]))
assert format_namelist([{'name': 'Bart'}]) == 'Bart'
print(format_namelist([{'name': 'Bart'}]))
assert format_namelist([]) == ''
print(format_namelist([]))
