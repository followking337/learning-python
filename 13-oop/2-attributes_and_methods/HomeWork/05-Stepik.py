print('\nЗадача 1')


class Lion:

    def roar(self):
        print("Rrrrrrr!!!")


simba = Lion()
simba.roar()

print('\nЗадача 2')


class Counter:

    def start_from(self, start=0):
        self.count = start

    def increment(self):
        self.count += 1

    def display(self):
        print(f'Текущее значение счетчика = {self.count}')

    def reset(self):
        self.count = 0


print('\nc1:')
c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.increment()
c1.display()
c1.reset()
c1.display()

print('\nc2:')
c2 = Counter()
c2.start_from(3)
c2.display()
c2.increment()
c2.display()

print('\nЗадача 3')


class Point:

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_distance(self, p2):
        if hasattr(p2, 'x') and hasattr(p2, 'y'):
            return ((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2) ** 0.5  # Теорема Пифагора по 2 точкам
        else:
            print("Передана не точка")


p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
print(p1.x, p1.y)
print(p2.x, p2.y)
print(p1.get_distance(p2))
print(p1.get_distance(10))
