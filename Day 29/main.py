from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    uname = uname_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(uname) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Please don\'t leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n Username: {uname} \n'
                                                      f'Password: {password} \nIs it okay to save?')

        if is_ok:
            with open('data.txt', mode='a') as data:
                data.write(f'{website} | {uname} | {password}\n')

            website_entry.delete(0, END)
            uname_entry.delete(0, END)
            uname_entry.insert(0, 'davisburrill@icloud.com')
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
my_pass_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=my_pass_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

uname_label = Label(text='Email/Username:')
uname_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=37)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

uname_entry = Entry(width=37)
uname_entry.grid(column=1, row=2, columnspan=2)
uname_entry.insert(0, 'davisburrill@icloud.com')

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_button = Button(text='Generate Password', width=12, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
