import pygame, settings

class Block(pygame.sprite.Sprite):
	
	def __init__(self, coordinates):
		super(Block, self).__init__()
		self.image = pygame.Surface((settings.size_block, settings.size_block))
		self.image.fill(settings.color_block)
		self.rect = self.image.get_rect(center=(coordinates))
