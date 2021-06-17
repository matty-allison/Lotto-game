#Matthew Allison Class 2
from tkinter import *

window = Tk()
window.title("Log in")
window.geometry("500x350")
window.config(bg="yellow")
class LogIn:
    def __init__(self, master):
        self.label_name = Label(master, text="Enter your name: ")
        self.label_name.place(x=180, y=50)
        self.label_name.config(bg="yellow", font="200")
        self.enter_name = Entry(master)
        self.enter_name.place(x=170, y=80)
        self.enter_name.config(width="20")
        self.label_playerid = Label(master, text="Enter your unique player ID")
        self.label_playerid.place(x=150, y=150)
        self.label_playerid.config(bg="yellow", font="200")
        self.enter_playerid = Entry(master)
        self.enter_playerid.place(x=170, y=180)
        self.login_button = Button(master, text="Log in", command=self.welcomeback)
        self.login_button.config(bg="orange", borderwidth="10")
        self.login_button.place(x=210, y=240)
        self.back = Button(master, text="back", command=self.backbutton)
        self.back.place(x=10, y=300)
        self.back.config(bg="orange", borderwidth="5")

    def welcomeback(self):
        window.destroy()
        import letsplaylotto

    def backbutton(self):
        window.destroy()
        import Sign_up_form

x = LogIn(window)
window.mainloop()
