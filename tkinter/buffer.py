#! usr/bin/python3
#программа для работы с буфером обмена
import tkinter, pyperclip

buf =[]

def save(event):
    '''копирует данные из буфера'''
    global  buf
    buf.append(pyperclip.paste())

def prin(event):
    global buf
    print(buf)

def sel():
    '''меняет буфер обмена на то значение, что выбираем из списка'''
    global buf
    selection = buf[var.get()]
    pyperclip.copy(selection)


def new(event):
    global buf

    for i in range(len(buf)):
        b = tkinter.Radiobutton(root, text='buffer-' + str(i+1), value=i, variable=var, command=sel)
        b.pack()
    var.set(i)
    look = tkinter.Text(root)
    look.pack()

def clean(event):
    global buf,b
    for i in range(len(buf)):
        b.deselect()
    buf = []

root = tkinter.Tk()
root.geometry('400x400')
var = tkinter.IntVar()
abut = tkinter.Label(root, text = 'Программа для работы с буфером обмена')
abut.pack()
btn1=tkinter.Button(root, text = 'Сохранить данные из буфера')
btn1.pack(side='top')

btn2=tkinter.Button(root, text = 'Обновить значение в буфере буфера')
btn2.pack()

btn3=tkinter.Button(root, text = 'Очистить')
btn3.pack()


btn1.bind("<Button-1>", save)
btn1.bind("<Button-2>", prin)
btn2.bind("<Button-1>", new)
btn3.bind("<Button-1>", clean)

root.mainloop()