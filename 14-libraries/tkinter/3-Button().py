"""
WIDGET BUTTON
"""

import tkinter as tk

win = tk.Tk()
win.geometry('300x400+100+200')


def say_hello():
    print('hello')


def add_label():
    label = tk.Label(win, text='def')
    label.pack()


def counter():
    global count
    count += 1
    button4['text'] = f'Counter: {count}'  # изменяем свойство 'text' у button4 как у словаря


button1 = tk.Button(win, text='Hello',
                    command=say_hello
                    )
button2 = tk.Button(win, text='Add new label (def)',
                    command=add_label
                    )
button3 = tk.Button(win, text='Add new label (lambda)',
                    command=lambda: tk.Label(win, text='lambda').pack()
                    )
count = 0
button4 = tk.Button(win, text=f'STAR',
                    command=counter,
                    background='red',          # не работает
                    fg='blue',
                    activebackground='green',  # не работает
                    state=tk.NORMAL            # DISABLED
                    )

button1.pack()
button2.pack()
button3.pack()
button4.pack()

win.mainloop()
