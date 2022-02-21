from collections import defaultdict

print('\nint():')
print(int())
r = defaultdict(int)
print(r, type(r))
print(r['one'])
print(r, type(r))

print('\nlist():')
print(list())
a = defaultdict(list)
print(a, type(a))
print(a[1])
print(a, type(a))
a['a'] = 123
print(a, type(a))

print('\ndefault_factory:')
print(a.default_factory)
a.default_factory = lambda: [1, 2, 3]  # default_factory should be callable
print(a[4])
print(a, type(a))
a.default_factory = lambda: 'hello'
print(a[5])
print(a, type(a))

print('\nПрименение:')
data = [
    ('Ivanov', 2),
    ('Petrov', 1),
    ('Sidorov', 5),
    ('Petrov', 3),
    ('Ivanov', 2),
    ('Ivanov', 4),
]
marks = defaultdict(int)
marks_list = defaultdict(list)
marks_unique = defaultdict(set)

for surname, mark in data:
    print(surname, mark)
    marks[surname] += mark
    marks_list[surname].append(mark)
    marks_unique[surname].add(mark)

print(marks)
print(marks_list)
print(marks_unique)
