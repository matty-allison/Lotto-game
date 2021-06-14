#Matthew Allison Class 2
from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("600x700")
root.title("Welcome to the lotto")
root.config(bg="yellow")
class SignUp:
    canvas = Canvas(root, width=300, height=300)
    canvas.place(x=150, y=10)
    img = PhotoImage(file="lotto-pic.png")
    canvas.create_image(150, 150, image=img)
    def __init__(self, master):
        self.label_name = Label(master, text="Enter your name: ")
        self.label_name.place(x=120, y=350)
        self.label_name.config(bg='yellow',  font="200")
        self.enter_name = Entry(master)
        self.enter_name.place(x=300, y=350)
        self.enter_name.config(width="25")
        self.label_email = Label(master, text="Enter your email: ")
        self.label_email.place(x=120, y=400)
        self.label_email.config(bg="yellow", font="200")
        self.enter_email = Entry(master)
        self.enter_email.place(x=300, y=400)
        self.enter_email.config(width="25")
        self.label_idnumber = Label(master, text="Enter ID number: ")
        self.label_idnumber.place(x=120, y=450)
        self.label_idnumber.config(bg="yellow", font="200")
        self.enter_idnumber = Entry(master)
        self.enter_idnumber.place(x=300, y=450)
        self.enter_idnumber.config(width="25")
        self.signup_button = Button(master, text="sign up", command=self.signin_button)
        self.signup_button.config(bg="orange", borderwidth="10")
        self.signup_button.place(x=250, y=500)
        self.label_login = Label(master, text="already have a account?")
        self.label_login.place(x=300, y=650)
        self.label_login.config(bg="yellow", font="200")
        self.login_button = Button(master, text="log in", command=self.log_button)
        self.login_button.place(x=510, y=640)
        self.login_button.config(bg="orange", borderwidth="5")

    def signin_button(self):
        root.destroy()
        import letsplaylotto


    def log_button(self):
        root.destroy()
        import login_form

x = SignUp(root)
root.mainloop()

