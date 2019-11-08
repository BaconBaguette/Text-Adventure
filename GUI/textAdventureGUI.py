from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Text Adventure")
root.resizable(False, False)

# mainframe = ttk.Frame(root, padding=5, width=1400, height=700, borderwidth=55, relief="groove")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

storyFrame = ttk.Frame(root, padding=5, width=800, height=350, relief="groove")
storyFrame.grid(column=0, row=0)

choiceFrame = ttk.Frame(root, padding=5, width=800, height=125, relief="groove")
choiceFrame.grid(column=0, row=1)

buttonFrame = ttk.Frame(root, padding=5, width=800, height=75, relief="groove")
buttonFrame.grid(column=0, row=2)
buttonFrame.grid_propagate(0)

choice1Button = ttk.Button(buttonFrame, text="Choice 1")
choice1Button.place(relx=0.1, rely=0.5, anchor=CENTER)

choice2Button = ttk.Button(buttonFrame, text="Choice 2")
choice2Button.place(relx=0.25, rely=0.5, anchor=CENTER)

choice3Button = ttk.Button(buttonFrame, text="Choice 3")
choice3Button.place(relx=0.4, rely=0.5, anchor=CENTER)

playerFrame = ttk.Frame(root, padding=5, width=300, height=350, relief="groove")
playerFrame.grid(column=1, row=0, sticky='n')

enemyFrame = ttk.Frame(root, padding=5, width=300, height=200, relief="groove")
enemyFrame.grid(column=1, row=1, rowspan=2, sticky='s')


root.mainloop()