from tkinter import *
from PIL import Image, ImageTk

def get_started():
    print("Getting started!")

aditya_root = Tk()

# Set the window size
aditya_root.geometry("900x600")

h_label = Label(aditya_root, text="Organizer", font=("Helvetica", 16))
h_label.grid(row=0, column=0, columnspan=2, pady=10)

logo_image = Image.open("logo.jpg")
logo_image = logo_image.resize((int(aditya_root.winfo_reqwidth() * 2), int(aditya_root.winfo_reqheight() * 2)))
logo_photo = ImageTk.PhotoImage(logo_image)

logo = Label(aditya_root, image=logo_photo)
logo.grid(row=1, column=0, padx=20, pady=30, sticky="w")

text_right = Label(aditya_root, text="Features:\n"
                                     "1. Organize\n"
                                     "   - Arrange all your files based on their file types.\n"
                                     "2. Clean Old Items\n"
                                     "   - Delete the files of certain user-given old-aged files.",
                   font=("Helvetica", 12), justify=LEFT)
text_right.grid(row=1, column=1, padx=10, pady=10)

# Button at the bottom right
get_started_butn = Button(aditya_root, text="Get Started", command=get_started)
get_started_butn.grid(row=2, column=1, sticky="se", padx=10, pady=10)

# Footer
f_label = Label(aditya_root, text="@organizer", font=("Helvetica", 12))
f_label.grid(row=4, column=0, columnspan=2, pady=10)

aditya_root.mainloop()
