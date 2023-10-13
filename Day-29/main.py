from tkinter import *
from tkinter import messagebox
import random
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img_lock = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=img_lock)
canvas.grid(row=0, column=1)


# Password Generator

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
               'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# Functionality
def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(password_data) == 0:

        messagebox.showwarning(title="Error Found", message="You did not fill Website or Password")

    else:

        message = messagebox.askokcancel(title="Submit Request", message=f"These are the details entered for\n"
                                                                         f"{website_data}\n\nEmail: {email_data}\n"
                                                                         f"Password: {password_data}")
        if message:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website_data} | {email_data} | {password_data}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# lavel
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entry
website_entry = Entry(width=38)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "mridulroy010@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
btn_password = Button(text="Generate Password", command=generate_password)
btn_password.grid(row=3, column=2)
btn_add = Button(text="Add", width=36, command=save)
btn_add.grid(row=4, column=1, columnspan=2)

window.mainloop()