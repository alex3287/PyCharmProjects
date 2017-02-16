from tkinter import *

root =Tk()
root.geometry('400x300')
btn1 = Button(root, width =10, text = 'Test1')
btn1.pack(side='left')
btn2 = Button(root, width =10, text = 'Test2')
btn2.pack(side='top')
text = Entry(root, width=50)
text.pack()
btn3 = Button(root, width =10, text = 'Test2')
btn3.pack()
mainloop()