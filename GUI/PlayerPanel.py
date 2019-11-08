import tkinter as tk
from tkinter import ttk

class PlayerPanel:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding=5, width=300, height=350, relief="groove")
        self.frame.grid(column=1, row=0, sticky='n')
        self.frame.grid_propagate(0)