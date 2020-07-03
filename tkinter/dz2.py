from tkinter import *

root = Tk()
root.title('Rainbow')

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

class MyButtons():

    def __init__(self, master, text_color, hex_color):
        self.text_color = text_color
        self.hex_color = hex_color
        self.b = Button(root, bg=hex_color, command=self.get_color)
        self.b.pack(fill=X)

    def get_color(self):
        l['text'] = self.text_color
        e.delete(0, END)
        e.insert(0, self.hex_color)

for k, v in colors.items():
    MyButtons(root, v, k)

root.mainloop()