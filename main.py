import pandas
import smtplib
import datetime as dt
import random

my_email = "captainrogers3069@gmail.com"
password = "***************"

now = dt.datetime.now()
today_month = now.month
today = now.today().date().day

birthday = pandas.read_csv("birthdays.csv")
d = birthday.to_dict(orient="records")

letters = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
l = random.choice(letters)
letter = ""
for x in d:
    with open(l, "r") as let:
        f = let.readlines()
        f[0] = f[0].replace("[NAME]", x["name"])
    for y in f:
        letter += y

    if x["month"] == today_month:
        if x["day"] == today:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=x["email"], msg=f"Subject:Happy Birthday\n\n{letter}")
                connection.close()
