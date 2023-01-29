import pygame, settings
from Spaceship import Spaceship
from Shots import Shots
from Invaders import Invaders
from AlienShip import AlienShip
from Block import Block

# Initialize the pygame, screen and music game
def initialize():

	pygame.init()

	# Initialize the screen, clock and game music
	clock = pygame.time.Clock()
	screen = settings.screen
	pygame.display.set_caption('Space Invaders')
	
	# Printing massage to start
	massage('To start press space', pygame.K_SPACE)
	
	return clock


# Initialize background and loops events for alien_ship and random invader shot
def initialize_each_level(level):
	
	pygame.mixer.music.load(settings.bacground_music[level])
	pygame.mixer.music.play(loops=-1)
	
	# Initialize the background image of the screen
	background = pygame.image.load(settings.background_image[level])
	background = pygame.transform.scale(background, (settings.SCREEN_WIDTH,settings.SCREEN_HEIGHT))
	
	# Initialize an event for a loop of a random invader shot and alien_ship
	ADDSHOT = set_event_timer(settings.invaders_loop_shots[level], 1)
	ADDSHIP = set_event_timer(settings.alien_ship_loop_shots, 2)
	
	# Save the time of the start of the game
	start_ticks = pygame.time.get_ticks()
	space_ticks = start_ticks

	# Printing massage level
	settings.screen.blit(background, (0,0))
	massage(f'level {level}', pygame.K_SPACE)
	return background, ADDSHOT, ADDSHIP, start_ticks, space_ticks
	

# Set event with timer
def set_event_timer(miliseconds, i):
	EVENT = pygame.USEREVENT + i
	pygame.time.set_timer(EVENT, miliseconds)
	return EVENT


# Creat the objects and groups for the level
def create_groups_and_objects(level):

	# Initialize the invaders, shots, spaceship_shots, alien_ships and all_sprites groups
	all_sprites = pygame.sprite.Group()
	invaders = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	spaceship_shots = pygame.sprite.Group()
	alien_ships = pygame.sprite.Group()
	blocks = pygame.sprite.Group()
		
	# Creating the spaceship and adding into the all_sprites group
	spaceship = Spaceship()
	all_sprites.add(spaceship)
	
	# Creating the all_invaders and obstacles, and adding them to their groups
	all_invaders = Invaders(level)
	all_invaders.add_groups(all_sprites, invaders)
	create_multiple_obstacles(blocks, all_sprites)
	
	list_of_groups = [invaders, shots, spaceship_shots, alien_ships, blocks]
	
	return all_sprites, list_of_groups, spaceship, all_invaders


# Creating create multiple obstacles
def create_multiple_obstacles(blocks, all_sprites):
	for x, y in zip(settings.x_points, settings.y_points):
		create_obstacle(x, y, blocks, all_sprites)


# Create one obstacle according to given axes 
def create_obstacle(x_start, y_start, blocks, all_sprites):
	for row_index, row in enumerate(settings.shape):
		for col_index, col in enumerate(row):
			if col == 'X':
				x = x_start + col_index * settings.size_block
				y = y_start + row_index * settings.size_block
				block = Block((x,y))
				blocks.add(block)
				all_sprites.add(block)
			
# Check the keyboard events and updating the game accordingly
def check_general_events(events, ADDSHOT, ADDSHIP, running, play, list_of_groups, all_sprites, all_invaders):
	for event in events:
		# Check if the player close the game
		if event.type == pygame.QUIT:
			running = False
			play = False
	
		# Creating new random invader shot
		elif event.type == ADDSHOT:
			random_invader_shot(all_invaders, list_of_groups[1], all_sprites)
		
		# Creating new alien_ship
		elif event.type == ADDSHIP:
			new_alien_ship = AlienShip()
			all_sprites.add(new_alien_ship)
			list_of_groups[3].add(new_alien_ship)
	return running, play
	

# Uptates the objects movement in the game
def update_pressed_keys(running, play, space_ticks, spaceship_shots, spaceship, all_sprites):
	
	# Get pressed_keys
	pressed_keys = pygame.key.get_pressed()
	
	# Update spaceship movement
	spaceship.update(pressed_keys)
	
	# Dedine a limit of the spaceship shots (time limit and quantity limit)
	limit_spaceship_shots = (pygame.time.get_ticks()-space_ticks) > settings.spaceship_shot_time_limit and len(spaceship_shots) < settings.spaceship_shot_quantity_limit
			
	# If the player press k_space and there is no a limit create spaceship shot
	if pressed_keys[pygame.K_SPACE] and limit_spaceship_shots:
		space_ticks = pygame.time.get_ticks()
		spaceship.spaceship_shot(spaceship_shots, all_sprites)
	
	if pressed_keys[pygame.K_p]:
		massage('Pause!', pygame.K_SPACE)
	
	# If the player press K_ESCAPE close the game
	if pressed_keys[pygame.K_ESCAPE]:
		running = False
		play = False
	
	# Back door to the next level
	if pressed_keys[pygame.K_LCTRL] and pressed_keys[pygame.K_LSHIFT]:
		running = False
	return space_ticks, running, play
	

# adding a random invader shot
def random_invader_shot(all_invaders, shots, all_sprites):
	place_shoot = all_invaders.shooter()
	new_shot = Shots(place_shoot, 'Invaders')
	settings.shots_sound.play()
	shots.add(new_shot)
	all_sprites.add(new_shot)


# Uptates the objects movement in the game
def update(all_invaders, list_of_groups, level):
	all_invaders.update(level)
	list_of_groups[1].update()
	list_of_groups[2].update()
	list_of_groups[3].update()


# Uptates the collisions and scoring
def check_collisions(list_of_groups, all_invaders, score):
	messages_group = []
	# Extract the groups from the list
	invaders, shots, spaceship_shots, alien_ships, blocks = list_of_groups
	
	# Check (and kill) collisions between spaceship_shots and other sprites
	for shot in spaceship_shots:
		
		list_of_blocks_collidets = pygame.sprite.spritecollide(shot, blocks, True)
		list_of_shots_collidets = pygame.sprite.spritecollide(shot, shots, True)
		list_of_alien_ships_collidets = pygame.sprite.spritecollide(shot, alien_ships, True)
		list_of_invaders_collidets = pygame.sprite.spritecollide(shot, invaders, True)
		all_invaders.kill_in_collide(list_of_invaders_collidets)
		
		# Updates score
		if list_of_invaders_collidets:
			score += sum([invader.score for invader in list_of_invaders_collidets])
		if list_of_shots_collidets:
			score += settings.shot_score * len(list_of_shots_collidets)
		if list_of_alien_ships_collidets:
			
			alien_score = [alien.score for alien in list_of_alien_ships_collidets]
			score += sum(alien_score)
			crnter = [alien.rect.center for alien in list_of_alien_ships_collidets]
			[show_in_game(f'{score}', center, settings.dinamic_massage_font, 100, messages_group) for score, center in zip(alien_score, crnter)]

		
		# Kill the shot
		if list_of_shots_collidets or list_of_invaders_collidets or list_of_alien_ships_collidets or list_of_blocks_collidets:
			settings.shots_sound.stop()
			settings.collision_sound.play()
			shot.kill()
	
	# Check (and kill) collisions between shots and other sprites
	for  shot in shots:
		list_of_blocks_collidets = pygame.sprite.spritecollide(shot, blocks, True)
		if list_of_blocks_collidets:
			settings.shots_sound.stop()
			settings.collision_sound.play()
			shot.kill()
	
	# Check collisions between invaders and blocks and kill the blocks if was a collision
	for  invader in invaders:
		list_of_blocks_collidets = pygame.sprite.spritecollide(invader, blocks, True)
		if list_of_blocks_collidets:
			[block.kill() for block in blocks]

	return score, messages_group


# Check the game status win/lose/lose life
def game_status(spaceship, all_invaders, list_of_groups, running, play, LIVES):

	# Extract the groups from the list
	invaders, shots, = list_of_groups[0], list_of_groups[1]
	
	# Check collisions between spaceship and invaders shots
	list_of_collidets = pygame.sprite.spritecollide(spaceship, shots, True)
	if list_of_collidets:
		settings.shots_sound.stop()
		settings.collision_sound.play()
		LIVES -=1
		# repositioning of the spaceship after collision 
		spaceship.new_game()
	# Chcking if the game is over
		# case 1 : LIVES == 0
		if LIVES == 0: 
			massage('Game Over!', pygame.K_KP_ENTER)
			running = False
			play = False
			spaceship.kill()
		else:
			massage('Let\'s try again', pygame.K_KP_ENTER)
				
	# case 2: invaders collided in spaceship or out of screen	
	elif pygame.sprite.spritecollideany(spaceship, invaders) or all_invaders.out_of_screen():
		settings.shots_sound.stop()
		settings.collision_sound.play()
		massage('Game Over!', pygame.K_KP_ENTER)
		running = False
		play = False
		spaceship.kill()
	
	# Chcking if the player win the level	
	elif not invaders:
		massage('You Win !!', pygame.K_KP_ENTER)
		running = False
	return running, play, LIVES
	
# Display the game on the screen
def display(start_ticks, background, all_sprites, level, LIVES, score, messages_group):
	
	# Draw the background, all sprites and dynamic information
	screen = settings.screen
	screen.blit(background, (0,0))
	
	all_sprites.draw(screen)
	
	seconds = (pygame.time.get_ticks() - start_ticks)//1000
	show_in_game(f'Level {level}', (100, 15), settings.dinamic_massage_font, settings.dinamic_massage_size, messages_group)
	show_in_game(f'Time of the game: {seconds}', (100, 50), settings.dinamic_massage_font, settings.dinamic_massage_size, messages_group)
	show_in_game(f'Lives: {LIVES}', (100, 85), settings.dinamic_massage_font, settings.dinamic_massage_size, messages_group)
	show_in_game(f'Score: {score}', (100, 120), settings.dinamic_massage_font, settings.dinamic_massage_size, messages_group)
	
	[screen.blit(surf[0], surf[1]) for surf in messages_group]
	
	pygame.display.flip()


# Level up
def level_up(LIVES, score, level, play):
	LIVES += 1
	score += 1000 * level
	level += 1
	pygame.mixer.music.stop()
	if level == 5 and play:
		mass = []
		show_in_game(f'Your score is: {score}', (settings.SCREEN_WIDTH // 2 -180, settings.SCREEN_HEIGHT // 2 +50), settings.score_massage_font, settings.score_massage_size, mass)
		settings.screen.blit(mass[0][0], mass[0][1])
		massage('Well Done !!', pygame.K_ESCAPE)
		play = False
	return LIVES, score, level, play

# Massage on all the screen
def massage(massage, key_press):
	pressed_keys = pygame.key.get_pressed() 
	while not pressed_keys[key_press]:
		for event in pygame.event.get():
			pressed_keys = pygame.key.get_pressed() 
			font = pygame.font.Font(settings.screen_massage_font, settings.screen_massage_size)
			text = font.render(massage, True, (255, 255, 255))
			textRect = text.get_rect()
			textRect.center = (settings.SCREEN_WIDTH // 2, settings.SCREEN_HEIGHT // 2)
			settings.screen.blit(text, textRect)
			pygame.display.flip()


# Dinamic massage on the screeen 
def show_in_game(massege, location, font, size, messages_group):
	font = pygame.font.Font(font, size)
	text = font.render(massege, True, (102, 102, 255))
	textRect = text.get_rect(topleft = location)
	messages_group.append((text, textRect))
	

