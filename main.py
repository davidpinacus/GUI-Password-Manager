from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

COLOUR="#CBB9D8"
FONT="Brass Mono Regular"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter=[choice(letters) for _ in range(randint(8,10))]
    password_number=[choice(numbers) for _ in range(randint(2,4))]
    password_symbol=[choice(symbols) for _ in range(randint(2,4))]

    password_list=password_letter+password_number+password_symbol
    shuffle(password_list)

    password="".join(password_list)
    password_section.insert(0,password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    
    website=website_section.get()
    email=email_section.get()
    password=password_section.get()
    if len(website)==0 or len(password)==0:
        messagebox.showwarning(title="Oop",message="Please don't leave any fields empty!")
    else:
        pop_up=messagebox.askokcancel(title=website,message=f"Email: {email}\nPassword: {password}\n\nClick OK To Save")
        if pop_up:
            with open("password_data.txt","a") as file:
                file.write(f"{website} | {email} | {password}\n")
                website_section.delete(0,END)
                password_section.delete(0,END)
    
# ---------------------------- UI SETUP ------------------------------- #

screen=Tk()
screen.title("Password Manager")
screen.config(padx=20,pady=20,bg=COLOUR,highlightthickness=0)

logo=PhotoImage(file="password.png")
logo_label=Label(image=logo,bg=COLOUR,highlightthickness=0)
logo_label.grid(row=0,column=0,columnspan=2,pady=20)
logo_label.image=logo

website_label=Label(text="Website:",font=(FONT,12,"bold"))
website_label.grid(row=1,column=0,sticky="e",padx=5,pady=10)
website_section=Entry(width=55,font=(FONT,10))
website_section.grid(row=1,column=1,sticky="w",padx=5,pady=10)
website_section.focus()

email_label=Label(text="Email/Username:",font=(FONT,12,"bold"))
email_label.grid(row=2,column=0,sticky="e",padx=5,pady=10)
email_section=Entry(width=55,font=(FONT,10,))
email_section.grid(row=2,column=1,sticky="w",padx=5,pady=10)
email_section.insert(0,"@gmail.com")

password_label=Label(text="Password:",font=(FONT,12,"bold"))
password_label.grid(row=3,column=0,sticky="e",padx=5,pady=10)
password_section=Entry(width=40,font=(FONT,10))
password_section.grid(row=3,column=1,sticky="w",padx=5,pady=10)

generate_button=Button(text="Generate",font=(FONT,10,"bold"),command=generate_password)
generate_button.grid(row=3,column=2,padx=5,pady=10)

add_button=Button(text="Add",font=(FONT,10,"bold"),width=55,command=save_password)
add_button.grid(row=4,column=1,padx=5,pady=10)

screen.mainloop()
