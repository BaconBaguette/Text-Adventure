
##      Declaring multiple item classes     ##
class Item(object):
	def __init__(self, name, description, value, qty):
		self.name = name
		self.description = description
		self.value = value
		
	def __repr__(self):
		return "\t%s\n\t%s\n\tValue - %d gold" % (self.name, self.description, self.value)

class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.name = name
		self.description = description
		self.value = value
		self.damage = damage

	def __repr__(self):
		return "\t%s\n\t%s\n\tDamage - %s\n\tValue - %d gold" % (self.name, self.description, self.damage, self.value)

class Potion(Item):
	def __init__(self, name, description, value, effect, effText):
		self.name = name
		self.description = description
		self.value = value
		self.effect = effect
		self.effText = effText
		
class Apparel(Item):
	def __init__(self, name, description, value, armour, effect, effText):
		self.name = name
		self.description = description
		self.value = value
		self.armour = armour
		self.effect = effect
		self.effText = effText
