print('\nЗадача 1')


class City:

    def __init__(self, city_name):
        self.name = city_name.title()

    def __str__(self):
        return f'{self.name}'

    def __bool__(self):
        return self.name[-1] not in 'aeoui'


p1 = City('new york')
print(p1)          # печатает "New York"
print(bool(p1))    # печатает "True"
p2 = City('SaN frANCISco')
print(p2)          # печатает "San Francisco"
print(p2 is True)  # печатает "False"

print('\nЗадача 2')


class Quadrilateral:

    def __init__(self, width, height=None):
        self.width = width
        if height is None:       # self.height = height or width
            self.height = width  # self.height = height if height != None else width
        else:
            self.height = height

    def __str__(self):
        # return f'{["Куб", "Прямоугольник"][self.width != self.height]} размером {self.width}х{self.height}'
        return f'{["Куб", "Прямоугольник"][not bool(self)]} размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height


q1 = Quadrilateral(10)
print(q1)          # печатает "Куб размером 10х10"
print(bool(q1))    # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)          # печатает "Прямоугольник размером 3х5"
print(q2 is True)  # печатает "False"
