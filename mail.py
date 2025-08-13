from tkinter import *
from tkinter import messagebox
import smtplib

BACKGROUND_COLOR = "#876700"

my_email = "samuelntw4lyf@gmail.com"
password = "gnhckbheebxeypxt"


def clear_box():
    message_box.delete("1.0", "end")


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connect:
        connect.starttls()
        connect.login(user=my_email, password=password)
        message = message_box.get("1.0", "end-1c")
        connect.sendmail(from_addr=my_email, to_addrs=to_email.get(), msg=f"Subject:{subject.get()}\n\n{message}")
        messagebox.showinfo(title="Message sent", message=f"Message sent to {to_email.get()} successfully!")


window = Tk()
window.title("Email Sender")
window.config(pady=40, padx=40, bg=BACKGROUND_COLOR)
window.minsize(width=400, height=500)

intro_label = Label(text="Send email to:", highlightbackground=BACKGROUND_COLOR, bg=BACKGROUND_COLOR)
intro_label.config()
intro_label.grid(row=0, column=0, columnspan=2)

to_email = Entry(width=20)
to_email.grid(row=1, column=0, columnspan=2)

sub_txt = Label(text="Subject:", bg=BACKGROUND_COLOR)
sub_txt.grid(row=2, column=0, columnspan=2)

subject = Entry(width=20)
subject.grid(row=3, columnspan=2, column=0)

msg_label = Label(text="Message:", bg=BACKGROUND_COLOR)
msg_label.grid(row=4, column=0, columnspan=2)

message_box = Text(width=50, height=20, font=("Arial", 12))
message_box.config()
message_box.grid(row=5, columnspan=2, column=0, padx=10, pady=10)

clear_btn = Button(text="Clear", command=clear_box, highlightbackground=BACKGROUND_COLOR)
clear_btn.grid(row=6, column=0)

send_btn = Button(text="Send", command=send_mail, highlightbackground=BACKGROUND_COLOR)
send_btn.grid(row=6, column=1)

window.mainloop()
