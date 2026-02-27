from tkinter import *
from tkinter import messagebox
import sqlite3
import webbrowser

# ---------- DATABASE ----------
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
name TEXT,
email TEXT,
password TEXT
)
""")

conn.commit()


# ---------- WINDOW ----------
root = Tk()
root.title("Login System")
root.geometry("500x450")
root.config(bg="white")


# ---------- FUNCTIONS ----------

def show_signup():

    login_frame.pack_forget()
    signup_frame.pack(fill="both",expand=True)


def show_login():

    signup_frame.pack_forget()
    login_frame.pack(fill="both",expand=True)


def signup():

    name = name_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    repass = repass_entry.get()

    if name=="" or email=="" or password=="":
        messagebox.showerror("Error","Fill all fields")
        return

    if password!=repass:
        messagebox.showerror("Error","Passwords not match")
        return

    cursor.execute("INSERT INTO users VALUES(?,?,?)",
                   (name,email,password))
    conn.commit()

    messagebox.showinfo("Success","Account Created")

    show_login()


def login():

    email = login_email.get()
    password = login_pass.get()

    cursor.execute("SELECT * FROM users WHERE email=? AND password=?",
                   (email,password))

    data = cursor.fetchone()

    if data:
        show_welcome(data[0])
    else:
        messagebox.showerror("Error","Invalid Login")


def show_welcome(username):

    login_frame.pack_forget()

    welcome_frame.pack(fill="both",expand=True)

    welcome_label.config(text="Welcome " + username)

    # Open YouTube Video Automatically
    webbrowser.open("https://youtube.com/shorts/8TO6_J3i5YU")


def logout():

    welcome_frame.pack_forget()
    login_frame.pack(fill="both",expand=True)



# ---------- LOGIN FRAME ----------

login_frame = Frame(root,bg="white")

Label(login_frame,
text="Login",
font=("Arial",28,"bold"),
bg="white").pack(pady=20)


Label(login_frame,text="Email",bg="white").pack()

login_email = Entry(login_frame,font=("Arial",12),width=30)
login_email.pack(pady=5,ipady=5)


Label(login_frame,text="Password",bg="white").pack()

login_pass = Entry(login_frame,font=("Arial",12),width=30,show="*")
login_pass.pack(pady=5,ipady=5)



Button(login_frame,
text="Login",
font=("Arial",14),
bg="#3b82b6",
fg="white",
width=20,
command=login).pack(pady=20)



Button(login_frame,
text="New User? Signup",
bd=0,
fg="blue",
bg="white",
command=show_signup).pack()



# ---------- SIGNUP FRAME ----------

signup_frame = Frame(root,bg="white")


Label(signup_frame,
text="Signup",
font=("Arial",28,"bold"),
bg="white").pack(pady=20)


Label(signup_frame,text="Name",bg="white").pack()

name_entry = Entry(signup_frame,width=30,font=("Arial",12))
name_entry.pack(pady=5,ipady=5)


Label(signup_frame,text="Email",bg="white").pack()

email_entry = Entry(signup_frame,width=30,font=("Arial",12))
email_entry.pack(pady=5,ipady=5)


Label(signup_frame,text="Password",bg="white").pack()

pass_entry = Entry(signup_frame,width=30,font=("Arial",12),show="*")
pass_entry.pack(pady=5,ipady=5)


Label(signup_frame,text="Re-enter Password",bg="white").pack()

repass_entry = Entry(signup_frame,width=30,font=("Arial",12),show="*")
repass_entry.pack(pady=5,ipady=5)



Button(signup_frame,
text="Create Account",
font=("Arial",14),
bg="#3b82b6",
fg="white",
width=20,
command=signup).pack(pady=20)



Button(signup_frame,
text="Already user? Login",
bd=0,
fg="blue",
bg="white",
command=show_login).pack()



# ---------- WELCOME FRAME ----------

welcome_frame = Frame(root,bg="white")


welcome_label = Label(welcome_frame,
font=("Arial",26,"bold"),
bg="white")

welcome_label.pack(pady=80)


Button(welcome_frame,
text="Logout",
font=("Arial",14),
bg="red",
fg="white",
width=15,
command=logout).pack()



# Start from Login
login_frame.pack(fill="both",expand=True)

root.mainloop()