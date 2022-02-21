from turtle import right, left, forward, speed, goto, color, begin_fill, end_fill


def turn(direction):
    if direction == 'right':
        right(90)
    elif direction == 'left':
        left(90)


def move(x, y, direction):
    forward(x)
    turn(direction)
    forward(y)
    turn(direction)


def drawing(x, y, direction):
    for i in range(2):
        move(x, y, direction)


def color_drawing(x, y, direction, col, col2):
    color(col, col2)
    begin_fill()
    drawing(x, y, direction)
    end_fill()


speed(2)
drawing(100, 60, 'left')
goto(-50, -50)
drawing(60, 30, 'right')
goto(-100, -100)
color_drawing(100, 60, 'right', 'green', 'yellow')
goto(-150, -150)
color_drawing(120, 80, 'right', 'red', 'orange')
