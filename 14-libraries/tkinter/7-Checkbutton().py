"""
WIDGET CHECKBUTTON
"""

import tkinter as tk


def select_all():
    for check in [over_18, commercial, follow]:
        check.select()


def deselect_all():
    for check in [over_18, commercial, follow]:
        check.deselect()


def switch_all():
    for check in [over_18, commercial, follow]:
        check.toggle()


def show():
    print('Флажок 18', over_18_value.get())
    print('Реклама', commercial_value.get())


win = tk.Tk()
win.geometry('600x400+100+200')

over_18_value = tk.StringVar()
over_18_value.set('No')
commercial_value = tk.IntVar()  # по умолчанию =0

over_18 = tk.Checkbutton(win, text='Вам исполнилось 18?',
                         variable=over_18_value,
                         offvalue='No',
                         onvalue='Yes'
                         )
over_18.pack()
commercial = tk.Checkbutton(win, text='Хотите получать рекламу?',
                            variable=commercial_value,
                            offvalue=0,
                            onvalue=1
                            )
commercial.pack()
follow = tk.Checkbutton(win, text='Хотите подписаться на канал?',
                        indicatoron=0
                        )
follow.pack()

tk.Button(win, text='Select All', command=select_all).pack()
tk.Button(win, text='Deselect All', command=deselect_all).pack()
tk.Button(win, text='Switch', command=switch_all).pack()
tk.Button(win, text='Show', command=show).pack()

win.mainloop()
