
##      Declaring enemy class       ##
class Enemy:
	def __init__(self, name, description, attack, health, attText, drattle, loot):
		self.name = name
		self.description = description
		self.attack = attack
		self.health = health
		self.attText = attText
		self.drattle = drattle
		self.loot = loot
	def attackPlayer(self, op):
		op.health = op.health - self.attack