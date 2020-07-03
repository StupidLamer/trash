from tkinter import *

def add_str():
    e.insert(END, 'Hello!')

def del_str():
    e.delete(0, END)

def get_str():
    l_text['text'] = e.get()

root = Tk()
root.title('Counter')
root.iconbitmap('icon.ico')
root.geometry('600x400+300+100')

l = Label(root, text='Enter place')
l.pack()

e = Entry(root, show='*')
e.insert(0, 'Hello')
e.insert(END, ' world')
e.pack()

btn_add = Button(root, text='Add', command=add_str).pack()
btn_del = Button(root, text='Delete', command=del_str).pack()
btn_get = Button(root, text='Get', command=get_str).pack()

l_text = Label(root, bg='blue')
l_text.pack(fill=X)

root.mainloop()
