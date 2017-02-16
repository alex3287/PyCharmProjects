# -*- coding:utf-8 -*-
from tkinter import *


# окно
tk = Tk()
tk.geometry("300x200+100+100")


# функция читающая буфер
def read(e):
    bufer_data['text'] = tk.clipboard_get()


# функция записывающая в буфер
def write(e):
    tk.clipboard_clear()
    tk.clipboard_append('akzo rulez:)')


# текст с содержанием буфера
bufer_data = Label(tk, text="No Data")
bufer_data.pack(expand='YES')

# кнопка вызывающая фкнуцию для чтения
button = Button(tk, text="Read Bufer Data")
button.pack(expand='YES')
button.bind("<Button-1>", read)

# кнопка для записи
button = Button(tk, text="Write Bufer Data")
button.pack(expand='YES')
button.bind("<Button-1>", write)

tk.mainloop()