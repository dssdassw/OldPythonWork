import pygame
from clean_living import living

class Player(living):
	def __init__(self, form_list):
		pygame.sprite.DirtySprite.__init__(self)
		living.__init__(self)
		self.image, self.rect = self.loadr(form_list[0])
		self.cliprect = pygame.rect.Rect((0,0), (0,0))
		self.h = self.rect.h
		self.y = self.rect.y
		self.orig = self.image
		self.forms = form_list
		self.loop = 0
		self.v = 0
		self.f = 'r'
		self.j = False
		self.m = False
		self.mask = pygame.mask.from_surface(self.image, 1)
		self.origh = self.rect.h
		self.maskinit()
	def react(self,sprite=None):
		for event in pygame.event.get():
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: self.stopm()
#				if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					if pygame.key.get_mods() == 1: self.sprintleft()
					else: self.left()
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					if pygame.key.get_mods() == 1: self.sprintright()
					else: self.right()
				if event.key == pygame.K_e:
					pass # < < < <
				if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
					self.j = True
					self.rect.y = self.rect.y - 1
					self.jump()
		if self.f == 'l' and self.m == True:
			if pygame.key.get_mods == 1: self.sprintleft()
			else: self.left()
		if self.f == 'r' and self.m == True:
			if pygame.key.get_mods == 1: self.sprintright()
			else: self.right()
		if self.y > self.rect.y:
			#print "self.y > self.rect.y. Jumping."
			self.imageswap(2)
			self.jump()
		else: self.resetJump()