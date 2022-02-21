class Vector:

    def __init__(self, *args):
        self.values = sorted(filter(lambda x: isinstance(x, int), args))

    def __str__(self):
        return f'Вектор{tuple(self.values)}' if len(self.values) else "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            return Vector(*[i + other for i in self.values])
            # return Vector(*map(lambda x: x + other, self.values))
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                return Vector(*[sum(i) for i in zip(self.values, other.values)])
                # return Vector(*map(lambda x, y: x + y, self.values, other.values))
            else:
                print("Сложение векторов разной длины недопустимо")
        print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, int):
            # return Vector(*[i * other for i in self.values])
            return Vector(*map(lambda x: x * other, self.values))
        elif isinstance(other, Vector):
            if len(self.values) == len(other.values):
                # return Vector(*[i[0] * i[1] for i in zip(self.values, other.values)])
                return Vector(*map(lambda x, y: x * y, self.values, other.values))
            else:
                print("Умножение векторов разной длины недопустимо")
        print(f'Вектор нельзя умножать с {other}')


v1 = Vector(3, 2, 1, 'hello', 5.78)
print(v1)  # печатает "Вектор(1, 2, 3)"
v2 = Vector(3, 4, 5)
print(v2)  # печатает "Вектор(3, 4, 5)"
v3 = v1 + v2
print(v3)  # печатает "Вектор(4, 6, 8)"
v4 = v3 + 5
print(v4)  # печатает "Вектор(9, 11, 13)"
v5 = v1 * 2
print(v5)  # печатает "Вектор(2, 4, 6)"
v5 + 'hi'  # печатает "Вектор нельзя сложить с hi"
