from tkinter import *
from PIL import Image, ImageTk
import login as l

def next():
    welcome_screen.destroy()
    l.main2()

def main_screen():
    global welcome_screen
    welcome_screen = Tk()
    window_width = 1100  # window sizing and positioning
    window_height = 700
    screen_width = welcome_screen.winfo_screenwidth()
    screen_height = welcome_screen.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    welcome_screen.geometry(f"{window_width}x{window_height}+{x_position}+{y_position-30}")
    welcome_screen.minsize(1100, 700)

    welcome_screen.configure(bg="#4ed4b3")  # window background colour

    head = Frame(welcome_screen, bg="#000000")  # Heading Frame
    heading = Label(head, text="A File Organizer", font="Arial 25 bold", pady="20px", bg="#000000", fg="#FFFFFF")
    heading.pack()
    head.pack(side=TOP, fill=X)

    bottom = Frame(welcome_screen, bg="#000000")
    footer = Label(bottom, text="@All rights reserved", font="Arial 10", pady="10px", bg="#000000", fg="#FFFFFF")
    footer.pack()
    bottom.pack(side=BOTTOM, fill=X)

    f1 = Frame(welcome_screen, bg="#FFFFFF")
    logo = Image.open("final1.png")
    resized_logo = logo.resize((500, 500))
    photo = ImageTk.PhotoImage(resized_logo)
    image_label = Label(f1, image=photo, bd="0")
    image_label.pack(pady=20)
    f1.pack(side=LEFT, fill=Y)

    f2 = Frame(welcome_screen, bd="0", bg="#4ed4b3")  # Right Frame
    feature = Label(f2, text="Features", font="Arial 20 bold", bg="#4ed4b3")
    feature.pack(pady=("30px", 0))
    text_right = Label(f2, text="\n"
                               "1. Organize\n"
                               "   - Arrange all your files based on their file types.\n"
                               "2. Clean Old Items\n"
                               "   - Delete the files of certain user-given old-aged files.",
                       font=("Arial", 16), justify=LEFT, bg="#4ed4b3")
    text_right.pack(anchor="center", pady=20, padx=20)

    but1 = Button(f2, text="Get Started", bg="#4ed4b3", fg="#FFFFFF", font="Arial 18", padx=20, pady=10, command=next)
    but1.pack(side=BOTTOM, pady=("50px", 0))

    f2.pack(fill=BOTH, padx="15px", pady="20px", )

    welcome_screen.mainloop()

if __name__ == "_main_":
    main_screen()