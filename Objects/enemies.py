from Objects.enemyClass import Enemy
from Objects.weapons import *
from Objects.potions import *
from Objects.apparel import *

barPatron = Enemy("Bar Patron", "One of the bits of furniture at this point.", 1, 6, "He stabs with his dagger for 1 damage.", "The man falls to the ground, he still hasn't let go of his beer.", "Dagger")
childOfTheSpider = Enemy("Unkown", "You really shouldn't be messing with this guy.", 5, 10, "", "", "Amulet of The Spider")

enemies = {
    "barPatron":barPatron,
    "childOfTheSpider":childOfTheSpider
}