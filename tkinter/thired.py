from tkinter import *

def pr_h(event):
    global s
    s=0
    s += int(ed.get())
    ed.delete(0,END)

def pr_h2(event):
    lbl2['text']='Ответ ' + str(s)
    ed.delete(0,END)
root = Tk()
root.geometry('200x200')
but = Button(root, text='Clic me')
but.pack(side='top')
lbl1 = Label(root, text='Представьтесь. Как ваше имя?')
lbl1.pack()

ed=Entry(root, width=20)
ed.pack()

lbl2 = Label(root)
lbl2.pack()

but.bind("<Button-1>", pr_h)
but.bind("<Button-2>", pr_h2)

root.mainloop()
