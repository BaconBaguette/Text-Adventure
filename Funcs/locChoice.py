##		Gets the player decision and sets player.choice = to it		##
def locChoice(op):
	if op.cCount != 0:
		ch = int(input("Enter the number that corresponds to your choice.  > "))
		print()
		while ch < 1 or ch > op.cCount:
			print("That isn't a valid entry.")
			ch = int(input("Enter the number that corresponds to your choice.  > "))
			print()
		else:
			op.choice = int(ch)