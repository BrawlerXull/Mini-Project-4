# from tkinter import *
# from tkinter import filedialog
# import mysql.connector
# from mysql.connector import Error
# from datetime import datetime
# from tkinter import ttk
# import login as l

# connection = None
# treeview = None  

# def choose_folder():
#     global connection, treeview
#     folder_path = filedialog.askdirectory()

#     try:
#         if connection.is_connected():
#             cursor = connection.cursor()
#             current_date = datetime.now()
#             current_time = datetime.now()
#             query = "INSERT INTO file_records (file_path, file_date, file_time) VALUES (%s, %s, %s)"
#             values = (folder_path, current_date, current_time)
#             cursor.execute(query, values)
#             connection.commit()
#             cursor.close()

#             # Update Treeview after inserting data
#             update_treeview(treeview)  # Pass treeview as an argument

#     except Error as e:
#         print("Error:", e)

# def update_treeview(treeview):
#     global connection

#     try:
#         if connection.is_connected():
#             cursor = connection.cursor()
#             cursor.execute("SELECT * FROM file_records")
#             records = cursor.fetchall()

#             # Clear existing data in Treeview
#             for row in treeview.get_children():
#                 treeview.delete(row)

#             # Insert new data into Treeview
#             for record in records:
#                 treeview.insert("", "end", values=record)

#             cursor.close()

#     except Error as e:
#         print("Error:", e)

# def main():
#     global connection, treeview,browse

#     browse = Tk()
#     window_width = 1100
#     window_height = 700
#     screen_width = browse.winfo_screenwidth()
#     screen_height = browse.winfo_screenheight()
#     x_position = (screen_width - window_width) // 2
#     y_position = (screen_height - window_height) // 2
#     browse.geometry(f"{window_width}x{window_height}+{x_position}+{y_position-30}")
#     browse.minsize(1100, 700)

#     # Left Frame
#     l_frame = Frame(browse, bg="#000000", width=400)
#     l_frame.pack_propagate(0)
#     l_frame.pack(side=LEFT, fill=Y)

#     l_heading = Label(l_frame, text="Quick Start Guide", font=("Helvetica", 17, "bold"), bg="#000000", fg="white", )
#     l_heading.pack(side=TOP, pady=(15, 20))
#     Frame(l_frame, width=350, height=2, bg="white").pack()
#     l_label1 = Label(l_frame, text="""1) Click on the 'Browse' button to initiate the folder selection process.
#         \n2) Navigate through your directories and select the folder where you want to organize your files.
#         \n3) Once you've chosen the target folder, click on the 'Upload' button to initiate the organization process.
#         \n4)The application will automatically arrange the files within your selected folder based on predefined rules and categories.
#         \n5)After the organization process completes, you'll find your files neatly sorted and categorized within the same folder.""",
#                      font=("Helvetica", 12), bg="#000000", fg="white", wraplength=300, justify=LEFT)
#     l_label1.pack(pady=(10, 5))

#     # Bottom Frame
#     b_frame = Frame(browse, bg="#4ed4b3")
#     next_btn = Button(b_frame, text="Recently Used", bg="#4ed4b3", fg="white", font="Helvetica 13 bold", padx=("5px", "5px"),
#                       pady=("5px", "5px"), bd=0,
#                       activebackground="#4ed4b3")
#     next_btn.pack(side=RIGHT, padx=15, pady=(10, 5))
#     b_frame.pack(side=BOTTOM, fill=X)

#     # Right Frame
#     r_frame = Frame(browse, bg="#4ed4b3")
#     r_frame.pack(side=RIGHT,fill=BOTH,expand=True)

#     r_heading = Label(r_frame, text="Organizer", font=("Helvetica", 16, "bold"), bg="#4ed4b3")
#     r_heading.pack(pady=(5,10))

#     choose_folder_butn = Button(r_frame, text="Browse", command=choose_folder,font=("Helvetica", 16),bd=0,activebackground="black",activeforeground="white")
#     choose_folder_butn.pack(pady=(40))

#     style=ttk.Style()
#     style.configure("Treeview",font=("Helvetica", 11),foreground="#FBFADA",background="#12372A",rowheight=35,borderwidth=0, highlightthickness=0)
#     style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), foreground="black")
#     treeview = ttk.Treeview(r_frame, columns=("file_path", "file_date", "file_time"), show="headings",style="Treeview")
#     treeview.heading("file_path", text="File Path")
#     treeview.heading("file_date", text="Date")
#     treeview.heading("file_time", text="Time")

#     treeview.column("file_path",width=450)
#     treeview.column("file_date",width=100)
#     treeview.column("file_time",width=100)
#     treeview.pack(pady=100)

#     try:
#         connection = mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="admin",
#             database="organiser"
#         )
#         update_treeview(treeview)  # Pass treeview as an argument

#     except Error as e:
#         print("Error:", e)

#     # browse.grid_rowconfigure(0, weight=1)
#     # browse.grid_columnconfigure(0, weight=1)
#     # browse.grid_columnconfigure(1, weight=1)

#     browse.mainloop()
# main()
# if __name__ == "_main_":
#      main()




import threading
from tkinter import *
from tkinter import filedialog
import mysql.connector
from mysql.connector import Error
from datetime import datetime
from tkinter import ttk
import login as l
from helper import applyWatcher

connection = None
treeview = None  
global_path = ""

def choose_folder():
    global connection, treeview
    folder_path = filedialog.askdirectory()
    global_path = folder_path
    print(global_path)
    
    print("CHOOSE FUNC CALLED")
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

            # Update Treeview after inserting data
            update_treeview(folder_path)  # Pass folder_path as an argument

    except Error as e:
        print("Error:", e)

def update_treeview(folder_path):
    global connection

    try:
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM file_records")
            records = cursor.fetchall()

            # Clear existing data in Treeview
            for row in treeview.get_children():
                treeview.delete(row)

            # Insert new data into Treeview
            for record in records:
                treeview.insert("", "end", values=record)
            
            cursor.close()

    except Error as e:
        print("Error:", e)

    print("Update FUNC CALLED")
    if folder_path != "":
        print("Watcher Applied")

        # Create a thread for applying watcher
        thread1 = threading.Thread(target=applyWatcher, args=(folder_path,))
        thread1.start()

def main():
    global connection, treeview

    browse = Tk()
    window_width = 1100
    window_height = 700
    screen_width = browse.winfo_screenwidth()
    screen_height = browse.winfo_screenheight()
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    browse.geometry(f"{window_width}x{window_height}+{x_position}+{y_position-30}")
    browse.minsize(1100, 700)

    # Left Frame
    l_frame = Frame(browse, bg="#000000", width=400)
    l_frame.pack_propagate(0)
    l_frame.pack(side=LEFT, fill=Y)

    l_heading = Label(l_frame, text="Quick Start Guide", font=("Helvetica", 17, "bold"), bg="#000000", fg="white", )
    l_heading.pack(side=TOP, pady=(15, 20))
    Frame(l_frame, width=350, height=2, bg="white").pack()
    l_label1 = Label(l_frame, text="""1) Click on the 'Browse' button to initiate the folder selection process.
        \n2) Navigate through your directories and select the folder where you want to organize your files.
        \n3) Once you've chosen the target folder, click on the 'Upload' button to initiate the organization process.
        \n4)The application will automatically arrange the files within your selected folder based on predefined rules and categories.
        \n5)After the organization process completes, you'll find your files neatly sorted and categorized within the same folder.""",
                     font=("Helvetica", 12), bg="#000000", fg="white", wraplength=300, justify=LEFT)
    l_label1.pack(pady=(10, 5))

    # Bottom Frame
    b_frame = Frame(browse, bg="#4ed4b3")
    next_btn = Button(b_frame, text="Recently Used", bg="#4ed4b3", fg="white", font="Helvetica 13 bold", padx=("5px", "5px"),
                      pady=("5px", "5px"), bd=0,
                      activebackground="#4ed4b3")
    next_btn.pack(side=RIGHT, padx=15, pady=(10, 5))
    b_frame.pack(side=BOTTOM, fill=X)

    # Right Frame
    r_frame = Frame(browse, bg="#4ed4b3")
    r_frame.pack(side=RIGHT,fill=BOTH,expand=True)

    r_heading = Label(r_frame, text="Organizer", font=("Helvetica", 16, "bold"), bg="#4ed4b3")
    r_heading.pack(pady=(5,10))

    choose_folder_butn = Button(r_frame, text="Browse", command=choose_folder,font=("Helvetica", 16),bd=0,activebackground="black",activeforeground="white")
    choose_folder_butn.pack(pady=(40))

    style=ttk.Style()
    style.configure("Treeview",font=("Helvetica", 11),foreground="#FBFADA",background="#12372A",rowheight=35,borderwidth=0, highlightthickness=0)
    style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"), foreground="black")
    treeview = ttk.Treeview(r_frame, columns=("file_path", "file_date", "file_time"), show="headings",style="Treeview")
    treeview.heading("file_path", text="File Path")
    treeview.heading("file_date", text="Date")
    treeview.heading("file_time", text="Time")

    treeview.column("file_path",width=450)
    treeview.column("file_date",width=100)
    treeview.column("file_time",width=100)
    treeview.pack(pady=100)

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="chaudhari.1234",
            database="Organiser"
        )
        update_treeview("")  # Pass empty string as folder_path

    except Error as e:
        print("Error:", e)

    browse.mainloop()
main()
if __name__ == "_main_":
    main()