from tkinter import *

def get_color(text, hex):
    l['text'] = text
    e.delete(0, END)
    e.insert(0, hex)

root = Tk()
root.title('Rainbow')
# root.geometry('250x220')

l = Label(root)
l.pack()

e = Entry(root)
e.pack()

colors = {
    '#ff0000': 'RED',
    '#ff7d00': 'ORANGE',
    '#ffff00': 'YELLOW',
    '#00ff00': 'GREEN',
    '#007dff': 'CYAN',
    '#0000ff': 'BLUE',
    '#7d00ff': 'VIOLET'
}

for k, v in colors.items():
    Button(root, bg=k, command=lambda text=v, hex=k: get_color(text, hex)).pack(fill=X)

root.mainloop()