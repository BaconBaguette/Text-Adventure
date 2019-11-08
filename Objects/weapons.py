from Objects.itemClass import Item, Weapon

dagger = Weapon("Dagger", "A small side-arm, suitable for poking.", 9, 3)
hammer = Weapon("Hammer", "Made for whacking", 8, 4)
sword = Weapon("Sword", "Not very well looked after but it works.", 15, 5)

#	Weapons Dictionary	#
weapons = {	
	"dagger":dagger,
	"sword":sword,
	"hammer":hammer
}