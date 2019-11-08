import csv
from time import sleep

##		Prints the story text to the screen for the players current location		##
def locIntro(op):
	with open('loc.csv', encoding='utf-8') as loc_file:
		loc_reader = csv.reader(loc_file, delimiter=';')
		for entry in loc_reader:
			if entry[0] == str(op.locationID):
				for x in range(2, 11):
					if entry[x] != '':
						print(entry[x].replace('playername', op.name), '\n')
						sleep(0.5)
					else:
						pass
			else:
				pass