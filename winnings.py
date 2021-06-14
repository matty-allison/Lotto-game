from tkinter import *
from tkinter import messagebox

block = Tk()
block.title("HOPE YOU HAD FUN!")
block.geometry("500x300")
block.config(bg="yellow")
class Winnings:
    def __init__(self, master):
        self.set = Label(master, text="10 20 30 40 50 60")
        self.set.place(x=50, y=30)
        self.set.config(bg='yellow', font="200")
        self.set2 = Label(master, text="10 20 30 40 50 60")
        self.set2.place(x=50, y=70)
        self.set2.config(bg='yellow', font="200")
        self.set3 = Label(master, text="10 20 30 40 50 60")
        self.set3.place(x=50, y=120)
        self.set3.config(bg='yellow', font="200")
        self.winningset = Label(master, text="10 20 30 40 50 60")
        self.winningset.place(x=280, y=30)
        self.winningset.config(bg='yellow', font=("bold", 15), fg="red")
        self.money = Label(master, text="You won: ")
        self.money.place(x=280, y=70)
        self.money.config(bg="yellow", font=("bold", 15))
        self.amount = Label(master, text="10, 000, 000.00")
        self.amount.place(x=280, y=120)
        self.amount.config(bg="yellow", font=("bold", 15))
        self.currency = Button(master, text="Convert?", command=self.currencyconverter)
        self.currency.place(x=280, y=170)
        self.currency.config(bg="orange", borderwidth="5")
        self.playagain = Button(master, text="Play again?!", command=self.play_again)
        self.playagain.place(x=80, y=170)
        self.playagain.config(bg="orange", borderwidth="5")
        self.claimprize = Button(master, text="Claim prize!!", command=self.claim_prize_money)
        self.claimprize.place(x=180, y=230)
        self.claimprize.config(bg="red", borderwidth="8")
    def currencyconverter(self):
        block.destroy()
        import currency_convert

    def play_again(self):
        block.destroy()
        import letsplaylotto

    def claim_prize_money(self):
        block.destroy()
        import end_window

x = Winnings(block)
block.mainloop()
