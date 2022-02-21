print('\nЗадача 1')
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Physics', 93), ('History', 82)]
for i in sorted(subject_marks, key=lambda x: x[1]):
    print(*i)

print('\nЗадача 2')
subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
                 ('Physics', 93), ('History', 82), ('French', 78),
                 ('Art', 58), ('Chemistry', 76), ('Programming', 91)]
# for i in sorted(subject_marks, key=lambda x: x[1], reverse=True):
for i in sorted(subject_marks, key=lambda x: -x[1]):
    print(*i)

print('\nЗадача 3')
subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]
for i in sorted(subject_marks, key=lambda x: (-x[1], x[0])):
    print(*i)

print('\nЗадача 4')
models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
          {'make': 'Apple', 'model': 10, 'color': 'Silver'},
          {'make': 'Oppo', 'model': 9, 'color': 'Red'},
          {'make': 'Huawei', 'model': 4, 'color': 'Grey'},
          {'make': 'Honor', 'model': 3, 'color': 'Black'}]
for i in sorted(models, key=lambda x: x['color']):
    print(f'Производитель: {i["make"]}, модель: {i["model"]}, цвет: {i["color"]}')
