import tkinter as tk
from tkinter import ttk

class NameEntry:
    def __init__(self, master, player):
        self.master = master
        self.player = player

        self.label = ttk.Label(self.master, text="What is your name? ")
        self.label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        self.entry = ttk.Entry(self.master)
        self.entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.button = ttk.Button(self.master, text='Enter', command=lambda: self.getName(self.player))
        self.button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.entry.focus()
        self.master.bind('<Return>', self.getName)

    def getName(self, player, *args):
        player.name = self.entry.get()
        return self.entry.get()

# nameEntry = NameEntry('hi')
# nameEntry.root.mainloop()
