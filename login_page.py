import tkinter as tk
from tkinter import messagebox

def login():
    login_id = li_entry.get()
    password = p_entry.get()

    if login_id == "your_username" and password == "your_password":
        messagebox.showinfo("Login Successful")
    else:
        messagebox.showerror("Login Failed")

# GUI setup
root = tk.Tk()
root.title("Login Page")
root.geometry("400x400")  # Set the width and height of the window

# Header
h_label = tk.Label(root, text="Login Page", font=("Helvetica", 16, "bold"))
h_label.grid(row=0, column=0, columnspan=2, pady=10)

# Login ID Label and Entry
li_label = tk.Label(root, text="Login ID:")
li_label.grid(row=1, column=0, padx=10, pady=5)
li_entry = tk.Entry(root)
li_entry.grid(row=1, column=1, padx=10, pady=5)

# Password Label and Entry
p_label = tk.Label(root, text="Password:")
p_label.grid(row=2, column=0, padx=10, pady=5)
p_entry = tk.Entry(root, show="*")  # 'show' attribute hides the entered text
p_entry.grid(row=2, column=1, padx=10, pady=5)

# Login button
login_btn = tk.Button(root, text="Login", command=login)
login_btn.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
