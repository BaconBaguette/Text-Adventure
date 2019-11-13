from time import sleep
import csv

from Objects.enemies import *
from Objects.playerClass import *

from Objects.weapons import *
from Objects.potions import *
from Objects.apparel import *

from Funcs.fightEnemy import fightEnemy
from Funcs.getItem import getItem
from Funcs.locChoice import locChoice
from Funcs.locIntro import locIntro
from Funcs.locShowChoices import locShowChoices
from Funcs.splitOutcome import splitOutcome
from Funcs.winCheck import winCheck

##		Initializing the player		##
player = Player()

#		Main game loop		##
def game():
	player.name = input("What do they call you?  > ")
	print()
	
	while player.won==False:

		locIntro(player)

		winCheck(player)
		
		print()

		locShowChoices(player)

		locChoice(player)

		print()

		splitOutcome(player)

	print("This is where your adventure ends.")
	
player.inventory.append(healthPotion)
player.inventory.append(weakBlastPotion)

game()

#fightEnemy(player, barPatron)

input("\n\n\nPress ENTER to exit")