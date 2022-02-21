class Person:  # parent

    color = 'white'

    def __init__(self, name):
        print('__init__ Person')
        self.name = name

    def __str__(self):
        return f'Person: {self.name}'

    def breathe(self):
        print('человек дышит')

    def walk(self):
        print('человек идет')

    def sleep(self):
        print('человек спит')

    def combo(self):
        self.breathe()
        self.walk()
        self.sleep()


class Doctor(Person):  # subclass

    color = 'black'            # overriding - переопределение родительского атрибута у дочернего класса через присвоение
                               # одинакового имени атрибуту.

    def __str__(self):
        return f'Doctor: {self.name}'

    def breathe(self):         # overriding - переопределение родительского метода у дочернего класса через присвоение
        print('доктор дышит')  # одинакового имени методу.

    def sleep(self):
        print('доктор спит')


p = Person('John')
d = Doctor('Adam')

print('\n\tOverriding Methods:')
p.breathe()
d.breathe()
p.walk()
d.walk()

print('\n\tOverriding Attributes:')
print(p.color, d.color)

print('\n\tOverriding Dunder Methods:')
print(p, d)

print('\n\tcombo():')
p.combo()
print('------------')
d.combo()
