import csv
from Funcs.getItem import getItem
from Funcs.fightEnemy import fightEnemy
from Objects.enemies import enemies

##		Splits the outcome of the location then actions them. Gives items and moves the player at current		##
def splitOutcome(op):
	moved = False
	with open('loc.csv', encoding='utf-8') as loc_file:
		loc_reader = csv.reader(loc_file, delimiter=';')
		for entry in loc_reader:
			if entry[0] == str(op.locationID):
				olist = entry[13 + op.choice].split(',')
				#for x in entry[13 + op.choice].split(' '):
				for o in olist:
						if (o.split('-')[0]) == 'get':
							getItem(op, o.split('-')[1])
							print(o.split('-')[2])
							print()

						if (o.split('-')[0]) == 'fight':
							fightEnemy(op, enemies[o.split('-')[1]])
##		This part of the function has been causing problems, something to keep an eye on		##
				while moved == False and op.won == False:
##		----------------------------------------------------------------------------------		##
					if (o.split('-')[0]) == 'goto':
						op.locationID = int(o.split('-')[1])
						moved = True
					else:
						pass
			else:
				pass