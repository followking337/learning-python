class Person:

    age = 25

    def breathe(self):
        print('Человек дышит')

    def sleep(self):
        print('Человек спит')

    def combo(self):
        self.breathe()
        if hasattr(self, 'walk'):
            self.walk()
        self.sleep()
        if hasattr(self, 'age'):
            print(self.age)


class Doctor(Person):

    age = 30

    def breathe(self):  # overriding: переопределение метода у класса Person
        print('Доктор дышит')

    def sleep(self):    # extending: расширение класса Person в случае если данного метода нет у класса Person
        print('Доктор спит')

    def walk(self):
        print('Доктор идет')


p = Person()
d = Doctor()

p.breathe()
d.breathe()
d.sleep()
# p.sleep()  # AttributeError: 'Person' object has no attribute 'sleep'

print('\n\tcombo():')
p.combo()  # AttributeError: 'Person' object has no attribute 'walk'
print('-' * 20)
d.combo()
