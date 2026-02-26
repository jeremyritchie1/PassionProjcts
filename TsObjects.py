
#Dictionary for weapon items - includes rarity, drop chance
#####FOR RARITY#####
#Ordinary = Common
#Precious = Rare
#Eminent = Legendary

weapon_items = {
"Sword": {"rarity":
			["Ordinary", "Precious", "Eminent"],
		"drop_chance": 
			 [65, 30, 5] },

"Bow": {"rarity": 
			["Ordinary", "Precious", "Eminent"],
		"drop_chance": 
			[65, 30, 5] },

"Wand": {"rarity": 
			["Ordinary", "Precious", "Eminent"],
		"drop_chance": 
			[65, 30, 5] },

"Dagger": {"rarity": 
			["Ordinary", "Precious", "Eminent"],
		"drop_chance": 
			[65, 30, 5] }
}

#Dictionary for armor items - includes rarity
armor_items = {
#Chest/Torso armor
"Breastplate": {"rarity": ["Ordinary", "Precious", "Eminent"] },

#Head armor
"Helmet": {"rarity": ["Ordinary", "Precious", "Eminent"] },

#Armor for feet, eventually can dictate speed stats
"Boots": {"rarity": ["Ordinary", "Precious", "Eminent"] },

#Can only be equipped with One-Handed weapons
"Shield": {"rarity": ["Ordinary", "Precious", "Eminent"] },

#Armor for arms
"Greaves": {"rarity": ["Ordinary", "Precious", "Eminent"] }
}

#Dictionary for special items - includes size
#Items like potions, modifiers, rings/amulets(?)
special_items = {
"Health Potion": {"size": ["Small", "Medium", "Large"] },

"Mana Potion": {"size": ["Small", "Medium", "Large"] },

"Speed Potion": {"size": ["Small", "Medium", "Large"] },

"Strength Potion": {"rarity": ["Ordinary", "Precious"] }, #NOT SOLD ON THE IDEA OF RARITY
#MIGHT USE SMALL-LARGE OR JUST A BASE POTION SIZE

"Dexterity Potion": {"rarity": ["Ordinary", "Precious"] }, #NOT SOLD ON THE IDEA OF RARITY
#MIGHT USE SMALL-LARGE OR JUST A BASE POTION SIZE

"Glove of Holding": {} #RESEARCH GLOVE OF HOLDING & WHAT IT DOES
}

#Dictionary for currency
#Gold is used for purchasing basic items from shops
#Moonstone can be used for special upgrades of basic items or buying "Eminent" items
currency = {"Gold Piece": 0, 
			"Moonstone": 0
			}


##MAP TILES
# 0 = Space
# 1 = Wall

map_data = [
	[1,1,1,1,1,1,1,1,1,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,0,0,0,0,0,0,0,0,1],
	[1,1,1,1,1,1,1,1,1,1]
	]

TILE_SIZE = 32
