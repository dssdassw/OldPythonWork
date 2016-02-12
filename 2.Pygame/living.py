import pygame
from object import object

class living(object):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self)
		self.dirty = 2
		self.image, self.rect = self.loadr("spr/arrow.png")
		self.rect.y = 225
		self.modprev = 0
		self.health = 100
		self.live = True
		self.orig = self.image
		self.incrementer = 0
		self.framecount = 0
		self.v = 0      #It's the very vermillion velocity variable.
		self.f = 'r'    #Direction you're facing.
		self.j = 'still'#Jumping state
		self.y = None   #Starting y, useful only during jumping AFAIK
		self.m = False  #Are you moving or stagnant?
	def scale(self):
		self.image = pygame.transform.scale2x(self.image)
		self.sword.image = pygame.transform.scale2x(self.sword.image)
	def reversescale(self):
		self.image = self.orig
		self.sword.image = self.sword.orig
	def extend(self):
		print self.rect.h
		self.rect.h = self.rect.h + self.sword.range
		self.sword.orig = self.sword.image
		print self.rect.h
	def detract(self):
		self.rect.h = self.origh
	def checkcollide(self, list):
		return self.rect.collidelistall(list)
	def swordfix(self):
		if self.f == 'r':
			self.sword.rect.x = self.rect.x + 7
			if self.sword.f != 'r':
				self.sword.f = 'r'
				self.sword.image = pygame.transform.flip(self.sword.image, True, False)
		if self.f == 'l':
			self.sword.rect.x = self.rect.x-1
			if self.s == True:
				self.sword.rect.x = self.sword.rect.x - self.temp
				self.temp2 = self.temp2 + 1
				self.temp = self.temp + self.temp2
			else: self.temp = 0; self.temp2 = 3
			if self.sword.f != 'l':
				self.sword.f = 'l'
				self.sword.image = pygame.transform.flip(self.sword.image, True, False)
		self.sword.rect.y = self.rect.y + self.sword.y_offset
	def left(self):
		self.rect.x = self.rect.x - 2
		self.m = True
		if self.f == 'r':
			self.image = pygame.transform.flip(self.image, True, False)
			self.f = 'l'
			self.orig = self.image
	def sprintleft(self):
		self.rect.x = self.rect.x - 4
		self.m = True
		if self.f == 'r':
			self.image = pygame.transform.flip(self.image, True, False)
			self.f = 'l'
			self.orig = self.image
	def right(self):
		self.rect.x = self.rect.x + 2
		self.m = True
		if self.f == 'l':
			self.image = pygame.transform.flip(self.image, True, False)
			self.f = 'r'
			self.orig = self.image
	def sprintright(self):
		self.rect.x = self.rect.x + 4
		self.m = True
		if self.f == 'l':
			self.image = pygame.transform.flip(self.image, True, False)
			self.f = 'r'
			self.orig = self.image
	def stopm(self):
		self.rect.x = self.rect.x
		self.m = False
	def jump(self):
		if self.j == 'still':
			self.j = 'rising'
			self.y = self.rect.y
			self.modprev = 0; self.v = 0; self.incrementer = 1; self.framecount = 0
		if self.j == 'rising':
			if self.framecount != 10:
				print self.framecount
				self.framecount = self.framecount + 1
				self.modprev = self.modprev + 3
				self.v = self.v - (self.incrementer*1.5)
				self.rect.y = self.rect.y - (self.v + self.modprev)
			elif self.framecount >= 10:
				self.j = 'falling'
				self.incrementer = 0; self.modprev = 0
		if self.j == 'falling':
			if self.framecount != 0:
				print self.framecount
				self.framecount = self.framecount - 1
				self.modprev = self.modprev + 3
				self.v = self.v + (self.incrementer*1.5)
				self.rect.y = self.rect.y + (self.v - self.modprev)
			elif self.framecount <= 0:
				self.v = 0; self.modprev = 0; self.incrementer = 1
				self.rect.y = self.y
				self.j = 'still'