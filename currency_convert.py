#Matthew Allison class 2
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import requests

space = Tk()
space.title("Curency Converter")
space.geometry("500x200")
space.config(bg="yellow")

response = requests.get("https://v6.exchangerate-api.com/v6/a24d5559a57a8ed22b9fd2a0/latest/ZAR")
data = response.json()
conversion_rates = data['conversion_rates']

list1 = []
for i in conversion_rates.keys():
    list1.append(i)

a = StringVar()
b = StringVar()
c = StringVar()
class Currency_converter:
    def __init__(self, master):
        self.amount = Label(master)
        self.amount.place(x=30, y=70)
        self.amount.config(bg="yellow", font=("bold", 15))
        self.arrow = Label(master, text="-->")
        self.arrow.place(x=230, y=70)
        self.arrow.config(bg="yellow", font=("bold", 15))
        self.converted = Label(master, textvariable=a)
        self.converted.place(x=280, y=70)
        self.converted.config(bg="yellow", font=("bold", 15))
        self.countries = ttk.Combobox(master)
        self.countries['values'] = list1
        self.countries['state'] = 'readonly'
        self.countries.set('Select Country')
        self.countries.place(x=150, y=20)
        self.convert_button = Button(master, text="Convert", command=self.convertprize)
        self.convert_button.place(x=140, y=120)
        self.convert_button.config(bg="orange", borderwidth="5", font=("bold", 10))
        self.claim = Button(master, text="Claim Prize", command=self.finished)
        self.claim.place(x=240, y=120)
        self.claim.config(bg="red", font=("bold", 10), borderwidth="5", state="disabled")
        self.back = Button(master, text="Back", command=self.backup)
        self.back.place(x=5, y=165)
        self.back.config(bg="orange")
        with open('textfile.txt', 'r') as c:
            for l in c:
                if "winnings" in l:
                    self.amount.config(text=l[11:-1])
    def convert(self, to_currency, amount):
        converted_ammount = round(amount / conversion_rates[to_currency], 4)
        return converted_ammount

    def convertprize(self):
        with open('textfile.txt', 'r') as c:
            for l in c:
                if "winnings" in l:
                    amounts = int(l[11:-1])
        if self.countries.get() == "ZAR":
            messagebox.showerror('STATUS', "Invalid, your prize is already in Rands")
        else:
            country = self.countries.get()
            after_convert = self.convert(country, amounts)
            a.set(after_convert)
            self.claim.config(state="normal")

    def backup(self):
        space.destroy()
        import letsplaylotto

    def finished(self):
        final_money = open('textfile.txt', 'a')
        final_money.write("winnings: " + str(a.get()))

        space.destroy()
        import end_window

x = Currency_converter(space)
space.mainloop()
