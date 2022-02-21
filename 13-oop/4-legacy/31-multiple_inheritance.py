"""
MULTIPLE INHERITANCE - Множественное наследование
    Класс у наследуется от нескольких родителей.

        __mro__ --> method resolution order (порядок поиска методов):

            - class.__mro__

            1. Нынешний класс.
            2. Первый класс родитель.
            3. Следующий класс родитель.
            4. ...

        Делегирование:

            class Subclass(Parent1, Parent2):
                def __init__(self, argument1, argument2):
                    super().__init__(argument1)
                    Parent2.__init__(self, argument2)
"""


class Doctor:

    def __init__(self, degree):
        self.degree = degree

    def cure(self):
        print('я доктор, я умею лечить')

    def build(self):
        print('я доктор, я тоже умею строить, но не очень')

    def graduate(self):
        print('Ура, я отучился на доктора')


class Builder:

    def __init__(self, rank):
        self.rank = rank

    def build(self):
        print('я строитель, я умею строить')

    def graduate(self):
        print('Ура, я отучился на строителя')


class Person(Doctor, Builder):

    def __init__(self, degree, rank):
        # self.degree = degree
        # self.rank = rank
        super().__init__(degree)
        Builder.__init__(self, rank)

    def __str__(self):
        return f'Person: {self.degree} {self.rank}'

    # def build(self):
    #     print('я человек, я тоже умею строить')

    def graduate(self):
        print('Посмотрим кем я стал')
        super().graduate()
        Builder.graduate(self)


p = Person('бакалавр', 5)

print('\nПорядок Поисков Методов:')

print('\n\tБез конфликта имен:')  # class Person(Doctor, Builder):
p.cure()
p.build()                         #     pass

print('\n\tС конфликтом имен:')   # class Person(Doctor, Builder):
p.build()                         #      build(self)
print(Person.__mro__)

print('\nДелегирование:')
p.graduate()
print(p)
