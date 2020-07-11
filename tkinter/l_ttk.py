from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x480')


def choose(event):
    print(select.current(), select.get())


s = ttk.Style()
s.theme_use('clam')
# s.configure('.', foreground='red')
s.configure('me.TButton', foreground='red', padding=6)

Button(root, text='Button 1', padx=40, pady=5).pack(pady=10)
ttk.Button(root, text='Button 2', width=21, style='me.TButton').pack()

Entry(root).pack(pady=10)
ttk.Entry(root).pack()

select = ttk.Combobox(root, values=['Jan', 'Fab', 'Mar', 'Apr'])
select.place(relx=.6, rely=.6, anchor=CENTER)
select.current(2)
select.bind('<<ComboboxSelected>>', choose)

root.mainloop()