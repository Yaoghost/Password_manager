from tkinter import messagebox
#------------------- SAVE PASSWORD ---------------------------------

def save():
    email = email_entry.get()
    password = password_entry.get()
    website_name = website_entry.get()
    data = [email, password, website_name]
    filed = 1
    for data in data:
        if len(data) == 0:
            messagebox.showerror(title="INFORMATIONS", message="Please don't leave any field empty")
            filed = 0
    if filed == 1:
        is_ok = messagebox.askokcancel(title=website_name, message= f"These are the informations you have entered: \nEmail: {email}\n Password: {password}")
    if is_ok:

        f = open(r"C:\Users\chris\Documents\passwordmanager.txt", "a")
        f.write(website_name +" | " + email + " | " + password + "\n")
        f.close()
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        email_entry.delete(0, END)

#-------------------GENERATE PASSWORD--------------------------------

def gen_password():


    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(10))
    password_entry.insert(0, password)


#---------------------------- UI SETUP---------------------------------

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3, column=0)

#entries
website_entry = Entry(width=60)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=60)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "koffic526@gmail.com")
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

#Buttons

add_button = Button(text="Add", width=50, command=save)
add_button.grid(row= 4, column=1, columnspan=2)
gen_pass_button = Button(text="Generate password", command=gen_password)
gen_pass_button.grid(row=3, column=2)



window.mainloop()