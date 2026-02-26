#Classes that can be selected when making a new character

import TsObjects as TsObjects

character_classes = {
"Brute": { #Barbarian/Soldier like class thats an all-rounded basic pick
		"health": 150, 
		"speed": 5, 
		"strength": 18, 
		"mana": 12,
		"dexterity": 10,
		"equipped": {
			"weapon": "Sword",
			"armor": None}
		},
		
	"Ranger": {  #Archer class that has high speed & dexterity, but low-average armor and decreased health
		"health": 130, 
		"speed": 6, 
		"strength": 12,
		"mana": 10,
		"dexterity": 15,
		"equipped": {
			"weapon": "Bow",
			"armor": None}
		},
		 
	"Mage": {  #Wizard like class that has high affinity for mana, but lacks in other skills
		"health": 115, 
		"speed": 3, 
		"strength": 6, 
		"mana": 20,
		"dexterity": 12,
		"equipped": {
			"weapon": "Wand",
			"armor": None}
		},
		
	"Rogue": {
		"health": 115,
		"speed": 8,
		"strength": 9,
		"mana": 10,
		"dexterity": 15,
		"equipped": {
			"weapon": "Dagger",
			"armor": None}
		},
}	
###############

enemy_characters = {
		
#Enemy characters stats
	"Goblin": {
		"health": 50,
		"speed": 3,
		"strength": 4,
		"mana": 0,
		"dexterity": 5,
		"equipped": {
			"weapon": None,
			"armor": None}
		},
			
	"Skeleton": {
		"health": 55,
		"speed": 2,
		"strength": 4,
		"mana": 1,
		"dexterity": 6,
		"equipped": {
			"weapon": "Sword",
			"armor": None}
		}
	
	
}

