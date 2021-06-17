#Matthew Allison Class 2
from tkinter import *
import rsaidnumber
import re
from datetime import date, datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
    id_answer = StringVar()
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
        self.enter_idnumber = Entry(master, textvariable=self.id_answer)
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
        email_invalid = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
        player_info = open('textfile.txt', 'a')
        senders_email = "mattymallison@gmail.com"
        receivers_email = self.enter_email.get()
        password = "Mallison18$"
        try:
            for i in range(len(self.enter_email.get())):
                if re.search(email_invalid, self.enter_email.get()):
                    player_ID = self.enter_name.get().strip() + self.enter_idnumber.get()[:2]
                    subject = "Hello Player"
                    msg = MIMEMultipart()
                    msg["From"] = senders_email
                    msg["To"] = receivers_email
                    msg["Subject"] = subject

                    message = ("this is your unique player ID: " + str(player_ID))
                    message = message
                    msg.attach(MIMEText(message, 'plain'))
                    text = msg.as_string()
                    s = smtplib.SMTP("smtp.gmail.com", 587)

                    s.starttls()

                    s.login(senders_email, password)
                    s.sendmail(senders_email, receivers_email, text)
                    s.quit()

                    player_info.write("Username: " + self.enter_name.get())
                    player_info.write('\n')
                    player_info.write("Email: " + self.enter_email.get())
                    player_info.write('\n')
                    player_info.write("Id Number: " + self.enter_idnumber.get())
                    player_info.write('\n')
                    player_info.write("Player ID: " + player_ID)
                    player_info.write('\n')
                else:
                    messagebox.showerror('STATUS', "Invalid email")
                    break
                id_number = rsaidnumber.parse(self.enter_idnumber.get())
                age = (datetime.today() - id_number.date_of_birth) // timedelta(days=365.245)
                self.id_answer.set(age)
                player_info.write("Age:" + str(age))
                player_info.write('\n')

                if age < 18:
                    messagebox.showerror('STATUS', "No enter")
                elif age >= 18:
                    messagebox.showinfo('STATUS', "Let's play")
                    root.destroy()
                    import letsplaylotto
        except ValueError:
            if self.enter_idnumber.get() != int:
                messagebox.showerror('STATUS', "invalid")
        finally:
            player_info.close()

    def log_button(self):
        root.destroy()
        import login_form

x = SignUp(root)
root.mainloop()

