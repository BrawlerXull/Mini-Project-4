from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import subprocess
import re
import os

def hide_pass():
    eyeimg.config(file="show.png")
    password.config(show="*")
    eyebtn.config(command=show_pass)

def show_pass():
    eyeimg.config(file="hide.png")
    password.config(show="")
    eyebtn.config(command=hide_pass)

def on_enter(event):
    widget=event.widget
    if (widget.get()=='Username' or widget.get()=='Password' or widget.get()=='Email' or widget.get()=='Phone number'):
        widget.delete(0,END)

def empty():           # TO EMPTY SIGNUP CONTENT
    email.place_forget()
    mobile.place_forget()
    f1.place_forget()
    heading2.place_forget()
    f2.place_forget()
    signup_btn.place_forget()
    login()



def is_valid_email(email):
    pattern = r'^\S+@\S+\.\S+$'
    return bool(re.match(pattern, email))

#------------------------------------------connection----------------------------------------------

def insert_into_database(username, password, mobile, email):
    if username == "Username" or password == "Password" or mobile == "Phone number" or email == "Email":
        messagebox.showerror("Error", "Please fill in all fields.")
    elif not is_valid_email(email):
        messagebox.showerror("Error", "Invalid email format.")
    elif not mobile.isdigit() or len(mobile) != 10:
        messagebox.showerror("Error", "Invalid phone number format.")
    else:
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="chaudhari.1234",
                database="Organiser"
            )

            cursor = connection.cursor()

            query = "INSERT INTO users (username, password, mobile, email) VALUES (%s, %s, %s, %s)"
            data = (username, password, mobile, email)

            cursor.execute(query, data)
            connection.commit()
            empty()
            # messagebox.showinfo("Signuped", "Signup Successful!")
            # subprocess.run(["python", "C:\\Users\\Ayush Maurya\\Desktop\\tkinter gui\\login.py"])
        
        except Exception as e:
            messagebox.showerror("Error", f"Error during signup: {str(e)}")
        
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
#------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------SIGNUP-------------------------------------
        
def signup():

    global signup_btn,email,mobile,f1,f2,heading2

    login_btn.place_forget()
    heading1.place_forget()
    goto_signup.place_forget()
    option.place_forget()

    heading2=Label(root,text="USER SIGNUP",font=("Helvetica", 25),bg="#479BDF",fg="white")
    heading2.place(x=220,y=70)

    mobile=Entry(root,width=26,font=("Helvetica", 15),bd=0,bg="#479BDF",fg="white")
    mobile.place(x=170,y=320)
    mobile.insert(0,'Phone number')
    f1=Frame(root,width=290,height=2,bg="white")
    f1.place(x=170,y=345)
    email=Entry(root,width=26,font=("Helvetica", 15),bd=0,bg="#479BDF",fg="white")
    email.place(x=170,y=390)
    email.insert(0,'Email')
    f2=Frame(root,width=290,height=2,bg="white")
    f2.place(x=170,y=415)

    mobile.bind('<FocusIn>',on_enter)
    email.bind('<FocusIn>',on_enter)  
    #signup action-------------------------------------------
    def signup_action():
        username_val = username.get()
        password_val = password.get()
        mobile_val = mobile.get()
        email_val = email.get()

        insert_into_database(username_val, password_val, mobile_val, email_val)
        
    signup_btn = Button(root, text="Sign Up", font=("Helvetica", 16, "bold"), background="#1F0954", foreground="white",
                        activebackground="#1F0954",activeforeground="white", bd=0, padx=7, pady=4, command=signup_action)
    signup_btn.place(x=270, y=500)

#---------------------------------------------------------------------------------------------
#-------------------------------------------------LOGIN CHECK--------------------------------------
def login_action():
    username_val = username.get()
    password_val = password.get()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="chaudhari.1234",
            database="Organiser"
        )

        cursor = connection.cursor()

        # Assuming you have a table named 'users' with columns 'username' and 'password'
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        data = (username_val, password_val)

        cursor.execute(query, data)
        result = cursor.fetchone()

        if result:
            root.destroy()
            subprocess.run(["python", os.path.join(os.getcwd(),"browse.py")]) 
            # subprocess.run(["python", "C:\\Users\\Ayush Maurya\\Desktop\\tkinter gui\\browse.py"]) 
        else:
            messagebox.showerror("Error","Failed credentials")

    except Exception as e:
        messagebox.showerror("Error", f"Error during login: {str(e)}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
#--------------------------------------------------------------------------------------------------

#-----------------------------------------------LOGIN SECTION ------------------------------------------------------
def hover_enter(event):
    forgot_password.config(font=("Helvetica", 12, "underline"), cursor="hand2")

def hover_leave(event):
    forgot_password.config(font=("Helvetica", 12), cursor="")


def login():

    global login_btn,option,goto_signup,signup_btn,heading1,forgot_password

    heading1=Label(root,text="USER LOGIN",font=("Helvetica", 25),bg="#479BDF",fg="white")
    heading1.place(x=220,y=70)
    
    #login button
    login_btn=Button(root,text="Login",font=("Helvetica", 16, "bold"),background="#1F0954",foreground="white",activebackground="#1F0954",
                    activeforeground="white",bd=0,padx=7,pady=4,command=login_action)
    login_btn.place(x=270,y=350)
   
    option=Label(text="Don't have an account?",fg="white",bg="#479BDF",font=("Helvetica",15,"bold"))
    option.place(x=190,y=450)
    goto_signup=Button(root,text="Sign Up",font=("Helvetica", 16, "bold"),background="#479BDF",foreground="BLACK",activebackground="#479BDF",
                    activeforeground="BLACK",bd=0,command=signup)
    goto_signup.place(x=260,y=480)

    forgot_password=Label(root,text="forgot password",font=("Helvetica",12),bg="#479BDF",fg="black")
    forgot_password.place(x=250,y=580)

    # forgot_password.bind("<Enter>",hover_enter)
    # forgot_password.bind("<Leave>",hover_leave)
    # forgot_password.bind("<FocusIn",frogot_password_fun)
#-----------------------------------------------LOGIN SECTION ------------------------------------------------------
# GUI setup
def main2():
    global root,password,username,eyebtn,eyeimg,signup_btn
    root = Tk()
    width = 1100                                                 
    height = 700
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x_position = (screen_width - width) // 2
    y_position = (screen_height - height) // 2
    root.geometry(f"{width}x{height}+{x_position}+{y_position-30}")
    root.resizable(width=False,height=False)
    root.title("Login Page")

    loginimg=Image.open("loginpage2.png")
    loginimg=loginimg.resize((1100,700))
    photo=ImageTk.PhotoImage(loginimg)
    imglabel=Label(root,image=photo)
    imglabel.place(x=0,y=0)

    username=Entry(root,width=26,font=("Helvetica", 15),bd=0,bg="#479BDF",fg="white")
    username.place(x=170,y=180)
    username.insert(0,'Username')
    password=Entry(root,width=24,font=("Helvetica", 15),bd=0,bg="#479BDF",fg="white")
    password.place(x=170,y=250)
    password.insert(0,'Password')
    password.bind('<FocusIn>',on_enter)
    username.bind('<FocusIn>',on_enter)

    Frame(root,width=290,height=2,bg="white").place(x=170,y=205)
    Frame(root,width=290,height=2,bg="white").place(x=170,y=275)

    eyeimg=PhotoImage(file="hide.png")
    eyebtn=Button(root,image=eyeimg,bg="#479BDF",bd=0,activebackground="#479BDF",command=hide_pass)
    eyebtn.place(x=440,y=250)

    # signup_btn=Button(root,text="Sign Up",font=("Helvetica", 16, "bold"),background="#1F0954",foreground="white",activebackground="#1F0954",
    #                     activeforeground="white",bd=0,padx=7,pady=4,command=empty)

    login()

    root.mainloop()
