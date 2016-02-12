import pygame
from thing import thing

class living(thing):
	def __init__(self):
		pygame.sprite.DirtySprite.__init__(self); self.dirty = 2
		self.image, self.rect = self.loadr("spr/arrow.png"); self.orig = self.image
		self.forms = []
		self.y = self.rect.y
#		self.health = 100
		self.live = True
		self.jumpvar1 = 1
		self.jumpvar2 = 3
		self.jumpvar2 = 3
		self.mask = pygame.mask.from_surface(self.image)
		self.v = 0      #It's the very vermillion velocity variable.
		self.f = 'r'    #Direction you're facing.
		self.j = False  #Jumping state
		self.y = 0      #Starting y, useful only during jumping AFAIK
		self.m = False  #Are you moving or stagnant?
	def log(self, string):
		print string
	def maskinit(self):
		self.mask = pygame.mask.from_surface(self.image)
	def scale(self, w=30, h=41): #maintain 5:7 if using the sprites I designed.
		self.image = pygame.transform.scale(self.image, [w,h])
		self.maskinit()
	def flipimageh(self):
		self.image = pygame.transform.flip(self.image, True, False)
		self.orig = self.image
	def form(self, index):
		return pygame.image.load(self.forms[index])
	def imageswap(self, switchindex, isScaled=False, w=30, h=41):
		self.image = self.form(switchindex)
		if isScaled:
			self.scale(w, h)
		else: self.maskinit()
		if self.f == 'l':
			self.flipimageh()
		self.orig = self.image
	def reversescale(self):
		self.image = self.orig
	def checkcollide(self, list):
		return self.rect.collidelistall(list)
	def left(self):
		self.rect.x = self.rect.x - 2
		self.m = True
		if self.f == 'r':
			self.flipimageh()
			self.f = 'l'
	def sprintleft(self):
		self.rect.x = self.rect.x - 4
		self.m = True
		if self.f == 'r':
			self.flipimageh()
			self.f = 'l'
	def right(self):
		self.rect.x = self.rect.x + 2
		self.m = True
		if self.f == 'l':
			self.flipimageh()
			self.f = 'r'
	def sprintright(self):
		self.rect.x = self.rect.x + 4
		self.m = True
		if self.f == 'l':
			self.flipimageh()
			self.f = 'r'
	def stopm(self):
		self.rect.x = self.rect.x
		self.m = False
	def resetJump(self):
		self.jumpvar1 = 1
		self.jumpvar2 = 3
		self.rect.y = self.y
		self.imageswap(0)
	def jump(self): #with modprev set at 2 and incrementer at 1, it can go 16 frames without modprev going into negatives.
		self.log(str(self.jumpvar1) + " = " + str(self.jumpvar2) + "^2")
		self.log(str(self.jumpvar1) + " = " + str(self.jumpvar2 * self.jumpvar2))
		if self.jumpvar2 > 0: self.jumpvar1 = self.jumpvar2 * self.jumpvar2
		else: self.jumpvar1 = -1*(self.jumpvar2 * self.jumpvar2)
		self.jumpvar2 = self.jumpvar2 - .65
		self.log("!!!" + str(self.rect.y) + " = " + str(self.rect.y) + " - " + str(self.jumpvar1))
		self.rect.y = self.rect.y - self.jumpvar1
