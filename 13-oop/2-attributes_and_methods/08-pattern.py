"""
PATTERN МОНО-СОСТОЯНИЕ
     для всех экземпляров класса

        · Это такой класс, у экземпляров которого будет одно общее состояние.
        · Изменения одного экземпляра будут затрагивать другие экземпляры.
        · У каждого объекта хранится ссылка на один и тотже словарь-атрибут, когда один объект, изменяет этот словарь,
            данное изменение будет касаться каждого объекта.

            class [class]:
                __attribute = {             --> защищенный атрибут класса (типа словарь)
                    attribute1: element1,
                    attribute2: element2,
                    ...
                }

                def __init__(self):
                    self.__dict__ = [class].__attribute
"""


class Cat:

    breed = 'pers'


a = Cat()
b = Cat()
c = Cat()
a.breed = 'siam'
b.color = 'black'
print(a.__dict__, b.__dict__, c.__dict__, sep='\n')


class Cat:

    __shared = {
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared


d = Cat()
e = Cat()
h = Cat()
d.breed = 'siam'
d.name = 'Bob'
print(d.__dict__, e.__dict__, h.__dict__, sep='\n')
print(Cat.__dict__)
