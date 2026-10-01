import tkinter as tk

root = tk.Tk()

root.title("Student Management System")
root.geometry("600x400")

label = tk.Label(root, text="Enter Student Name")
label.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()