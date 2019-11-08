import csv

##		Checks if the current location is a winning one, and sets player.won to True if it is		##
def winCheck(op):
	with open('loc.csv', encoding='utf-8') as loc_file:
		loc_reader = csv.reader(loc_file, delimiter=';')
		for entry in loc_reader:
			if entry[0] == str(op.locationID) and entry[20] == str(1):
				op.won = True
			else:
				pass