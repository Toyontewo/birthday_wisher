##################### Normal Starting Project ######################
import random
import smtplib
import datetime as dt

import pandas as pd

my_email = "samuelntw4lyf@gmail.com"
password = "gnhckbheebxeypxt"
to_email = "toyontewo@yahoo.com"

txt_files = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt","letter_templates/letter_3.txt"]


# HINT 2: Use pandas to read the birthdays.csv
birthday = pd.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
birthdays_dict = {
     (row["month"], row["day"]): row
     for _, row in birthday.iterrows()
 }
today = (dt.datetime.now().month, dt.datetime.now().day)

if today in birthdays_dict:
    row = birthdays_dict[today]
    with open(random.choice(txt_files), "r") as letter_file:
        content = letter_file.read()
    content = content.replace("[NAME]", row["name"])
#    with open("final_txt.txt", "w") as file:
#        file.write(content)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(from_addr=my_email, to_addrs=to_email, msg=f"Subject:Happy Birthday\n\n{content}")

