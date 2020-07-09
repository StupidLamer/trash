from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import os
from datetime import datetime


def choose_dir():
    dir_path = filedialog.askdirectory()
    e_path.delete(0, END)
    e_path.insert(0, dir_path)


def f_start():
    cur_path = e_path.get()
    if cur_path:
        for folder, sub_folder, files in os.walk(cur_path):
            for file in files:
                path = os.path.join(folder, file)
                mtime = os.path.getmtime(path)
                date = datetime.fromtimestamp(mtime)
                date = date.strftime('%Y-%m-%d')
                date_folder = os.path.join(cur_path, date)
                if not os.path.exists(date_folder):
                    os.mkdir(date_folder)
                os.rename(path, os.path.join(date_folder, file))
        messagebox.showinfo('Success', 'Files were sorted')
        e_path.delete(0, END)
    else:
        messagebox.showwarning('Warining', 'Select folder')


root = Tk()
root.title('PhotoSort')
root.geometry('300x100')

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 15))

frame = Frame(root, bg='#56adff', bd=5)
frame.pack(padx=10, pady=10, fill=X)

e_path = ttk.Entry(frame)
e_path.pack(side=LEFT, expand=1, ipady=2, fill=X)

btn_dialog = ttk.Button(frame, text='Select folder', command=choose_dir)
btn_dialog.pack(side=LEFT, padx=5)

btn_start = ttk.Button(root, style='my.TButton', text='Start', command=f_start)
btn_start.pack(fill=X, padx=10)

root.mainloop()

