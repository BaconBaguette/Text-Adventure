from Objects.weapons import weapons
from Objects.potions import potions
from Objects.apparel import apparel

##		When called, checks item dictionaries for record matching get- then adds to player inventory		##
def getItem(op, item):
	if item.startswith("Gold"):
		op.gold += int(item[-2:])
	
	for x in weapons:
		if x == item:
			op.inventory.append(weapons[x])

	for y in potions:
		if y == item:
			op.inventory.append(potions[y])

	for z in apparel:
		if z == item:
			op.inventory.append(apparel[z])