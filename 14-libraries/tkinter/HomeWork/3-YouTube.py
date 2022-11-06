import tkinter as tk

win = tk.Tk()

win.title('My first GUI App')
win.geometry('300x400+100+200')


def counter():
    global count
    count += 1
    button1['text'] = f'Counter {count}'
    state = [tk.NORMAL, tk.DISABLED]
    button2['state'] = state[count % 2]


def changeBG():
    global i
    colors = ['red', 'blue', 'yellow', 'grey', 'green', 'black']
    win.config(bg=colors[i])
    i += 1
    if i == len(colors):
        i = 0


def reset():
    global count
    count = 0
    button1['text'] = 'START'


count = 0
i = 0
button1 = tk.Button(win, text='START',
                    command=counter)
button2 = tk.Button(win, text='HOLD',
                    command=lambda: tk.Label(win, text='hello').pack(),
                    state=tk.NORMAL)
button3 = tk.Button(win, text='BACKGROUND',
                    command=changeBG)
button4 = tk.Button(win, text='RESET COUNTER',
                    command=reset)

button1.pack()
button2.pack()
button3.pack()
button4.pack()

win.mainloop()
