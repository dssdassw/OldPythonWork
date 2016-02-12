import pygame

class allspr(pygame.sprite.RenderUpdates):
	def __init__(self):
		pygame.sprite.RenderUpdates.__init__(self)

class humans(pygame.sprite.Group):
	def __init__(self):
		pygame.sprite.Group.__init__(self)