"""
WIDGET ENTRY
"""

import tkinter as tk


def get_entry():
    value = name.get()
    if value:
        print(value)
    else:
        print('Empty Entry')


def delete_entry():
    name.delete(0, 'end')  # индексы от - до


def submit():
    print(name.get())
    print(password.get())
    delete_entry()
    password.delete(0, tk.END)


win = tk.Tk()
win.geometry('600x400+100+200')
# Label
tk.Label(win, text='Имя').grid(row=0, column=0, stick='w')
tk.Label(win, text='Пароль').grid(row=1, column=0, stick='w')
# Entry
name = tk.Entry(win, width=10)
password = tk.Entry(win, show='*', width=10)
name.grid(row=0, column=1)
password.grid(row=1, column=1)
# Button
tk.Button(win, text='Get', command=get_entry).grid(row=2, column=0, stick='we')
tk.Button(win, text='Delete', command=delete_entry).grid(row=2, column=1, stick='we')
tk.Button(win, text='Insert', command=lambda: name.insert(1, 'hello'))\
    .grid(row=2, column=2, stick='we')
tk.Button(win, text='Submit', command=submit).grid(row=3, column=0, stick='we')

win.grid_columnconfigure(0, minsize=100)
win.grid_columnconfigure(1, minsize=100)
win.grid_columnconfigure(2, minsize=100)

win.mainloop()
