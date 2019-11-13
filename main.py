import tkinter as tk
from tkinter import ttk

from Objects.playerClass import Player

from GUI.StoryPanel import StoryPanel
from GUI.ChoicePanel import ChoicePanel
from GUI.ButtonPanel import ButtonPanel
from GUI.PlayerPanel import PlayerPanel
from GUI.EnemyPanel import EnemyPanel
from GUI.NameEntry import NameEntry

global player 

player= Player()


if __name__ == '__main__':
    loginRoot =tk.Tk()
    loginRoot.geometry("150x95")
    loginRoot.eval('tk::PlaceWindow %s center' % loginRoot.winfo_pathname(loginRoot.winfo_id()))
    
    nameWindow = NameEntry(loginRoot, player)
    loginRoot.mainloop()


    root=tk.Tk()
    root.resizable(False, False)

    storyPanel = StoryPanel(root)
    choicePanel = ChoicePanel(root)
    buttonPanel = ButtonPanel(root)
    playerPanel = PlayerPanel(root)
    enemyPanel = EnemyPanel(root)