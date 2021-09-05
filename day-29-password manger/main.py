from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT = ("Arial", 13)
FREQUENTLY_USED_EMAIL = "richie@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    
    # Copies password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_data = website_entry.get()
    email_data = email_username_entry.get()
    password_data = password_entry.get()

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty !")

    else:
        is_ok = messagebox.askokcancel(title=website_data,
                                       message=f"These are the details entered:\n Email: {email_data}\n"
                                               f" Password: {password_data}\n Is it OK to save?")

        if is_ok:
            with open(file="data.txt", mode="a") as df:
                df.write(f"{website_data} | {email_data} | {password_data}\n")

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=80, pady=80)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", font=FONT)
website_label.grid(column=0, row=1)

email_username_label = Label(text="Email/Username:", font=FONT)
email_username_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=FONT)
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=35, font=FONT)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()  # shows blinking cursor

email_username_entry = Entry(width=35, font=FONT)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, FREQUENTLY_USED_EMAIL)

password_entry = Entry(width=21, font=FONT)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", font=FONT, command=password_generator)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", font=FONT, width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
