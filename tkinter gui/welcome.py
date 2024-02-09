from tkinter import *
from PIL import Image,ImageTk
import login as l


def next():
    welcome_screen.destroy()
    l.main2()


def main_screen():
    global welcome_screen
    welcome_screen = Tk()
    window_width = 1100                                                   #window sizing and positioning
    window_height = 700
    screen_width = welcome_screen.winfo_screenwidth()
    screen_height = welcome_screen.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    welcome_screen.geometry(f"{window_width}x{window_height}+{x_position}+{y_position-30}")
    welcome_screen.minsize(1100,00)

    welcome_screen.configure(bg="#737373")                                #window background colour 

    head=Frame(welcome_screen)
    heading=Label(head,text="File Organizer",font="comicsansms 19 bold",pady="10px",bg="#737373",fg="#FFFFFF")
    heading.pack()
    head.pack(side=TOP)

    bottom= Frame(welcome_screen)
    footer=Label(bottom,text="All rights reserved",font="comicsansms 10",pady="10px",bg="#737373",fg="#FFFFFF")
    footer.pack()
    bottom.pack(side=BOTTOM)

    f1=Frame(welcome_screen)                                              #frame for logo
    logo=Image.open("logo2.jpg")
    photo=ImageTk.PhotoImage(logo)
    image_label=Label(f1,image=photo,bd="0")
    image_label.pack()
    f1.pack(side=LEFT)

    f2=Frame(welcome_screen,bd="0",bg="#737373")                                  #LEFT FRAME
    feature=Label(f2,text="Features",font="Helvetica 17 bold",bg="#737373")
    feature.pack(pady=("30px",0))
    text_right = Label(f2, text="\n"
                                        "1. Organize\n"
                                        "   - Arrange all your files based on their file types.\n"
                                        "2. Clean Old Items\n"
                                        "   - Delete the files of certain user-given old-aged files.",
                    font=("Helvetica", 15), justify=LEFT,bg="#737373")
    text_right.pack(anchor="center",pady=10,padx=20 )

    import tkinter as tk
    #------------------------------

    but1=Button(f2,text="Get Started",bg="blue",fg="white",font="Helvetica 15",padx=("5px","5px"),pady=("5px","5px"),command=next)
    but1.pack(side=BOTTOM,pady=("150px",0))

    f2.pack(fill=BOTH,padx="15px",pady="20px",)

    welcome_screen.mainloop()

if __name__=="__main__":
    main_screen()