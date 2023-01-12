from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    char_list = [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    sym_list = [random.choice(symbols) for sym in range(nr_symbols)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    num_list = [random.choice(numbers) for num in range(nr_numbers)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    password_list = char_list + sym_list + num_list

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field blank!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}"
                                                      f"\n Is this ok to save?")
        if is_ok:
            x = open('data.txt', "a")
            x.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            x.close()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=0)

website_entry = Entry(width=35)
website_entry.grid(column=2, row=1, columnspan=2)
website_entry.focus()

website_label = Label(text="Website:")
website_label.grid(column=1, row=1)

email_entry = Entry(width=35)
email_entry.grid(column=2, row=2, columnspan=2)
email_entry.insert(0, "essienjustice@gmail.com")

email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=2)

password_entry = Entry(width=21)
password_entry.grid(column=2, row=3)

password_label = Label(text="Password:")
password_label.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=2, row=4, columnspan=2)


window.mainloop()