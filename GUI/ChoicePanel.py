import tkinter as tk
from tkinter import ttk

class ChoicePanel:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding=5, width=800, height=125, relief="groove")
        self.frame.grid(column=0, row=1)
        self.frame.grid_propagate(0)