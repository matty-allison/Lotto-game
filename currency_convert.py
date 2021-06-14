from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

space = Tk()
space.title("Curency Converter")
space.geometry("500x200")
space.config(bg="yellow")

response = requests.get("https://v6.exchangerate-api.com/v6/a24d5559a57a8ed22b9fd2a0/latest/USD")
data = response.json()
class Currency_converter:
    def __init__(self, master):
        self.amount = Label(master, text="R10, 000, 000.00")
        self.amount.place(x=30, y=70)
        self.amount.config(bg="yellow", font=("bold", 15))
        self.arrow = Label(master, text="-->")
        self.arrow.place(x=230, y=70)
        self.arrow.config(bg="yellow", font=("bold", 15))
        self.converted = Label(master, text="$130, 000, 000.00")
        self.converted.place(x=280, y=70)
        self.converted.config(bg="yellow", font=("bold", 15))
        self.countries = ttk.Combobox(master, values=list(data['conversion_rates'].values()))
        self.countries.place(x=150, y=20)


x = Currency_converter(space)
space.mainloop()
