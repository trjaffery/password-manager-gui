from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r',
               's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
               'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]
    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]
    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    password = password_entry.get()
    username = email_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showerror("Missing fields", "Please fill each field")
    else:
        try:
            with open("logins.json", "r") as file:
                # reading old data
                data = json.load(file)
                # updating old data with new data
                data.update(new_data)
        except FileNotFoundError:
            with open("logins.json", "w") as file:
                # saving data
                json.dump(new_data, file, indent=4)
        else:
            with open("logins.json", "w") as file:
                # saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().lower()
    if website == "":
        messagebox.showerror("Missing fields", "Please enter the website you are searching for!")
    else:
        try:
            with open("logins.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror("File Not Found", "You have not saved any login data!")
            website_entry.delete(0, END)
        else:
            if website in data:
                messagebox.showinfo(f"{website.title()} Login Information",
                                    f"Username: {data[website]['username']}\nPassword: "
                                    f"{data[website]['password']}")
            else:
                messagebox.showerror("Website Not Found", "No website found with that name!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# website_text_entry
website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, sticky="EW")
website_entry.focus()

# search button
search_button = Button(text="Search", command=find_password, width=13)
search_button.grid(row=1, column=2)

# user_name label
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

# email/user_name entry
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")

# password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# password entry
password_entry = Entry(width=18)
password_entry.grid(row=3, column=1, sticky="EW")

# password button
password_button = Button(text="Generate Password", width=14, command=generate_password)
password_button.grid(row=3, column=2, sticky="EW")

# add button
add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
