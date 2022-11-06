"""
WIDGET LABEL
"""

import tkinter as tk

win = tk.Tk()
win.geometry('300x400+100+200')

label1 = tk.Label(win, text="""Hello,
my
friend!!!""",
                  bg='red',          # back ground color
                  fg='white',        # font ground color
                  font=('Arial', 20, 'bold'),  # font=('name', size, 'type')
                  padx=20,           # отступы от label до текста по горизонтали (в пикселях)
                  pady=40,           # отступы от label до текста по вертикали (в пикселях)
                  width=10,          # ширина label по горизонтали (в числе символов)
                  height=5,          # ширина label по вертикали (в числе символов)
                  anchor='sw',       # расположение текста внутри label: n, ne, e, se, s, sw, w, nw, center
                  relief=tk.RAISED,  # границы
                  bd=10,             # ширина границ
                  justify=tk.RIGHT   # прижимает строки LEFT, CENTER, RIGHT
                  )
label1.pack()                        # располагает текст на экране

win.mainloop()
