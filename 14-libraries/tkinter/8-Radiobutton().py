"""
WIDGET RADIOBUTTON
"""

import tkinter as tk

levels = {
    1: 'Easy',
    2: 'Middle',
    3: 'Hard'
}


def select_level():
    level = level_var.get()
    level_text.set(f'Вы выбрали {level} уровень')
    print(levels[level])


win = tk.Tk()
win.geometry('600x400+100+200')

level_var = tk.IntVar()
nation_var = tk.IntVar()
level_text = tk.StringVar()

tk.Label(win, text='Выберите уровень сложности:').pack()
for level in sorted(levels):
    tk.Radiobutton(win, text=levels[level], variable=level_var, value=level, command=select_level).pack()
# tk.Radiobutton(win, text='Easy', variable=level_var, value=1, command=select_level).pack()
# tk.Radiobutton(win, text='Middle', variable=level_var, value=2, command=select_level).pack()
# tk.Radiobutton(win, text='Hard', variable=level_var, value=3, command=select_level).pack()
tk.Label(win, textvariable=level_text).pack()
tk.Label(win).pack()
tk.Label(win, text='Выберите расу:').pack()
tk.Radiobutton(win, text='Эльфы', variable=nation_var, value=4, command=select_level).pack()
tk.Radiobutton(win, text='Люди', variable=nation_var, value=5, command=select_level).pack()
tk.Radiobutton(win, text='Орки', variable=nation_var, value=6, command=select_level).pack()

win.mainloop()
