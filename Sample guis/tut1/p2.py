from tkinter import *
from tkinter import filedialog
import mysql.connector
from mysql.connector import Error
from datetime import datetime

connection = None

def choose_folder():
    global connection
    folder_path = filedialog.askdirectory()

    try:
        if connection.is_connected():
            cursor = connection.cursor()
            current_date = datetime.now()
            current_time = datetime.now()
            query = "INSERT INTO file_records (file_path, file_date, file_time) VALUES (%s, %s, %s)"
            values = (folder_path, current_date, current_time)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()

    except Error as e:
        print("Error:", e)

def main():
    global connection
    aditya_root = Tk()
    aditya_root.geometry("800x600")

    l_frame = Frame(aditya_root, bg="#f2f2f2", width=320, height=240)
    l_frame.pack_propagate(0)
    l_frame.grid(row=0, column=0, sticky="nsew")

    l_heading = Label(l_frame, text="Quick Start Guide", font=("Helvetica", 16, "bold"), bg="#f2f2f2")
    l_heading.pack()

    r_frame = Frame(aditya_root, bg="lightblue", width=480, height=360)
    r_frame.pack_propagate(0)
    r_frame.grid(row=0, column=1, sticky="nsew")

    r_heading = Label(r_frame, text="Organizer", font=("Helvetica", 16, "bold"), bg="lightblue")
    r_heading.pack()

    choose_folder_butn = Button(r_frame, text="Browse", command=choose_folder)
    choose_folder_butn.pack()

    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="admin",
            database="organizer"
        )

    except Error as e:
        print("Error:", e)

    aditya_root.grid_rowconfigure(0, weight=1)
    aditya_root.grid_columnconfigure(0, weight=1)
    aditya_root.grid_columnconfigure(1, weight=1)

    aditya_root.mainloop()

if __name__ == "__main__":
    main()
