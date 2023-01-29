import pygame, settings

class Shots(pygame.sprite.Sprite):
	
	def __init__(self, coordinates, shooter):
		super(Shots, self).__init__()
		self.image = pygame.Surface((4,20))
		self.image.fill('white')
		self.rect = self.image.get_rect(center=(coordinates))
		# Determine the speed accorting to the shooter
		self.__speed = settings.spaceship_shot_speeed if shooter == 'Spaceship' else settings.invader_shot_speeed
		

	# Update the movement and killing after the shot left the screen
	def update(self):
		self.rect.move_ip(0, self.__speed)
		if self.rect.top >= settings.SCREEN_HEIGHT or self.rect.bottom <= 0:
			self.kill()
