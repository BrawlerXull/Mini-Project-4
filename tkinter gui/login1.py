from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

signup_btn=None
def hide_pass():
    eyeimg.config(file="show.png")
    password.config(show="*")
    eyebtn.config(command=show_pass)

def show_pass():
    eyeimg.config(file="hide.png")
    password.config(show="")
    eyebtn.config(command=hide_pass)

def hide_pass_signup():
    eyeimg.config(file="show.png")
    password_signup.config(show="*")
    eyebtn.config(command=show_pass_signup)

def show_pass_signup():
    eyeimg.config(file="hide.png")
    password_signup.config(show="")
    eyebtn.config(command=hide_pass_signup)

def on_enter(event):
    widget=event.widget
    if (widget.get()=='Username' or widget.get()=='Password'):
        widget.delete(0,END)

# def login():
#     login_id = li_entry.get()
#     password = p_entry.get()

#     if login_id == "your_username" and password == "your_password":
#         messagebox.showinfo("Login Successful")
#     else:
#         messagebox.showerror("Login Failed")

def empty():           # TO EMPTY SIGNUP CONTENT
    name.place_forget()
    email.place_forget()
    password_signup.place_forget()
    mobile.place_forget()
    f1.place_forget()
    f2.place_forget()
    signup_btn.place_forget()
    login()
#---------------------------------------------------------------SIGNUP-------------------------------------
        
def signup():

    global signup_btn,password_signup,eyebtn,eyeimg,name,email,mobile,f1,f2
    
    login_btn.place_forget()
    username.place_forget()
    password.place_forget()
    goto_signup.place_forget()
    option.place_forget()
    

    heading=Label(root,text="USER SIGNUP",font=("Helvetica", 25),bg="#AD53A6",fg="white")
    heading.place(x=220,y=70)
    name=Entry(root,width=26,font=("Helvetica", 15),bd=0,bg="#AD53A6",fg="white")
    name.place(x=170,y=180)
    name.insert(0,'Username')
    Frame(root,width=290,height=2,bg="white").place(x=170,y=205)

    password_signup=Entry(root,width=26,font=("Helvetica", 15),bd=0,bg="#AD53A6",fg="white")
    password_signup.place(x=170,y=250)
    password_signup.insert(0,'Password')
    Frame(root,width=290,height=2,bg="white").place(x=170,y=275)

    mobile=Entry(root,width=26,font=("Helvetica", 15),bd=0,bg="#AD53A6",fg="white")
    mobile.place(x=170,y=320)
    mobile.insert(0,'phone number')
    f1=Frame(root,width=290,height=2,bg="white")
    f1.place(x=170,y=345)
    email=Entry(root,width=26,font=("Helvetica", 15),bd=0,bg="#AD53A6",fg="white")
    email.place(x=170,y=390)
    email.insert(0,'Email')
    f2=Frame(root,width=290,height=2,bg="white")
    f2.place(x=170,y=415)

    password_signup.bind('<FocusIn>',on_enter)
    name.bind('<FocusIn>',on_enter)
    mobile.bind('<FocusIn>',on_enter)
    email.bind('<FocusIn>',on_enter)

    eyeimg=PhotoImage(file="hide.png")
    eyebtn=Button(root,image=eyeimg,bg="#AD53A6",bd=0,activebackground="#AD53A6",command=hide_pass_signup)
    eyebtn.place(x=440,y=250)   
   
    signup_btn.place(x=270,y=500)
#-----------------------------------------------LOGIN SECTION ------------------------------------------------------
def login():

    global eyebtn,eyeimg,password,login_btn,option,goto_signup,username,password,signup_btn
    signup_btn.place_forget()

    heading=Label(root,text="USER LOGIN",font=("Helvetica", 25),bg="#AD53A6",fg="white")
    heading.place(x=220,y=70)
    username=Entry(root,width=26,font=("Helvetica", 15),bd=0,bg="#AD53A6",fg="white")
    username.place(x=170,y=180)
    username.insert(0,'Username')
    password=Entry(root,width=24,font=("Helvetica", 15),bd=0,bg="#AD53A6",fg="white")
    password.place(x=170,y=250)
    password.insert(0,'Password')
    password.bind('<FocusIn>',on_enter)
    username.bind('<FocusIn>',on_enter)
   
    Frame(root,width=290,height=2,bg="white").place(x=170,y=205)
    Frame(root,width=290,height=2,bg="white").place(x=170,y=275)
    
    eyeimg=PhotoImage(file="hide.png")
    eyebtn=Button(root,image=eyeimg,bg="#AD53A6",bd=0,activebackground="#AD53A6",command=hide_pass)
    eyebtn.place(x=440,y=250)
    
    login_btn=Button(root,text="Login",font=("Helvetica", 16, "bold"),background="#1F0954",foreground="white",activebackground="#1F0954",
                    activeforeground="white",bd=0,padx=7,pady=4)
    login_btn.place(x=270,y=350)
   
    option=Label(text="Don't have an account?",fg="white",bg="#AD53A6",font=("Helvetica",15,"bold"))
    option.place(x=190,y=450)
    goto_signup=Button(root,text="Sign Up",font=("Helvetica", 16, "bold"),background="#AD53A6",foreground="BLACK",activebackground="#AD53A6",
                    activeforeground="BLACK",bd=0,command=signup)
    goto_signup.place(x=260,y=480)

#-----------------------------------------------LOGIN SECTION ------------------------------------------------------
# GUI setup
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

signup_btn=Button(root,text="Sign Up",font=("Helvetica", 16, "bold"),background="#1F0954",foreground="white",activebackground="#1F0954",
                    activeforeground="white",bd=0,padx=7,pady=4,command=empty)

loginimg=Image.open("loginpage.png")
loginimg=loginimg.resize((1100,700))
photo=ImageTk.PhotoImage(loginimg)
imglabel=Label(root,image=photo)
imglabel.place(x=0,y=0)

login()

root.mainloop()