from tkinter import *
from tkinter import messagebox

frame = Tk()
frame.title("Lotto")
frame.geometry("600x600")
frame.config(bg="yellow")

class PlayerLotto:
    canvas = Canvas(frame, width="300", height="155")
    canvas.place(x=140, y=10)
    img = PhotoImage(file="images.png")
    canvas.create_image(150, 79, image=img)

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
        self.label1 = Label(master, text="Select 6 numbers to make a set. (You can have 3 sets)")
        self.label1.place(x=100, y=250)
        self.label1.config(bg="yellow", font="200")
        self.set1 = Label(master, text="10 20 30 40 50 60")
        self.set1.place(x=150, y=350)
        self.set1.config(bg="orange", font="600")
        self.set2 = Label(master)
        self.set2.place(x=150, y=400)
        self.set2.config(bg="orange", font="600")
        self.set3 = Label(master)
        self.set3.place(x=150, y=450)
        self.set3.config(bg="orange", font="600")
        self.finished_set = Button(master, text="Finished set")
        self.finished_set.place(x=250, y=290)
        self.finished_set.config(bg="orange", borderwidth="5")
        self.start_lotto = Button(master, text="START LOTTO!!", command=self.runlotto)
        self.start_lotto.place(x=240, y=500)
        self.start_lotto.config(bg="red", borderwidth="10")

    def runlotto(self):
        frame.destroy()
        import winnings


x = PlayerLotto(frame)
frame.mainloop()
