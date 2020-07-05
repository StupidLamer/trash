from tkinter import *

root = Tk()
root.geometry('600x480')

# l1 = Label(root, text='Hello world!', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# l1.place(x=0, y=0)
#
# l2 = Label(root, text='Hello world!', bg='#2ecc71', fg='#fff', font='16', padx=20, pady=8)
# l2.place(relx=.5, rely=.5, anchor='c')

# btn1 = Button(text='Button 1', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# btn1.place(x=0, y=0)
#
# btn2 = Button(text='Button 2', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# btn2.place(relx=0.5, rely=0.5, anchor=CENTER)
#
# btn3 = Button(text='Button 3', bg='#3498db', fg='#fff', font='16', padx=20, pady=8)
# btn3.place(relx=1, rely=1, anchor=SE)

l1 = Label(root, bg='#000')
l1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

root.mainloop()