print('\nЗадача 1')


class Laptop:

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = self.brand + ' ' + self.model


hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price)
print(hp.laptop_name)

print('\nЗадача 2')


class SoccerPlayer:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.goals = 0
        self.assists = 0

    def score(self, goals=1):
        self.goals += goals

    def make_assist(self, assists=1):
        self.assists += assists

    def statistics(self):
        print(f'{self.surname} {self.name} - голы: {self.goals}, передачи: {self.assists}')


leo = SoccerPlayer('Leo', 'Messi')
leo.score(700)
leo.make_assist(500)
leo.statistics()
kokorin = SoccerPlayer('Alex', 'Kokorin')
kokorin.score()
kokorin.statistics()

print('\nЗадача 3.1')


class Zebra:

    def __init__(self):
        self.count = 1

    def which_stripe(self):
        if self.count % 2 == 1:
            print('Полоска белая')
        else:
            print('Полоска черная')
        self.count += 1


z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
z2.which_stripe()

print('\nЗадача 3.1')


class Zebra:

    flag = True

    def which_stripe(self):
        print('Полоска белая' if self.flag else 'Полоска черная')
        self.flag = not self.flag


z1 = Zebra()
z1.which_stripe()
z1.which_stripe()
z1.which_stripe()

z2 = Zebra()
z2.which_stripe()

print('\nЗадача 4')


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        return self.age > 17


p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())
print(p1.is_adult())
