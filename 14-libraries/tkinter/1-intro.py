"""
TKINTER
    GUI - Graphical User Interface
"""

import tkinter as tk

win = tk.Tk()

win.title('My first GUI App')    # заголовок окна
win.geometry('500x600+100+200')  # 500x600 размер окна; +100+200 пиксели слева и сверху позиция окна
win.minsize(300, 400)            # минимальный размер окна (по ширине, по высоте)
win.maxsize(700, 800)            # максимальный размер окна (по ширине, по высоте)
win.resizable(False, False)      # вкл/выкл менять размер окна (по ширине, по высоте)

photo = tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)      # иконка в Mac появляется только в about

win.config(bg='grey')
win.config(bg='#33FFF9')         # --> https://htmlcolorcodes.com/es/

win.mainloop()  # главный цикл, переход программы в режим ожидания
