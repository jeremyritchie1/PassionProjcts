import pygame
import TsObjects
import TsCharacters

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Thornspire")

clock = pygame.time.Clock()

	
player = {"x": 400, "y": 300, "speed": 0, "health": 0, "max_health": 0,
		   "strength": 0, "mana": 0, "dexterity": 0, 
		   "equipped": {"weapon": None, "armor": None}
}

camera = {"x": 0, "y": 0}

def select_class(chosen_class):
	player["health"] = TsCharacters.character_classes[chosen_class]["health"]
	player["speed"] = TsCharacters.character_classes[chosen_class]["speed"]
	player["strength"] = TsCharacters.character_classes[chosen_class]["strength"]
	player["mana"] = TsCharacters.character_classes[chosen_class]["mana"]
	player["dexterity"] = TsCharacters.character_classes[chosen_class]["dexterity"]
	player["equipped"] = TsCharacters.character_classes[chosen_class]["equipped"]

	print(f"{chosen_class} selected!")


def update_camera():
	camera["x"] = player["x"] - 400
	camera["y"] = player["y"] - 300
	
select_class("Mage")
print(player)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			
	#Keyboard movement		
	keys = pygame.key.get_pressed()
	if keys[pygame.K_w]:
		player["y"] -= player["speed"]
	if keys[pygame.K_s]:
		player["y"] 	+= player["speed"]
	if keys[pygame.K_a]:
		player["x"] -= player["speed"]
	if keys[pygame.K_d]:
		player["x"] += player["speed"]	
		
	update_camera() #Moved camera with player movement

	#map draw function
	def draw_map():
		for row_index, row in enumerate(TsObjects.map_data):
			for col_index, tile in enumerate(row):
				#calculates where the tile is on the map
				tile_x = col_index * TsObjects.TILE_SIZE - camera["x"]
				tile_y = row_index * TsObjects.TILE_SIZE - camera["y"]
			
				if tile == 1:
					pygame.draw.rect(screen, (100, 100, 100), (tile_x, tile_y, TsObjects.TILE_SIZE, TsObjects.TILE_SIZE))
				elif tile == 0:
					pygame.draw.rect(screen, (50, 35, 20), (tile_x, tile_y, TsObjects.TILE_SIZE, TsObjects.TILE_SIZE))

	#drawing
	screen.fill((0, 0, 0))
	draw_map()

	pygame.draw.rect(screen, (180, 30, 30), (player["x"] - camera["x"], player["y"] - camera["y"], 24, 24))
	pygame.draw.rect(screen, (255, 255, 255), (800 - camera["x"], 400 - camera["y"], 32, 32))

	pygame.display.flip()
	
	clock.tick(60)

pygame.quit()