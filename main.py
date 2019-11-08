import tkinter as tk
from tkinter import ttk

from Objects.playerClass import Player

from GUI.StoryPanel import StoryPanel
from GUI.ChoicePanel import ChoicePanel
from GUI.ButtonPanel import ButtonPanel
from GUI.PlayerPanel import PlayerPanel
from GUI.EnemyPanel import EnemyPanel

player = Player()


if __name__ == '__main__':
    root=tk.Tk()
    root.resizable(False, False)

    storyPanel = StoryPanel(root)
    choicePanel = ChoicePanel(root)
    buttonPanel = ButtonPanel(root)
    playerPanel = PlayerPanel(root)
    enemyPanel = EnemyPanel(root)

    root.mainloop()