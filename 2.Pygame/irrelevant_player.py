import pygame
print "player: pygame imported!"
import time
print "player: time imported!"
from human import human
print "player: agent imported!"

#streamline code after completion, removing any unnecessary variables, etc.
allspr = pygame.sprite.Group()
#idea, use sprite layered updates to do the shooting anim...

class Player(human):
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)
		self.calmfile = "spr/p.png"
		self.waryfile = "spr/pa.png"
		self.firefile = "spr/ps.png"
		self.kickfile = "spr/pk.png"
		self.deadfile = "spr/pd.png"
		self.alive = True
		self.before = self.calmfile
		screen = pygame.display.get_surface()
		self.gunup = False
		self.moving = False
		human.__init__(self, self.calmfile, self.waryfile, self.firefile, self.kickfile, screen)
		self.rect.x = 720
		self.rect.y = 350

	def loopresp(self, screen):
		if self.alive == True:
			if self.shootstg == 4:
				pygame.time.delay(100)
				self.revert()
				self.shootstg = 0

			if self.shootstg == 3:
				pygame.time.delay(100)
				self.beware()
				self.shootstg = 4

			if self.shootstg == 2:
				pygame.time.delay(100)
				self.sprfileswp(self.waryfile)
				self.shootstg = 0

			if self.shootstg == 1:
				pygame.time.delay(100)
				self.recoil()
				self.shootstg = 2

			for event in pygame.event.get():
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_a:
							if self.f != 0:
								self.turn()
							self.moving = True
							self.moveleft()
							self.d = 0
						if event.key == pygame.K_d:
							if self.f != 1:
								self.turn()
							self.moving = True
							self.moveright()
							self.d = 1
						if event.key == pygame.K_s:
							self.moving = True
							self.movedown()
							self.d = 2
						if event.key == pygame.K_w:
							self.moving = True
							self.moveup()
							self.d = 3
						if event.key == pygame.K_SPACE:
							if self.jof == 0:
								self.state = 1
								self.velocity = 10
								self.jof = 1
					if event.type == pygame.MOUSEBUTTONDOWN:
						if pygame.mouse.get_pressed()[2] == True:#get_pressed()[2] is right mouse button, [0] is left mouse button.
							self.nomove()
							self.sprfileswp(self.waryfile)
							self.gunup = True
							if pygame.mouse.get_pressed()[0] == True:
								self.dischg(screen)
								pygame.mixer.Sound.play(self.shot)
								self.shootstg = 1
								print "PLAYER SHOT AT", pygame.time.get_ticks()
					if event.type == pygame.MOUSEBUTTONUP:
						if pygame.mouse.get_pressed()[2] == False:
							self.gunup = False
							self.state = 0
							self.sprfileswp(self.calmfile)
							self.before = self.calmfile
					if event.type == pygame.KEYUP:
						self.moving = False
						self.d = None
						if event.key == pygame.K_SPACE:
							self.jof = -1
			if self.gunup == False:
				self.sprfileswp(self.calmfile)
		else:
			self.sprfileswp(self.deadfile)
			self.d = None
			self.moving = False