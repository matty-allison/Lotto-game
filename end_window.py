from tkinter import *

holder = Tk()
holder.title("Claim your prize!")
holder.geometry("550x360")
holder.config(bg="yellow")

class ClaimThePrize:
    def __init__(self,master):
        self.label1 = Label(master, text="Please enter your account number: ")
        self.label1.place(x=130, y=50)
        self.label1.config(bg="yellow", font="200")
        self.enter_account = Entry(master)
        self.enter_account.place(x=200, y=80)
        self.label2 = Label(master, text="Please enter the account holders name: ")
        self.label2.place(x=120, y=120)
        self.label2.config(bg="yellow", font="200")
        self.enter_account_name = Entry(master)
        self.enter_account_name.place(x=200, y=160)
        OptionList = ["FNB", "NEDBANK", "CAPITEC", "STANDARD BANK", "ABSA"]
        variable = StringVar(master)
        variable.set(OptionList[0])
        self.bank = OptionMenu(master, variable, *OptionList)
        self.bank.place(x=250, y=200)
        self.bank.config(bg="orange", borderwidth="5")
        self.submit = Button(master, text="Submit")
        self.submit.place(x=230, y=280)
        self.submit.config(bg="red", borderwidth="5", font=("bold", 15))

x = ClaimThePrize(holder)
holder.mainloop()
