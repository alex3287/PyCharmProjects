from tkinter import *

root = Tk()
root.geometry('305x300')
root.title('Калькулятор')

#рабочие области в виде фрэймов
frame1 = Frame(root)
frame1.pack(side=TOP, pady=5) #, expand = YES, fill=BOTH
#тут нужно задать размер фрейма
frame2 = Frame(root)
frame2.pack(side=LEFT,anchor=N, pady=5)
frame4 = Frame(root)
frame4.pack(side=BOTTOM,anchor=S, pady=5)
frame3 = Frame(root)
frame3.pack(side=RIGHT,anchor=N)



text1=Text(frame1, height=1,width=20,font='Arial 20', wrap=WORD)
text1.pack(side=RIGHT, anchor=N)

#Кнопки цифр от 7 до 9
b_7 = Button(frame2, text='7')
b_7.grid(row =1, column = 1)
b_8 = Button(frame2, text='8')
b_8.grid(row =1, column = 2)
b_9 = Button(frame2, text='9')
b_9.grid(row =1, column = 3)

#Кнопки цифр от 4 до 6
b_4 = Button(frame2, text='4')
b_4.grid(row =2, column = 1)
b_5 = Button(frame2, text='5')
b_5.grid(row =2, column = 2)
b_6 = Button(frame2, text='6')
b_6.grid(row =2, column = 3)

#Кнопки цифр от 1 до 3
b_1 = Button(frame2, text='1')
b_1.grid(row =3, column = 1)
b_2 = Button(frame2, text='2')
b_2.grid(row =3, column = 2)
b_3 = Button(frame2, text='3')
b_3.grid(row =3, column = 3)

#Кнопки действий
b_plas = Button(frame3, text='+')
b_plas.pack(side=TOP, anchor=N)

root.mainloop()