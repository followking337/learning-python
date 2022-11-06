"""
WIDGET COMBOBOX
"""

import tkinter as tk
from tkinter import ttk


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point {self.x} {self.y}'


def show_day():
    print(combo1.get(), combo2.get())


def set_day():
    combo1.set('aaaaa')


weekDays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
list_int = [1, 2, 3, 4, 5]  # через метод get() передается строка

win = tk.Tk()
win.geometry('600x400+100+200')

combo1 = ttk.Combobox(win, values=weekDays)
combo1.current(1)  # index
combo1.pack()
combo2 = ttk.Combobox(win, values=list_int)
combo2.current(4)  # index
combo2.pack()
combo3 = ttk.Combobox(win, values=[Point(2, 5), Point(1, 1)])  # через метод get() передается строка
combo3.pack()

ttk.Button(win, text='show day', command=show_day).pack()
ttk.Button(win, text='set day', command=set_day).pack()

win.mainloop()
