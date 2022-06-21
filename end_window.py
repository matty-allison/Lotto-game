#Matthew Allison Class 2
from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tkinter import messagebox
from playsound import playsound

holder = Tk()
holder.title("Claim your prize!")
holder.geometry("550x360")
holder.config(bg="yellow")

class ClaimThePrize:
    def __init__(self,master):
        self.label1 = Label(master, text="Please enter your account number: ")
        self.label1.place(x=130, y=50)
        self.label1.config(bg="yellow", font="200")
        self.enter_account = Entry(master, bg="yellow", fg="black")
        self.enter_account.place(x=200, y=80)
        self.label2 = Label(master, text="Please enter the account holders name: ")
        self.label2.place(x=120, y=120)
        self.label2.config(bg="yellow", font="200")
        self.enter_account_name = Entry(master, bg="yellow", fg="black")
        self.enter_account_name.place(x=200, y=160)
        OptionList = ["FNB", "NEDBANK", "CAPITEC", "STANDARD BANK", "ABSA"]
        variable = StringVar(master)
        variable.set(OptionList[0])
        self.bank = OptionMenu(master, variable, *OptionList)
        self.bank.place(x=250, y=200)
        self.bank.config(bg="orange", borderwidth="5")
        self.submit = Button(master, text="Submit", command=self.final_email)
        self.submit.place(x=230, y=280)
        self.submit.config(bg="red", borderwidth="5", font=("bold", 15))

    def final_email(self):
        prize = 0
        if len(self.enter_account.get()) != 10:
            messagebox.showerror('STATUS', "Invalid account number")
        else:
            with open('textfile.txt', 'r') as c:
                for l in c:
                    if "Player ID" in l:
                        player_id = str(l[11:-1])
            with open('textfile.txt', 'r') as c:
                for l in c:
                    if "Email" in l:
                        email = str(l[7:-1])
            with open('textfile.txt', 'r') as c:
                for l in c:
                    if "winnings" in l:
                        prize = str(l[10:-1])
            senders_email = "mattymallison@gmail.com"
            receivers_email = email
            password = ""

            subject = "Thank you for playing Lotto"
            msg = MIMEMultipart()
            msg["From"] = senders_email
            msg["To"] = receivers_email
            msg["Subject"] = subject
            message = ("Thank for playing lotto we hope you enjoyed your time, here are your banking info and your winnings(obviously this is not really but its fun isn't it), we hope you come again: " + self.enter_account_name.get() + self.enter_account.get() + player_id + prize)
            message = message
            msg.attach(MIMEText(message, 'plain'))
            text = msg.as_string()
            s = smtplib.SMTP("smtp.gmail.com", 587)

            s.starttls()

            s.login(senders_email, password)
            s.sendmail(senders_email, receivers_email, text)
            s.quit()
            messagebox.showinfo('STATUS', "Thank you for playing, PLease check your email for your prize!!")
            playsound("sound effectGOODBYE.mp3")
            holder.destroy()


x = ClaimThePrize(holder)
holder.mainloop()
