import time
import pygame
print "enemy: pygame imported!"
import time
print "enemy: time imported!"
import random
print "enemy: random imported!"
from agent import Agent
print "enemy: Agent imported!"
from player import Player
print "enemy: Player imported!"

class Enemy(Agent):
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.calmfile = "spr/e.png"
		self.waryfile = "spr/ea.png"
		self.firefile = "spr/es.png"
		self.kickfile = "spr/ek.png"
		self.deadfile = "spr/ed.png"
		self.alive = True
		self.shootstg = 0
		self.before = self.calmfile
		self.actchnce = 0
		self.acthigh = 0
		self.actlow = 0
		screen = pygame.display.get_surface()
		Agent.__init__(self, self.calmfile, self.waryfile, self.firefile, self.kickfile, screen)
		self.rect.x = 720
		self.rect.y = 350


	def roll_low(self):
		self.acthigh = random.randint(500, 1000)
		self.actlow = random.randint(0, 499)
		self.actchnce = random.randint(self.actlow,self.acthigh)

	def roll_med(self):
		self.actchnce = random.randint(500,1000)

	def roll_high(self):
		self.actchnce = random.randint(0,100)

	def loopresp(self, screen):
		#must explain what I think is really clever of me before I
		#forget! These shootstg ifs are backwards and elif-ing because
		#it is DESIGNED for only one to be true at a time before the
		#game cycles the frame, allowing me to avoid forcing a
		#framechange. This insures that all sprites also display without
		#flickering around the place while one is shooting!
		if self.shootstg == 4:
			pygame.time.delay(100)
			self.revert()
			self.shootstg = 0
		elif self.shootstg == 3:
			pygame.time.delay(100)
			self.beware()
			self.shootstg = 4 #hidden on stgs 1 & 2 in functions
			#in order to save making too many functions, I reused one
			#and added some code to make it do the same as the rest.

		elif self.shootstg == 2:
			pygame.time.delay(100)
			self.recoil()

		elif self.shootstg == 1:
			self.dischg(screen)
			pygame.mixer.Sound.play(self.shot)
			print "ENEMY SHOT AT", pygame.time.get_ticks()
		if self.actchnce == 42 and (not self.shootstg > 0):
			self.sprfileswp(self.firefile)
			self.shootstg = 1