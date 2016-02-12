import pygame
from object import object
class Sword(object):
	def __init__(self, file, type, range, speed, damage, length, yoffset):
		pygame.sprite.DirtySprite.__init__(self)
		self.dirty = 2
		self.image, self.rect = self.loadr(file)
		self.orig = self.image
		self.image2 = self.orig
		self.f = 'r'
		self.type = type
		self.range = range
		self.speed = speed
		self.damage = damage
		self.counter = 0
		self.y_offset = yoffset
