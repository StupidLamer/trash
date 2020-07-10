from tkinter import *
import time


def tick():
    watch.after(200, tick)
    watch['text'] = time.strftime('%H:%M:%S')

root = Tk()

watch = Label(root, font='Arial 70')
watch.pack()
tick()

root.mainloop()