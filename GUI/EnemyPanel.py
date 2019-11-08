import tkinter as tk
from tkinter import ttk

class EnemyPanel:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding=5, width=300, height=200, relief="groove")
        self.frame.grid(column=1, row=1, rowspan=2, sticky='s')
        self.frame.grid_propagate(0)