print('\nЗадача 1.1')


class Person:
    gend_dict = {'male': 'Гражданин',
                 'female': 'Гражданка'
                 }

    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        self.gender = self.set_gender(gender)

    @staticmethod
    def set_gender(gender):
        if gender in Person.gend_dict:
            return gender
        else:
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            return 'male'

    def __str__(self):
        return f'{Person.gend_dict[self.gender]} {self.surname} {self.name}'


p1 = Person('Chuck', 'Norris')
print(p1)  # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2)  # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3)  # печатает "Гражданин Кеноби Оби-Ван"

print('\nЗадача 1.2')


class Person:

    def __init__(self, name, surname, gender='male'):
        if gender not in ('male', 'female'):
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            gender = 'male'
        self.name = name
        self.surname = surname
        self.gender = gender

    def __str__(self):
        return f"Граждан{['ин', 'ка'][self.gender == 'female']} {self.surname} {self.name}"


p1 = Person('Chuck', 'Norris')
print(p1)  # печатает "Гражданин Norris Chuck"
p2 = Person('Mila', 'Kunis', 'female')
print(p2)  # печатает "Гражданка Kunis Mila"
p3 = Person('Оби-Ван', 'Кеноби', True)  # печатает "Не знаю, что вы имели ввиду? Пусть это будет мальчик!"
print(p3)  # печатает "Гражданин Кеноби Оби-Ван"

print('\nЗадача 2.1')


class Vector:

    def __init__(self, *args):
        # self.values = [i for i in args if isinstance(i, int)]
        self.values = sorted(filter(lambda x: type(x) == int, args))

    def __str__(self):
        return f'Вектор{tuple(sorted(self.values))}' if len(self.values) else "Пустой вектор"


v1 = Vector(3, 2, 1, 'hello', 5.78)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector()
print(v2)  # печатает "Пустой вектор"
