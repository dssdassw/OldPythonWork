import pygame
from thing import thing
#formerly named "clean_player" because it's a lot cleaner than it once was.

class living(thing):
	def __init__(self, form_list):
		pygame.sprite.DirtySprite.__init__(self); self.dirty = 2
		self.image, self.rect = self.loadr("spr/arrow.png"); self.orig = self.image
		self.forms = form_list
		self.y = self.rect.y
		self.health = 100
		self.living = True
		self.jumpvar1 = 1
		self.jumpvar2 = 3
		self.jumpvar2 = 3
		self.mask = pygame.mask.from_surface(self.image)
		self.f = 'r'    #Direction you're facing.
		self.j = False  #Jumping state
		self.y = 0      #Starting y, useful only during jumping.
		self.x = 0      #Starting x, useful only during sliding.
		self.m = False  #Are you moving or stagnant?
		self.sframes = 0
		self.sliding = False
	def log(self, string):
		print string
	def maskinit(self):
		self.mask = pygame.mask.from_surface(self.image)
	def scale(self, w=30, h=41): #maintain 5:7 if using the sprites I designed.
		self.image = pygame.transform.scale(self.image, [w,h])
		self.maskinit()
	def flipimageh(self):
		self.image = pygame.transform.flip(self.image, True, False)
	def fliph(self, image):
		return pygame.transform.flip(image, True, False)
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
	def left(self):
		self.rect.x = self.rect.x - 1
		self.m = True
		if self.f == 'r':
			self.flipimageh()
			self.f = 'l'
	def sprintleft(self, speed):
		self.rect.x = self.rect.x - 1 * speed
		if self.f == 'r':
			self.flipimageh()
			self.f = 'l'
	def right(self):
		self.rect.x = self.rect.x + 1
		self.m = True
		if self.f == 'l':
			self.flipimageh()
			self.f = 'r'
	def sprintright(self, speed):
		self.rect.x = self.rect.x + 1 * speed
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
	def jump(self):
		if self.jumpvar2 > 0: self.jumpvar1 = self.jumpvar2 * self.jumpvar2
		else: self.jumpvar1 = -1*(self.jumpvar2 * self.jumpvar2)
		self.jumpvar2 = self.jumpvar2 - .20 #lower number, higher jump.
		self.rect.y = self.rect.y - self.jumpvar1
		if self.y < self.rect.y: self.rect.y = self.y
	def resetSlide(self):
		self.sframes = 0
		self.sliding = False
	def slide(self, f, framelimit = 25):
		if self.sframes < framelimit:
			if f == 'l':
				self.rect.x = self.rect.x - 3
			else:
				self.rect.x = self.rect.x + 3
			self.sframes = self.sframes + 1
			self.sliding = True
		else:
			self.resetSlide()