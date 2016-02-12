import pygame

class thing(pygame.sprite.DirtySprite):
	def loadr(self, file):
		image = pygame.image.load(file)
		image = image.convert_alpha()
		return image, image.get_rect()
	def load(self, file):
		image = pygame.image.load(file)
		return image