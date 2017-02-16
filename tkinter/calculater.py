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
frame3 = Frame(root)
frame3.pack(side=RIGHT,anchor=N)

text1=Text(frame1, height=1,width=20,font='Arial 20', wrap=WORD)
text1.pack(side=RIGHT, anchor=N)

#Кнопки цифр
b_7 = Button(frame2, text='7')
b_7.pack(side='left', padx=2)
b_8 = Button(frame2, text='8')
b_8.pack(side='left', padx=2)
b_9 = Button(frame2, text='9')
b_9.pack(side='left', padx=2)

lb = Label(text='***************************')
lb.pack(side='right')
b_4 = Button(frame2, text='4')
b_4.pack(side='left', padx=2 )
b_5 = Button(frame2, text='5')
b_5.pack(side='left', padx=2)
b_6 = Button(frame2, text='6')
b_6.pack(side='left', padx=2, )


#Кнопки действий
b_plas = Button(frame3, text='+')
b_plas.pack(side=TOP, anchor=N)

root.mainloop()