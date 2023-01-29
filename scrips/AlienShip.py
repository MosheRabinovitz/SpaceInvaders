import pygame, random, settings

class AlienShip(pygame.sprite.Sprite):
	
	# initialize invader acording to width, height and image that obtain fron invaders class
	def __init__(self):
		super(AlienShip, self).__init__()
		self.score = random.choice(settings.alien_ship_score)
		self.image = pygame.image.load(settings.alien_ship)
		self.image = pygame.transform.scale(self.image, (100,50))
		width_location = random.choice([0,settings.SCREEN_WIDTH])
		self.rect = self.image.get_rect(midtop = (width_location, 10))
		self.__speed = settings.alien_ship_speed if width_location == 0 else -settings.alien_ship_speed
		
	
	
	# Update the movement of the alien_ship
	def update(self):
		self.rect.move_ip(self.__speed, 0)
		if self.rect.right > settings.SCREEN_WIDTH+50 or self.rect.left < -50:
			self.kill()
