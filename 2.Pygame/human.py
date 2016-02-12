import time
print "agent: time imported!"
import pygame
print "agent: pygame imported!"
import pygame.mixer
print "agent: mixer imported!"
from fileops import *
print "agent: fileops imported!"

#point of gun location: facing left = origin(+5, +4); facing right = origin(+20, +4)

class human(pygame.sprite.Sprite):
	def __init__(self, file0, file1, file2, file3, screen):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = globalload(file0)
		self.calmfile = file0
		self.waryfile = file1
		self.firefile = file2
		self.kickfile = file3
		self.alive = True
		self.channel = pygame.mixer.find_channel()
		#self.aaAaa = pygame.mixer.Sound("snd/WilhelmScream.ogg")
		self.shot = pygame.mixer.Sound("snd/gunshot.ogg")
		self.f = 0 #start facing left.
		self.d = None
		self.jof = -1
		self.jof = 0
		self.state = 0#standing
		self.velocity = 0#no velocity, obviously.
		screen = pygame.display.get_surface()
		self.area = pygame.Surface(self.rect.size)
		screct = screen.get_rect()
		backgr = pygame.Surface(screct.size)
		self.orig = self.image
		self.shootstg = 0
		self.tmpstore = None
		self.tmpstore2= None
		self.bullet = pygame.Rect(0, 0, 1, 1)#unimportant, unimportant, WIDTH, HEIGHT
		self.displbullet = pygame.Surface(self.bullet.size)
		self.displbullet.fill((255,255,255))

	def turn(self, explicit = 42):
		if explicit == 0:
			self.f = 0
			self.image = self.orig
			explicit = 42
		elif explicit == 1:
			self.f = 1
			self.image = pygame.transform.flip(self.orig, True, False)
			explicit = 42
		elif explicit == 42:
			if self.f == 1:
				self.f = 0
				self.image = self.orig
			elif self.f == 0:
				self.f = 1
				self.image = pygame.transform.flip(self.orig, True, False) #should do it.... I hope.
			explicit = 42

	def moveleft(self):
		self.rect.x = self.rect.x - 2

	def moveright(self):
		self.rect.x = self.rect.x + 2

	def movedown(self):
		self.rect.y = self.rect.y + 2

	def moveup(self):
		self.rect.y = self.rect.y - 2

	def nomove(self):
		self.d = None

	def sprfileswp(self, file):
		self.tempx = self.rect.x
		self.tempy = self.rect.y
		self.image, self.rect = globalload(file)
		self.orig = self.image
		if self.f == 1:
			self.image = pygame.transform.flip(self.orig, True, False)
		self.rect.x = self.tempx
		self.rect.y = self.tempy

	def sprimgswp(self, img):
		self.tempx = self.rect.x
		self.tempy = self.rect.y
		self.image, self.rect = globalimgload(img)
		self.orig = self.image
		if self.f == 1:
			self.image = pygame.transform.flip(self.orig, True, False)
		self.rect.x = self.tempx
		self.rect.y = self.tempy

	def beware(self):
		self.sprfileswp(self.waryfile)

	def revert(self):
		self.sprfileswp(self.calmfile)
		pygame.event.clear()

	def bulletreset(self):
		if self.f == 0:
			self.bullet.left = self.tmpstore
			self.bullet.x = 0
			self.bullet.y = 0
			self.bullet.w = 1
			self.tmpstore = None
		else:
			(self.bullet.right, self.bullet.left) = self.tmpstore
			self.bullet.x = 0
			self.bullet.y = 0
			self.bullet.w = 1
			self.tmpstore = None
			self.tmpstore2= None

	def dischg(self, screen):
		self.sprfileswp(self.firefile)
		self.nomove()
		if self.f == 0: #Left
			print "Agent shooting left...."
			self.bullet.x = (self.rect.x + 5)
			self.bullet.y = (self.rect.y + 4)
			self.tmpstore = self.bullet.left
			self.bullet.w = self.bullet.left
			self.bullet.left = 0
			screen.blit(pygame.Surface(self.bullet.size), (self.bullet))
			self.bulletreset()
		else:#if it's not facing left, its facing RIGHT.
			print "Agent shooting right...."
			self.bullet.x = (self.rect.x + 20)
			self.bullet.y = (self.rect.y + 4)
			self.tmpstore = (self.bullet.right, self.bullet.left)
			self.tmpstore2= (1280 + self.rect.x)/2
			(self.bullet.right, self.bullet.left) = (self.tmpstore2, (self.rect.x + 20))
			self.bullet.w = self.tmpstore2 * 2
			screen.blit(pygame.Surface(self.bullet.size), (self.bullet))
			self.bulletreset()
		self.shootstg = 2#THIS MUST GO IN ORDER FOR RECTAGLE TO WORK, BECAUSE OF HOW IT IS IMPLEMENTED (CHECK MAIN)!
	def jump(self):
		if self.state == 1:
			if self.jof == 1:
				if self.rect.top > 200:
					self.rect.y = self.rect.y - self.velocity
					self.velocity = self.velocity - 1
					self.state = 1
					self.jof = 1
				elif self.rect.top < 200:
					self.jof = -1

			if self.jof == -1:
				if self.rect.y < 350:
					self.rect.y = self.rect.y + self.velocity
					self.velocity = self.velocity + 1
				else:
					self.velocity = 0
					self.jof = 0
					self.state = 0
		return self.state
	def recoil(self):
		self.sprfileswp(self.kickfile)
		self.shootstg = 3
