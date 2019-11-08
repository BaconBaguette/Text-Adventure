from time import sleep
from Funcs.usePotion import usePotion

##		IN PROGRESS - Resolves fights when they occur		##
def fightEnemy(op, e):
	max_attack = 1
	best_weapon = 'Fists'

	#	Finds the strongest weapon in the players inventory and 'equips' it	 #
	for i in op.inventory:
		if 'Weapon' in str(type(i)):
			if i.damage > max_attack:
				max_attack = i.damage
				best_weapon = i.name
			else:
				pass
		else:
			pass
	
	while op.health > 0 and e.health > 0:
		#	Only attacking works at the moment	#
		print("1 - Attack " + e.name)
		print("2 - Use Item")
		print("3 - Attempt to Flee\n")
	
		atkChoice = int(input("Enter the number that corresponds to your choice.  >"))
		print()
		
		if atkChoice == 1:
			e.health -= max_attack
			op.health -= (e.attack - op.armour)
			print("You attack the " + e.name + " with your " + best_weapon + " for " + str(max_attack) + " damage.\n")
			sleep(0.5)
			print(e.attText)
			sleep(0.5)


		elif atkChoice == 2:
			usableItems = []
			usableDict = {}
			op.uiCount = 0
			for x in op.inventory:
				if 'Potion' in str(type(x)):
					op.uiCount += 1
					usableItems.append(x)
			
			if op.uiCount > 0:
				op.uiCount = 0
				for y in usableItems:
					op.uiCount += 1
					usableDict[op.uiCount] = y

				usableDict[op.uiCount+1] = 'Cancel'

				print('You have the following potions available to use: ')
				for z in usableDict:
					sleep(0.5)
					try:
						print(z, ' - ', usableDict[z].name)
					except AttributeError:
						print(z, ' - ', usableDict[z])
				print()
				print("Enter the number that corresponds to the potion you want to use,")
				itemChoice = int(input('or cancel and make another choice > '))

				for i in usableDict:
					if itemChoice == i:
						usePotion(op, e, usableDict[i])

		if e.health < 0:
			e.health = 0				
	
		print()
		print(e.name, 'has', e.health, 'health remaining.')
		print()
		sleep(0.5)
		print('You have', op.health)
		print()

	print(e.drattle)
	print()
