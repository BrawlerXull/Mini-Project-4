import tkinter as tk
from tkinter import messagebox
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="admin",
    database="organizer"
)
cursor = db_connection.cursor()

def signup():
    name = name_entry.get()
    age = age_entry.get()
    mobile_number = mobile_entry.get()
    email_address = email_entry.get()
    login_id = login_entry.get()
    password = password_entry.get()

    insert_query = f"""
    INSERT INTO people (name, age, mobile_number, email_address, login_id, password)
    VALUES ('{name}', {age}, '{mobile_number}', '{email_address}', '{login_id}', '{password}')
    """
    cursor.execute(insert_query)
    db_connection.commit()

    messagebox.showinfo("Signup Successful", "User successfully signed up!")

root = tk.Tk()
root.title("Signup Page")
root.geometry("400x400")

h_label = tk.Label(root, text="Signup Page", font=("Helvetica", 16, "bold"))
h_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(expand=True, fill="both")

tk.Label(frame, text="Name:").grid(row=0, column=0, padx=50, pady=10)
tk.Label(frame, text="Age:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(frame, text="Mobile Number:").grid(row=2, column=0, padx=10, pady=10)
tk.Label(frame, text="Email Address:").grid(row=3, column=0, padx=10, pady=10)
tk.Label(frame, text="Login ID:").grid(row=4, column=0, padx=10, pady=10)
tk.Label(frame, text="Password:").grid(row=5, column=0, padx=10, pady=10)

name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry = tk.Entry(frame)
age_entry.grid(row=1, column=1, padx=10, pady=5)
mobile_entry = tk.Entry(frame)
mobile_entry.grid(row=2, column=1, padx=10, pady=5)
email_entry = tk.Entry(frame)
email_entry.grid(row=3, column=1, padx=10, pady=5)
login_entry = tk.Entry(frame)
login_entry.grid(row=4, column=1, padx=10, pady=5)
password_entry = tk.Entry(frame, show="*")
password_entry.grid(row=5, column=1, padx=10, pady=5)

signup_btn = tk.Button(frame, text="Signup", command=signup)
signup_btn.grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
