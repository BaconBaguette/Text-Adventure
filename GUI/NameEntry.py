import tkinter as tk
from tkinter import ttk

class NameEntry:
    def __init__(self):
        self.root =tk.Tk()
        self.root.geometry("150x95")
        self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_pathname(self.root.winfo_id()))

        self.label = ttk.Label(self.root, text="What is your name? ")
        self.label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        self.entry = ttk.Entry(self.root)
        self.entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.button = ttk.Button(self.root, text='Enter', command=self.getName)
        self.button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

    def getName(self):
        print(self.entry.get())
        return self.entry.get()

nameEntry = NameEntry()

nameEntry.root.mainloop()