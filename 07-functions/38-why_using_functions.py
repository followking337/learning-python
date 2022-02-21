"""
У функций два основных плюса:
    1. Помогают устранить избыточность кода.
    2. Обеспечивают декомпозицию проблемы - возможность разбить одну большую задачу на более мелкие задачи.
"""
import turtle


def move(a):
    turtle.forward(a)
    turtle.left(90)


def draw_square(a):
    for i in range(4):
        move(a)


def draw_color_square(a, color):
    turtle.color(color)
    turtle.begin_fill()
    draw_square(a)
    turtle.end_fill()


turtle.speed(2)
draw_color_square(60, 'red')
turtle.goto(120, 120)
draw_color_square(120, 'blue')
