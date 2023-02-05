import json
from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip
import json



FONT = "Arial", 14


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list  = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)


    input_password.insert(0, password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Missing value", message="Er ontbreken nog gegevens")
    else:
        try:
            with open("data.json", "r") as data_file:  # a = append
                # reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(new_data, data_file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            input_website.delete(0, END)
            input_password.delete(0, END)



def search():
    website = input_website.get()
    if website == "":
        messagebox.showinfo(title="Missing value", message="Vul website in")

    try:
        with open("data.json", "r") as data_file:  # a = append
            # reading old data
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"There are no details foor {website}")

        # for site in data:
        #     if site == website:
        #         print(data.get(site).get("password"))
        #         messagebox.showinfo(title="Password",
        #                             message=f"website: {site}\nPassword: {data.get(site).get('password')}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.minsize(600, 400)
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
image_slot = PhotoImage(file="logo.png",)
canvas.create_image(100, 100,image= image_slot )

canvas.grid(column=1, row=0)

label_website = Label(text="Website: ", fg= "Black", font=(FONT))
label_website.grid(column=0, row=1, sticky="e")

input_website = Entry(width=21, font=(FONT))
input_website.grid(column=1, row= 1)
input_website.focus()

label_username = Label(text="Email/Username: ", fg= "Black", font=(FONT), pady= 2)
label_username.grid(column=0, row=2)

input_email = Entry(width=35, font=(FONT))
input_email.grid(column=1, row= 2, columnspan=2, pady= 2)
input_email.insert(0, "kvanwijk@akemo.nl") # als je index END gebruikt dan voer je in aan het eind van de text.

label_password = Label(text="Password: ", fg= "Black", font=(FONT))
label_password.grid(column=0, row=3, pady= 2, sticky="e")

input_password = Entry(width=21, font=(FONT))
input_password.grid(column=1, row= 3, pady= 2)

button_search = Button(text="Search", command=search, font=("Arial", 10))
button_search.config(width=18)
button_search.grid(column=2, row=1, )

button_generate = Button(text="Generate password", command=gen_password, font=("Arial", 10))
button_generate.config(width=18)
button_generate.grid(column=2, row=3, )

button_add = Button(text="add", command=add, font=("Arial", 10))
button_add.config(width=48)
button_add.grid(column=1, row=4, columnspan=3, pady= 2)







window.mainloop()