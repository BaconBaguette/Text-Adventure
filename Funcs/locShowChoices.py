import csv

##		Loops through the available choices and prints them to the screen. Also sets cCount = number of choices		##
def locShowChoices(op):
	with open('loc.csv', encoding='utf-8') as loc_file:
		loc_reader = csv.reader(loc_file, delimiter=';')
		op.cCount = 0
		for entry in loc_reader:
			if entry[0] == str(op.locationID):
				for x in range(11, 14):
					if entry[x+6] == str(1):
						op.cCount += 1
						print(op.cCount, ' - ', entry[x], '\n')
					else:
						pass
			else:
				pass
            