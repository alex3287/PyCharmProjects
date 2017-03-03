#! usr/bin/python3
#программа для работы с буфером обмена
import pyperclip
from tkinter import *

buf =[]

def save(event):
    '''копирует данные из буфера'''
    global  buf
    buf.append(pyperclip.paste())

def prin(event):
    global buf
    print(buf)

def sel():
    global look
    '''меняет буфер обмена на то значение, что выбираем из списка'''
    global buf
    selection = buf[var.get()]
    pyperclip.copy(selection)
    look.delete(0.0, END)
    look.insert(0.0, selection[:500])


def new(event):
    global look
    '''Показывает варианты которые находятся в буфере и
    формирует поле для вывода на просмотр'''
    global buf

    for i in range(len(buf)):
        b = Radiobutton(fr1, text='buffer-' + str(i+1), value=i, variable=var, command=sel)
        b.pack()
    var.set(i)
    #look = tkinter.Text(root)
    #look.pack()

def clean(event):
    global buf, b, look
    look.delete(0.0,END)
    for i in range(len(buf)):
        b.deselect()
    buf = []

root = Tk()
root.geometry('400x400')
root.title('Буфер обмена')
fr1 = Frame(root)
fr1.pack()
fr2 = Frame(root)
fr2.pack()
var = IntVar()
abut = Label(fr1, text = 'Программа для работы с буфером обмена')
abut.pack()

btn1=Button(fr1, text = 'Сохранить данные из буфера')
btn1.pack(side='top')

btn2=Button(fr1, text = 'Обновить значение в буфере буфера')
btn2.pack()

btn3=Button(fr1, text = 'Очистить')
btn3.pack()

btn1.bind("<Button-1>", save)
btn1.bind("<Button-2>", prin)
btn2.bind("<Button-1>", new)
btn3.bind("<Button-1>", clean)

look = Text(fr2)
look.pack()

root.mainloop()