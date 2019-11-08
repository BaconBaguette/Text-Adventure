from Objects.itemClass import Item, Potion

##		Potions		##
healthPotion = Potion("Heath Potion", "A flask of.. you're not actually sure.", 12, 'heal-5', 'restore 5 health to yourself')
weakBlastPotion = Potion("Weak Blast Potion", "It says weak but you still don't want to get hit by one.", 23, 'damage-5', 'deal 5 damage to the enemy')

#	Potions Dictionary	#
potions = {
	"healthPotion":healthPotion,
	"weakBlastPotion":weakBlastPotion
}