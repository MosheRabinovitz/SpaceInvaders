import pygame, settings
from Shots import Shots

class Spaceship(pygame.sprite.Sprite):
	
	
	def __init__(self):
		super(Spaceship, self).__init__()
		# Initialize the form of the spaceship
		self.image = pygame.image.load(settings.spaceship_image)
		self.image = pygame.transform.scale(self.image, (60,60))
		self.location = {'midbottom' : (settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT-5)}
		self.rect = self.image.get_rect(**self.location)
	
	
	# Update the movement acording to the pressed keys of the player
	def update(self, pressed_keys):
		if pressed_keys[pygame.K_LEFT]:
			self.rect.move_ip(-settings.spaceship_speed, 0)
		if pressed_keys[pygame.K_RIGHT]:
			self.rect.move_ip(settings.spaceship_speed, 0)

		# Determine the limit movement to screen size
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > settings.SCREEN_WIDTH:
			self.rect.right = settings.SCREEN_WIDTH
			
	
	# Create a object of spaceship shot and add it to spaceship_shots and all_sprites grops
	def spaceship_shot(self, spaceship_shots, all_sprites):
		place_shoot = self.rect.midtop
		new_shot = Shots(place_shoot, 'Spaceship')
		settings.shots_sound.play()
		spaceship_shots.add(new_shot)
		all_sprites.add(new_shot)
			
			
	# Update the posision of the spaceship to the start point
	def new_game(self):
		self.rect = self.image.get_rect(**self.location)
		
