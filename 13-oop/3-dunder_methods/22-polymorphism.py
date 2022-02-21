from polymorphism import Rectangle, Square, Circle


rec1 = Rectangle(3, 4)
rec2 = Rectangle(12, 5)
print(rec1.get_rect_area(), rec2.get_rect_area())

sq1 = Square(5)
sq2 = Square(7)
print(sq1.get_sq_area(), sq2.get_sq_area())

cir1 = Circle(3)
cir2 = Circle(2)
print(cir1.get_cir_area(), cir2.get_cir_area())

figures = [rec1, rec2, sq1, sq2, cir1, cir2]

print('\n\tПроблема:')
for figure in figures:
    if isinstance(figure, Rectangle):
        print(figure.get_rect_area())
    elif isinstance(figure, Square):
        print(figure.get_sq_area())
    elif isinstance(figure, Circle):
        print(figure.get_cir_area())

print('\n\tРешение:')
for figure in figures:
    print(figure, f'with area: {figure.get_area()}')
