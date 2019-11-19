import tkinter as tk
from tkinter import ttk

class NameEntry(tk.Frame):
    def __init__(self, master, player):
        tk.Frame.__init__(self, master)
        self.root2 = tk.Toplevel(master)
        self.root2.geometry("150x95")
        #self.root2.eval('tk::PlaceWindow %s center' % loginRoot.winfo_pathname(loginRoot.winfo_id()))

        self.player = player

        self.label = ttk.Label(self.root2, text="What is your name? ")
        self.label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        self.entry = ttk.Entry(self.root2)
        self.entry.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.button = ttk.Button(self.root2, text='Enter', command=lambda: self.getName(self.player))
        self.button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        self.entry.focus()
        self.master.bind('<Return>', self.getName)

    def getName(self, player, *args):
        player.name = self.entry.get()
        self.master.destroy()

# nameEntry = NameEntry('hi')
# nameEntry.root.mainloop()
