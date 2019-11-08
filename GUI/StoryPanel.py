import tkinter as tk
from tkinter import ttk
from functools import partial
from time import sleep
import io
import csv
import os

mainDir = os.getcwd()
loc = mainDir + '\\loc.csv'

class StoryPanel:
    def __init__(self, parent):

        #guifuncs = GUIFuncs.GUIfuncs(parent)
        self.parent = parent

        self.frame = ttk.Frame(parent, padding=5, width=800, height=350, relief="groove")
        self.frame.grid(column=0, row=0)
        self.frame.grid_propagate(0)

        self.line1Text = tk.StringVar()
        self.line2Text = tk.StringVar()
        self.line3Text = tk.StringVar()
        self.line4Text = tk.StringVar()
        self.line5Text = tk.StringVar()
        self.line6Text = tk.StringVar()
        self.line7Text = tk.StringVar()
        self.line8Text = tk.StringVar()
        self.line9Text = tk.StringVar()

        self.lineTextDict = { 2:self.line1Text,
                          3:self.line2Text,
                          4:self.line3Text,
                          5:self.line4Text,
                          6:self.line5Text,
                          7:self.line6Text,
                          8:self.line7Text,
                          9:self.line8Text,
                          10:self.line9Text }

        self.line1 = ttk.Label(self.frame, textvariable=self.line1Text, padding=5)
        self.line1.place(relx=0.5, rely=0.05, anchor=tk.CENTER)

        self.line2 = ttk.Label(self.frame, textvariable=self.line2Text, padding=5)
        self.line2.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

        self.line3 = ttk.Label(self.frame, textvariable=self.line3Text, padding=5)
        self.line3.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        self.line4 = ttk.Label(self.frame, textvariable=self.line4Text, padding=5)
        self.line4.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

        self.line5 = ttk.Label(self.frame, textvariable=self.line5Text, padding=5)
        self.line5.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

        self.line6 = ttk.Label(self.frame, textvariable=self.line6Text, padding=5)
        self.line6.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

        self.line7 = ttk.Label(self.frame, textvariable=self.line7Text, padding=5)
        self.line7.place(relx=0.5, rely=0.65, anchor=tk.CENTER)

        self.line8 = ttk.Label(self.frame, textvariable=self.line8Text, padding=5)
        self.line8.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

        self.line9 = ttk.Label(self.frame, textvariable=self.line9Text, padding=5)
        self.line9.place(relx=0.5, rely=0.85, anchor=tk.CENTER)

        self.button = ttk.Button(self.frame, text='Click Me After', padding=5, command=lambda: self.applyStoryText(self.parent))
        self.button.place(relx=0.6, rely=0.95, anchor=tk.CENTER)

        self.lineDict = { 2:self.line1,
                          3:self.line2,
                          4:self.line3,
                          5:self.line4,
                          6:self.line5,
                          7:self.line6,
                          8:self.line7,
                          9:self.line8,
                          10:self.line9 }


    def applyStoryText(self, parent):
        with open(loc) as loc_file:
            loc_reader = csv.reader(loc_file, delimiter=';')
            for entry in loc_reader:
                if entry[0] == '10':
                    for x in range(2, 11):
                        self.parent.update()
                        if entry[x] != '':
                            self.lineTextDict[x].set(entry[x])
                        else:
                            pass
                else:
                    pass