from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

    def final_email(self):
        senders_email = "mattymallison@gmail.com"
        receivers_email = self.enter_email.get()
        password = "Mallison18$"

        subject = "Thank you for playing Lotto"
        msg = MIMEMultipart()
        msg["From"] = senders_email
        msg["To"] = receivers_email
        msg["Subject"] = subject
        message =("Thank for playing lotto we hope you enjoyed your time here is your info and your winnings, do come again: " + self.enter_account_name.get() + self.enter_account.get() + + str(player_ID))
        message = message
        msg.attach(MIMEText(message, 'plain'))
        text = msg.as_string()
        s = smtplib.SMTP("smtp.gmail.com", 587)

        s.starttls()

        s.login(senders_email, password)
        s.sendmail(senders_email, receivers_email, text)
        s.quit()

x = ClaimThePrize(holder)
holder.mainloop()
