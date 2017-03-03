from tkinter import *

#Тут будут функции
def number_button(event,but):
    h = but['text']
    text1.insert(END, s)
    print(h)

def clear(event):
    text1.delete(0,END)

def summa(event):
    pass

def proiz(event):
    pass

def minus(event):
    pass

root = Tk()
#root.geometry('300x300')
root.title('Калькулятор')

# this removes the maximize button
root.resizable(0,0)

#рабочие области в виде фрэймов
frame1 = Frame(root)
frame1.pack(side=TOP, pady=5) #, expand = YES, fill=BOTH
#тут нужно задать размер фрейма
frame2 = Frame(root)
frame2.pack(side=LEFT,anchor=N, pady=5, padx=5)
frame4 = Frame(root)
frame4.pack(side=LEFT,anchor=S, pady=5)
frame3 = Frame(root)
frame3.pack(side=RIGHT,anchor=N)



text1=Entry(frame1, font='Arial 30',justify='right',bd=20, insertwidth=-1 )
text1.pack(side=RIGHT, anchor=N)

#1 ряд
b_b = Button(frame2, text='<--', width=3, bd=8, fg="red",font='Arial 30')
b_b.grid(row =1, column = 1)
b_ce = Button(frame2, text='CE', width=3, bd=8, fg="red",font='Arial 30')
b_ce.grid(row =1, column = 2)
b_c = Button(frame2, text='C', width=3, bd=8, fg="red",font='Arial 30')
b_c.grid(row =1, column = 3)
b_p_m = Button(frame2, text='+/-', width=3, bd=8, fg="red",font='Arial 30')
b_p_m.grid(row =1, column = 4)
b_sqrt = Button(frame2, text='sqrt', width=3, bd=8, fg="red",font='Arial 30')
b_sqrt.grid(row =1, column = 5)

#2 ряд
b_7 = Button(frame2, text='7', width=3, bd=8, fg="red",font='Arial 30')
b_7.grid(row =2, column = 1)
b_8 = Button(frame2, text='8', width=3, bd=8, fg="red",font='Arial 30')
b_8.grid(row =2, column = 2)
b_9 = Button(frame2, text='9', width=3, bd=8, fg="red",font='Arial 30')
b_9.grid(row =2, column = 3)
b_d = Button(frame2, text='/', width=3, bd=8, fg="red", font='Arial 30')
b_d.grid(row =2, column = 4)
b_pr = Button(frame2, text='%', width=3, bd=8, fg="red", font='Arial 30')
b_pr.grid(row =2, column = 5)

#Кнопки цифр от 4 до *
b_4 = Button(frame2, text='4', width=3, bd=8, fg="red",font='Arial 30')
b_4.grid(row =3, column = 1)
b_5 = Button(frame2, text='5', width=3, bd=8, fg="red",font='Arial 30')
b_5.grid(row =3, column = 2)
b_6 = Button(frame2, text='6', width=3, bd=8, fg="red",font='Arial 30')
b_6.grid(row =3, column = 3)
b_u = Button(frame2, text='*', width=3, bd=8, fg="red",font='Arial 30')
b_u.grid(row =3, column = 4)
b_x = Button(frame2, text='1/x', width=3, bd=8, fg="red",font='Arial 30')
b_x.grid(row =3, column = 5)

#Кнопки цифр от 1 до -
b_1 = Button(frame2, text='1', width=3, bd=8, fg="red",font='Arial 30')
b_1.grid(row =4, column = 1)
b_2 = Button(frame2, text='2', width=3, bd=8, fg="red",font='Arial 30')
b_2.grid(row =4, column = 2)
b_3 = Button(frame2, text='3', width=3, bd=8, fg="red",font='Arial 30')
b_3.grid(row =4, column = 3)
b_m = Button(frame2, text='-', width=3, bd=8, fg="red",font='Arial 30')
b_m.grid(row =4, column = 4)
b_r = Button(frame2, text='=', width=3, bd=8, fg="red",font='Arial 30', height=3)
b_r.grid(row =4, column = 5, rowspan=2)

#Кнопки от 0 до + height=32, width=32
b_0 = Button(frame2, text='0', width=8, bd=8, fg="red",font='Arial 30')
b_0.grid(row =5, column = 1, columnspan=2)
b_t = Button(frame2, text=',', width=3, bd=8, fg="red",font='Arial 30')
b_t.grid(row =5, column = 3)
b_p = Button(frame2, text='+', width=3, bd=8, fg="red",font='Arial 30')
b_p.grid(row =5, column = 4)


root.mainloop()