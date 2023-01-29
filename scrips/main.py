import pygame, settings, Management

def main():

	LIVES = settings.LIVES
	score = 0
	
	# Initialize the screen and game music
	clock = Management.initialize()
	
	# Game prossers each level:
	level = 1
	
	play = True
	while play:
		
		# Initialize background and loops events for alien_ship and random invader shot
		background, ADDSHOT, ADDSHIP, start_ticks, space_ticks = Management.initialize_each_level(level)
		
		# Creat the objects and groups for the level
		all_sprites, list_of_groups, spaceship, all_invaders = Management.create_groups_and_objects(level)
		
		# Start the game
		running = True

		while running:
			
			# Check the event QUIT and creat alien_ship and random invader shot
			events = pygame.event.get()
			running, play = Management.check_general_events(events, ADDSHOT, ADDSHIP, running, play, list_of_groups, all_sprites, all_invaders)
			
			# Check the keyboard events and updating the game accordingly
			space_ticks, running, play = Management.update_pressed_keys(running, play, space_ticks, list_of_groups[2], spaceship, all_sprites)
			
			# Uptates the objects movement in the game
			Management.update(all_invaders, list_of_groups, level)
			
			# Uptates the collisions and scoring
			score, messages_group = Management.check_collisions(list_of_groups, all_invaders, score)
			
			# Check the game status win/lose/life lose
			running, play, LIVES = Management.game_status(spaceship, all_invaders, list_of_groups, running, play, LIVES)
			
			# Display the game on the screen
			Management.display(start_ticks, background, all_sprites, level, LIVES, score, messages_group)
			clock.tick(30)
			
		# Level up
		LIVES, score, level, play = Management.level_up(LIVES, score, level, play)
		
	# Close the music
	pygame.mixer.music.stop()
	pygame.mixer.quit()

if __name__ == '__main__':
	main()
	
