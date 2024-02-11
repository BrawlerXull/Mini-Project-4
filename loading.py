from tkinter import *
import welcome as wel
from tkinter.ttk import *
from PIL import Image, ImageTk

splash_win = Tk()
width = 500
height = 300
screen_width = splash_win.winfo_screenwidth()
screen_height = splash_win.winfo_screenheight()
x_position = (screen_width - width) // 2
y_position = (screen_height - height) // 2
splash_win.geometry(f"{width}x{height}+{x_position}+{y_position}")

splash_win.overrideredirect(True)

style = Style()
style.configure("Blue.TFrame", background="blue")

frame1 = Frame(splash_win)
frame2 = Frame(splash_win, style="Blue.TFrame")
# Open the image and resize it
splash_logo = Image.open("please wait.jpg")
resized_image = splash_logo.resize((500, 250))

# Convert the resized image to a PhotoImage
photo = ImageTk.PhotoImage(resized_image)

# Create a label to display the image
image_label = Label(frame1, image=photo)
image_label.pack()

style = Style()
style.theme_use('default')  # Use the default theme
style.configure("blue.Horizontal.TProgressbar", foreground='blue', background='blue')
progress = Progressbar(frame2, orient=HORIZONTAL, length=450, mode='determinate',style="blue.Horizontal.TProgressbar")
progress.pack(anchor="center",padx=10,pady=10)

def update_progress(value=0):
    progress['value'] = value
    if value < 100:
        value += 40
        splash_win.after(1000, update_progress, value)

update_progress()

def mainWin():
    splash_win.destroy()
    wel.main_screen()

splash_win.after(3000, mainWin)

frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
splash_win.mainloop()
