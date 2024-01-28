from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=image)
canvas.grid(row=0, column=1)

# website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

# website_text_entry
website_entry = Entry()


username_label = Label(text="Email/Username")
username_label.grid(row=2, column=0)

window.mainloop()
