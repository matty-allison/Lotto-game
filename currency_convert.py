from tkinter import *
from tkinter import ttk
import requests

space = Tk()
space.title("Curency Converter")
space.geometry("500x200")
space.config(bg="yellow")

response = requests.get("https://v6.exchangerate-api.com/v6/a24d5559a57a8ed22b9fd2a0/latest/USD")
data = response.json()
conversion_rates = data['conversion_rates']

list1 = []
for i in conversion_rates.keys():
    list1.append(i)
class Currency_converter:
    def __init__(self, master):
        self.amount = Label(master, text="R10, 000, 000.00")
        self.amount.place(x=30, y=70)
        self.amount.config(bg="yellow", font=("bold", 15))
        self.arrow = Label(master, text="-->")
        self.arrow.place(x=230, y=70)
        self.arrow.config(bg="yellow", font=("bold", 15))
        self.converted = Label(master, text="$727, 047.50")
        self.converted.place(x=280, y=70)
        self.converted.config(bg="yellow", font=("bold", 15))
        self.countries = ttk.Combobox(master, values=list1)
        self.countries.place(x=150, y=20)
        self.convert_button = Button(master, text="Convert")
        self.convert_button.place(x=140, y=120)
        self.convert_button.config(bg="orange", borderwidth="5", font=("bold", 10))
        self.claim = Button(master, text="Claim Prize", command=self.finished)
        self.claim.place(x=240, y=120)
        self.claim.config(bg="red", font=("bold", 10), borderwidth="5")
        self.back = Button(master, text="Back", command=self.backup)
        self.back.place(x=5, y=165)
        self.back.config(bg="orange")
    def backup(self):
        space.destroy()
        import letsplaylotto

    def finished(self):
        space.destroy()
        import end_window

x = Currency_converter(space)
space.mainloop()
