from tkinter import *


def f_event(event, key):
    print(event)

root = Tk()
root.geometry('400x300')

e = Entry(root, justify=CENTER, font='Arial 15')
e.pack(fill=X, expand=1, padx=10, ipady=10)
e.bind(sequence='<Button-1>', func=lambda event, key='Left click': f_event(event, key))
e.bind(sequence='<Button-2>', func=lambda event, key='Middle click': f_event(event, key))
e.bind(sequence='<Button-3>', func=lambda event, key='Right click': f_event(event, key))

root.mainloop()