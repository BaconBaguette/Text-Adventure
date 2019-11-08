import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("150x50")
root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

label = ttk.Label(root, text="What is your name? ")
label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)


entry = ttk.Entry(root)
entry.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

root.mainloop()