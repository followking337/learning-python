"""
METHOD GRID()
    размещает виджеты в окне в виде таблицы

    [widget].grid(row=, column=)
"""

import tkinter as tk

win = tk.Tk()
win.geometry('600x400+100+200')

# button1 = tk.Button(win, text='Hello 1')
# button2 = tk.Button(win, text='Hello 2')
# button3 = tk.Button(win, text='Hello 3')
# button4 = tk.Button(win, text='Hello World 4')
# button5 = tk.Button(win, text='Hello 5')
# button6 = tk.Button(win, text='Hello 6')
# button7 = tk.Button(win, text='Hello 7')
# button8 = tk.Button(win, text='Hello 8')
# button1.grid(row=0, column=0)
# button2.grid(row=0, column=1, stick='W')
# button3.grid(row=1, column=0, stick='WE')
# button4.grid(row=1, column=1)
# button5.grid(row=2, column=0)
# button6.grid(row=2, column=1, stick='E')
# button7.grid(row=3, column=0, columnspan=2, stick='WE')  # columnspan=/rowspan= --> сколько позиций занимает 1 кнопка
# button8.grid(row=0, column=2, rowspan=4, stick='NS')     # stick= --> растягивает кнопку по направлению

for i in range(5):
    for j in range(2):
        tk.Button(win, text=f'point {i}-{j}').grid(row=i, column=j, stick='we')

win.grid_columnconfigure(0, minsize=100)  # minsize= в пикселях
win.grid_columnconfigure(1, minsize=100)  # minsize= в пикселях

win.mainloop()
