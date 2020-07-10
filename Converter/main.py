from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import urllib.request
import json

root = Tk()
root.title('Currency Converter')
root.geometry('300x250')
root.resizable(False, False)

START_AMOUNT = 1000

# Funcs
def exchange():
    e_usd.delete(0, END)
    e_eur.delete(0, END)
    try:
        e_usd.insert(0, round(float(e_rub.get()) / float(JSON_object['Valute']['USD']['Previous']), 2))
        e_eur.insert(0, round(float(e_rub.get()) / float(JSON_object['Valute']['EUR']['Previous']), 2))
    except:
        messagebox.showerror('Error', 'Enter correct value!')


try:
    html = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
    data = html.read()
    JSON_object = json.loads(data)
except:
    messagebox.showerror('Error', 'Check your Internet')

# Header frame
header_frame = Frame(root)
header_frame.pack(fill=X)
header_frame.grid_columnconfigure(0, weight=1)
header_frame.grid_columnconfigure(1, weight=1)
header_frame.grid_columnconfigure(2, weight=1)

#Header
h_currency = Label(header_frame, text='Currency', bg='#ccc', font='Arial 12 bold')
h_currency.grid(row=0, column=0, sticky=EW)
h_buy = Label(header_frame, text='Buying', bg='#ccc', font='Arial 12 bold')
h_buy.grid(row=0, column=1, sticky=EW)
h_sale = Label(header_frame, text='Sale', bg='#ccc', font='Arial 12 bold')
h_sale.grid(row=0, column=2, sticky=EW)

# USD course
usd_currency = Label(header_frame, text='USD', font='Arial 10')
usd_currency.grid(row=1, column=0, sticky=EW)
usd_buy = Label(header_frame, text=JSON_object['Valute']['USD']['Value'], font='Arial 10')
usd_buy.grid(row=1, column=1, sticky=EW)
usd_sale = Label(header_frame, text=JSON_object['Valute']['USD']['Previous'], font='Arial 10')
usd_sale.grid(row=1, column=2, sticky=EW)

# EUR course
eur_currency = Label(header_frame, text='EUR', bg='#ccc', font='Arial 10')
eur_currency.grid(row=2, column=0, sticky=EW)
eur_buy = Label(header_frame, text=JSON_object['Valute']['EUR']['Value'], bg='#ccc', font='Arial 10')
eur_buy.grid(row=2, column=1, sticky=EW)
eur_sale = Label(header_frame, text=JSON_object['Valute']['EUR']['Previous'], bg='#ccc', font='Arial 10')
eur_sale.grid(row=2, column=2, sticky=EW)

# Calc frame
calc_frame = Frame(root, bg='#fff')
calc_frame.pack(expand=1, fill=BOTH)
calc_frame.grid_columnconfigure(1, weight=1)

#RUB
l_rub = Label(calc_frame, text='Rubbles: ', bg='#fff', font='Arial 10 bold')
l_rub.grid(row=0, column=0, padx=10)
e_rub = ttk.Entry(calc_frame, justify=CENTER, font='Arial 10')
e_rub.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky=EW)
e_rub.insert(0, START_AMOUNT)

#Button
btn_calc = ttk.Button(calc_frame, text='Exchange', command=exchange)
btn_calc.grid(row=1, column=1, columnspan=2, sticky=EW, padx=10)

#Result frame
res_frame = Frame(root)
res_frame.pack(expand=1, fill=BOTH, pady=5)
res_frame.grid_columnconfigure(1, weight=1)

#USD
l_usd = Label(res_frame, text='USD: ', font='Arial 10 bold')
l_usd.grid(row=2, column=0)
e_usd = ttk.Entry(res_frame, justify=CENTER, font='Arial 10')
e_usd.grid(row=2, column=1, columnspan=2, padx=10, sticky=EW)
e_usd.insert(0, round(START_AMOUNT / float(JSON_object['Valute']['USD']['Previous']), 2))

#EUR
l_eur = Label(res_frame, text='EUR: ', font='Arial 10 bold')
l_eur.grid(row=3, column=0)
e_eur = ttk.Entry(res_frame, justify=CENTER, font='Arial 10')
e_eur.grid(row=3, column=1, columnspan=2, padx=10, sticky=EW)
e_eur.insert(0, round(START_AMOUNT / float(JSON_object['Valute']['EUR']['Previous']), 2))

root.mainloop()