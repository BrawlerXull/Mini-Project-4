import tkinter as tk
from tkinter import ttk

class RecentlyUsedFiles:
    def __init__(self, master):
        self.master = master
        self.master.title("Recently Used Files")

        # Header
        h_label = tk.Label(self.master, text="Recently Used Files", font=("Helvetica", 16))
        h_label.grid(row=0, column=0, columnspan=2, sticky = "ew")

        # Table
        columns = ["File Name", "Time Accessed"]
        self.tree = ttk.Treeview(self.master, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=350, anchor="center")

        self.tree.grid(row=1, column=0, columnspan=2)

    def file_names(self, file_names):
        for file in file_names:
            data = (file, "")
            self.tree.insert("", tk.END, values=data)

    def time_accessed(self, times_accessed):
        items = self.tree.get_children()

        for index, time_accessed in enumerate(times_accessed):
            self.tree.item(items[index], values=(self.tree.item(items[index], "values")[0], time_accessed))

if __name__ == "__main__":
    root = tk.Tk()

    p3 = RecentlyUsedFiles(root)

    # Example data
    file_names_array = ["1.png", "2.png", "3.png"]
    times_accessed_array = ["13", "5", "3"]

    p3.file_names(file_names_array)
    p3.time_accessed(times_accessed_array)

    root.mainloop()
