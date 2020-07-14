from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter import messagebox
import requests
import time

API_KEY = 'f205f7195b7c98bca16670b7c205bc49'
API_URL = 'https://api.openweathermap.org/data/2.5/weather'


def print_weather(weather):
    try:
        city = weather['name']
        country = weather['sys']['country']
        temp = weather['main']['temp']
        press = weather['main']['pressure']
        humidity = weather['main']['humidity']
        wind = weather['wind']['speed']
        desc = weather['weather'][0]['description']
        sunrise_ts = weather['sys']['sunrise']
        sunset_ts = weather['sys']['sunset']
        sunrise_struct_time = time.localtime(sunrise_ts)
        sunset_struct_time = time.localtime(sunset_ts)
        sunrise = time.strftime('%H:%M:%S', sunrise_struct_time)
        sunset = time.strftime('%H:%M:%S', sunset_struct_time)
        return f'Place: {city}, {country} \nTemperature: {temp} Celcies \nPressure: \
    {press} gPa \nHumidity: {humidity}% \nWind speed: {wind} m/s \nWeather: {desc} \
    \nSunrise: {sunrise} \nSunset: {sunset}'
    except:
        return 'Error get data'



def get_weather(event=''):
    if not entry.get():
        messagebox.showwarning('Warning', 'Enter request')
    else:
        params = {
            'appid': API_KEY,
            'q': entry.get(),
            'units': 'metric',
            'lang': 'ru'
        }
        r = requests.get(API_URL, params=params)
        weather = r.json()
        label['text'] = print_weather(weather)


root = ThemedTk(theme='arc')
root.geometry('500x400')
root.resizable(0, 0)

s = ttk.Style()
s.configure('TLabel', padding=5, font='Arial 11')

top_frame = ttk.Frame(root)
top_frame.place(relx=0.5, rely=0.1, relwidth=0.9, relheight=0.1, anchor='n')

entry = ttk.Entry(top_frame)
entry.place(relwidth=0.7, relheight=1)
entry.bind('<Return>', get_weather)

button = ttk.Button(top_frame, text='Get weather', command=get_weather)
button.place(relwidth=0.3, relx=0.7, relheight=1)

low_frame = ttk.Frame(root)
low_frame.place(relx=0.5, rely=0.25, relwidth=0.9, relheight=0.6, anchor='n')

label = ttk.Label(low_frame, anchor='nw')
label.place(relwidth=1, relheight=1)

root.mainloop()
