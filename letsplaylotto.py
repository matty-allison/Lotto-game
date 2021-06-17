#Matthew Allison class 2
from tkinter import *
from tkinter import messagebox
import random

frame = Tk()
frame.title("Lotto")
frame.geometry("600x600")
frame.config(bg="yellow")

class PlayerLotto:
    canvas = Canvas(frame, width="300", height="155")
    canvas.place(x=140, y=10)
    img = PhotoImage(file="images.png")
    canvas.create_image(150, 79, image=img)
    numberlist1 = StringVar()
    numberlist2 = StringVar()
    numberlist3 = StringVar()
    list1 = StringVar()
    list2 = StringVar()
    list3 = StringVar()
    def __init__(self,master):
        self.spinbox1 = Spinbox(master, width=5, from_=0, to=49)
        self.spinbox1.place(x=70, y=200)
        self.spinbox1.config(bg="orange", borderwidth="5")
        self.spinbox2 = Spinbox(master, width=5, from_=0, to=49)
        self.spinbox2.place(x=150, y=200)
        self.spinbox2.config(bg="orange", borderwidth="5")
        self.spinbox3 = Spinbox(master, width=5, from_=0, to=49)
        self.spinbox3.place(x=230, y=200)
        self.spinbox3.config(bg="orange", borderwidth="5")
        self.spinbox4 = Spinbox(master, width=5, from_=0, to=49)
        self.spinbox4.place(x=310, y=200)
        self.spinbox4.config(bg="orange", borderwidth="5")
        self.spinbox5 = Spinbox(master, width=5, from_=0, to=49)
        self.spinbox5.place(x=390, y=200)
        self.spinbox5.config(bg="orange", borderwidth="5")
        self.spinbox6 = Spinbox(master, width=5, from_=0, to=49)
        self.spinbox6.place(x=470, y=200)
        self.spinbox6.config(bg="orange", borderwidth="5")
        self.label1 = Label(master, text="Select 6 numbers to make a set. (the limit is 49)")
        self.label1.place(x=120, y=250)
        self.label1.config(bg="yellow", font="200")
        self.set1 = Label(master, textvariable=self.list1)
        self.set1.place(x=50, y=350)
        self.numberlist1 = []
        self.set1.config(bg="yellow", font="600")
        self.set2 = Label(master, textvariable=self.list2)
        self.set2.place(x=50, y=400)
        self.numberlist2 = []
        self.set2.config(bg="yellow", font="600")
        self.set3 = Label(master, textvariable=self.list3)
        self.set3.place(x=50, y=450)
        self.numberlist3 = []
        self.set3.config(bg="yellow", font="600")
        self.finished_set1 = Button(master, text="Set 1", command=self.set_1)
        self.finished_set1.place(x=150, y=290)
        self.finished_set1.config(bg="orange", borderwidth="5")
        self.finished_set2 = Button(master, text="Set 2", command=self.set_2)
        self.finished_set2.place(x=250, y=290)
        self.finished_set2.config(bg="orange", borderwidth="5")
        self.finished_set3 = Button(master, text="Set 3", command=self.set_3)
        self.finished_set3.place(x=350, y=290)
        self.finished_set3.config(bg="orange", borderwidth="5")
        self.start_lotto = Button(master, text="START LOTTO!!", command=self.winnings)
        self.start_lotto.place(x=220, y=500)
        self.start_lotto.config(bg="red", borderwidth="10")
        self.amount = Label(master)
        self.amount.place(x=350, y=400)
        self.amount.config(bg="yellow", font=("bold", 15))
        self.currency = Button(master, text="Convert?")
        self.currency.place(x=350, y=450)
        self.currency.config(bg="orange", borderwidth="5")
        self.playagain = Button(master, text="Play again?!", command=self.clr)
        self.playagain.place(x=80, y=500)
        self.playagain.config(bg="orange", borderwidth="5")
        self.claimprize = Button(master, text="Claim prize!!")
        self.claimprize.place(x=385, y=500)
        self.claimprize.config(bg="red", borderwidth="5")
        self.winningset = Label(master)
        self.winningset.place(x=350, y=350)
        self.winningset.config(bg='yellow', font=("bold", 15), fg="red")

    def winnings(self):
        winning_set = random.sample(range(1, 49), 6)
        self.winningset.config(text=winning_set)
        if self.list1.get() == self.winningset:
            self.amount.config(text="YOU WIN")
        else:
            self.amount.config(text="YOU LOSE")

    def set_1(self):
        the_set = self.spinbox1.get() + self.spinbox2.get() + self.spinbox3.get() + self.spinbox4.get() + self.spinbox5.get() + self.spinbox6.get()
        try:
            """
            self.numberlist1.append(int(self.spinbox1.get()))
            self.numberlist1.append(int(self.spinbox2.get()))
            self.numberlist1.append(int(self.spinbox3.get()))
            self.numberlist1.append(int(self.spinbox4.get()))
            self.numberlist1.append(int(self.spinbox5.get()))
            self.numberlist1.append(int(self.spinbox6.get()))
            """
            if int(self.spinbox1.get()) <= 49:
                self.numberlist1.append(int(self.spinbox1.get()))
            elif int(self.spinbox1.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox2.get()) <= 49:
                self.numberlist1.append(int(self.spinbox2.get()))
            elif int(self.spinbox2.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox3.get()) <= 49:
                self.numberlist1.append(int(self.spinbox3.get()))
            elif int(self.spinbox3.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox4.get()) <= 49:
                self.numberlist1.append(int(self.spinbox4.get()))
            elif int(self.spinbox4.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox5.get()) <= 49:
                self.numberlist1.append(int(self.spinbox5.get()))
            elif int(self.spinbox5.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox6.get()) <= 49:
                self.numberlist1.append(int(self.spinbox6.get()))
            elif int(self.spinbox6.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if self.spinbox1.get() == self.spinbox2.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox3.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox4.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox3.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox4.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox3.get() == self.spinbox4.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox3.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox3.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox4.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox4.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox5.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")

            self.list1.set(self.numberlist1)
        except ValueError:
            if the_set != int:
                messagebox.showerror('STATUS', "Invalid")
        self.finished_set1.config(state="disabled")

    def set_2(self):
        the_set = self.spinbox1.get() + self.spinbox2.get() + self.spinbox3.get() + self.spinbox4.get() + self.spinbox5.get() + self.spinbox6.get()
        try:
            if int(self.spinbox1.get()) <= 49:
                self.numberlist2.append(int(self.spinbox1.get()))
            elif int(self.spinbox1.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox2.get()) <= 49:
                self.numberlist2.append(int(self.spinbox2.get()))
            elif int(self.spinbox2.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox3.get()) <= 49:
                self.numberlist2.append(int(self.spinbox3.get()))
            elif int(self.spinbox3.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox4.get()) <= 49:
                self.numberlist2.append(int(self.spinbox4.get()))
            elif int(self.spinbox4.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox5.get()) <= 49:
                self.numberlist2.append(int(self.spinbox5.get()))
            elif int(self.spinbox5.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox6.get()) <= 49:
                self.numberlist2.append(int(self.spinbox6.get()))
            elif int(self.spinbox6.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if self.spinbox1.get() == self.spinbox2.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox3.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox4.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox3.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox4.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox3.get() == self.spinbox4.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox3.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox3.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox4.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox4.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox5.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")

            self.list2.set(self.numberlist2)
        except ValueError:
            if the_set != int:
                messagebox.showerror('STATUS', "Invalid")
        self.finished_set2.config(state="disabled")

    def set_3(self):
        the_set = self.spinbox1.get() + self.spinbox2.get() + self.spinbox3.get() + self.spinbox4.get() + self.spinbox5.get() + self.spinbox6.get()
        try:
            if int(self.spinbox1.get()) <= 49:
                self.numberlist3.append(int(self.spinbox1.get()))
            elif int(self.spinbox1.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox2.get()) <= 49:
                self.numberlist3.append(int(self.spinbox2.get()))
            elif int(self.spinbox2.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox3.get()) <= 49:
                self.numberlist3.append(int(self.spinbox3.get()))
            elif int(self.spinbox3.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox4.get()) <= 49:
                self.numberlist3.append(int(self.spinbox4.get()))
            elif int(self.spinbox4.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox5.get()) <= 49:
                self.numberlist3.append(int(self.spinbox5.get()))
            elif int(self.spinbox5.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if int(self.spinbox6.get()) <= 49:
                self.numberlist3.append(int(self.spinbox6.get()))
            elif int(self.spinbox6.get()) > 49:
                messagebox.showerror('STATUS', "Invalid, numbers must be between 0 and 50")
            if self.spinbox1.get() == self.spinbox2.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox3.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox4.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox1.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox3.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox4.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox2.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox3.get() == self.spinbox4.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox3.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox3.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox4.get() == self.spinbox5.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox4.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")
            if self.spinbox5.get() == self.spinbox6.get():
                messagebox.showerror('STATUS', "Invalid, You can not have more than 1 of a number.")

            self.list3.set(self.numberlist3)
        except ValueError:
            if the_set != int:
                messagebox.showerror('STATUS', "Invalid")
        self.finished_set3.config(state="disabled")

    def clr(self):
        self.spinbox1.delete(0, END)
        self.spinbox2.delete(0, END)
        self.spinbox3.delete(0, END)
        self.spinbox4.delete(0, END)
        self.spinbox5.delete(0, END)
        self.spinbox6.delete(0, END)
        self.numberlist1.clear()
        self.numberlist2.clear()
        self.numberlist3.clear()
        self.set1.config(text="")
        self.set2.config(text="")
        self.set3.config(text="")
        self.finished_set1.config(state="normal")
        self.finished_set2.config(state="normal")
        self.finished_set3.config(state="normal")
        self.winningset.config(text="")
        self.amount.config(text="")

x = PlayerLotto(frame)
frame.mainloop()
