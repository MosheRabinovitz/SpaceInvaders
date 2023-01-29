import pygame, random, settings

# Class of all invaders
class Invaders(pygame.sprite.Sprite):
	
	def __init__(self, level):
		super(Invaders, self).__init__()
		# Get/set the speed of the axis
		self.speed = settings.invaders_speed_movement[level]
		self.hieght_direction = 0
		# Creation the invaders in diffrent locations and colors
		self.__invaders = []
		images = settings.aliens_images
		score = settings.shot_invader_score
		
		for i, image, sc in zip(range(settings.SCREEN_HEIGHT//6, settings.SCREEN_HEIGHT//2, 60), images, score):
			for j in range(200, settings.SCREEN_WIDTH-150, 65):
				new_invader = Invader(j, i, image, sc)
				self.__invaders.append(new_invader)
	
	# Update the movement of the invaders
	def update(self, level):
		change_height = False
		# Checing if need to change direction in the axis
		for invader in self.__invaders:
			if invader.rect.left <= 0 or invader.rect.right >= settings.SCREEN_WIDTH:
				self.speed = -self.speed
				self.hieght_direction = settings.invaders_hieght_direction[level]
				change_height = True
				break
				
		if not change_height:
			self.hieght_direction = 0
		
		# Call to function of the movement of each invader
		for invader in self.__invaders:
			invader.update(self.speed, self.hieght_direction)
	
	# Adding each invader to the groups 
	def add_groups(self, invaders, all_sprites):
		for invader in self.__invaders:
			all_sprites.add(invader)
			invaders.add(invader)
		
	# chooses a random invader to shoot
	def shooter(self):
		shooter = random.randint(0, len(self.__invaders)-1)
		place_shoot = self.__invaders[shooter].rect.center
		return place_shoot

	
	# Kill the invader after collision
	def kill_in_collide(self, list_of_collidets):
		for invader in list_of_collidets:
			self.__invaders.remove(invader)
			invader.kill()

	def out_of_screen(self):
		for invader in self.__invaders:
			if invader.rect.bottom >= settings.SCREEN_HEIGHT:
				return True
		return False

# Class of one invader
class Invader(pygame.sprite.Sprite):
	
	# initialize invader acording to width, height and image that obtain fron invaders class
	def __init__(self, width, height, image, score):
		super(Invader, self).__init__()
		self.image = pygame.image.load(image)
		self.image = pygame.transform.scale(self.image, (50,40))
		self.rect = self.image.get_rect(center=(width, height))
		self.score = score
	
	
	# Update the movement of the invader
	def update(self, speed, hieght_direction):
		self.rect.move_ip(speed, hieght_direction)
		
			
			
			
			
