import tkinter as tk
from tkinter import ttk
#import GUIFuncs

class ButtonPanel:
    def __init__(self, parent):

        #guifuncs = GUIFuncs.GUIfuncs(parent)

        self.frame = ttk.Frame(parent, padding=5, width=800, height=75, relief="groove")
        self.frame.grid(column=0, row=2)

        self.button1 = ttk.Button(self.frame, text="Choice 1")#, command=guifuncs.printSomething)
        self.button1.place(relx=0.1, rely=0.5, anchor=tk.CENTER)

        self.button2 = ttk.Button(self.frame, text="Choice 2")
        self.button2.place(relx=0.25, rely=0.5, anchor=tk.CENTER)

        self.button3 = ttk.Button(self.frame, text="Choice 2")
        self.button3.place(relx=0.4, rely=0.5, anchor=tk.CENTER)