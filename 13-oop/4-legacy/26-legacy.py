class Person:  # parent class Person is subclassed by Doctor, Ortoped, Architecture

    def breathe(self):
        print('я могу дышать')

    def walk(self):
        print('я могу ходить')


class Doctor(Person):  # Doctor is subclass from parent class Person

    def cure(self):
        print('я могу лечить')


class Ortoped(Doctor):  # Ortoped is subclass from parent class Doctor
    pass


class Architecture(Person):  # Architecture is subclass from parent class Person

    def build(self):
        print('я могу построить здание')


d = Doctor()
a = Architecture()
o = Ortoped()

print('\n\tDoctor:')
d.breathe()
d.walk()
d.cure()

print('\n\tArchitecture:')
a.breathe()
a.walk()
a.build()

print('\n\tissubclass():')
print(issubclass(Doctor, Person))        # True
print(issubclass(Person, Doctor))        # False
print(issubclass(Architecture, Person))  # True
print(isinstance(d, Doctor))             # True
print(isinstance(d, Person))             # True

print('\n\tOrtoped:')
o.breathe()
o.walk()
o.cure()
