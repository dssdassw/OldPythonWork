import pygame
from living import *
from sword import Sword

class Player(living):
	def __init__(self, sword):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.rect = self.loadr("spr/p.png")
		self.h = self.rect.h
		self.rect.y = 225
		self.orig = self.image
		self.sword = sword
		self.health = 100
		self.live = True
		self.loop = 0
		self.v = 0
		self.f = 'l'
		self.j = 'still'
		self.y = None
		self.m = False
		self.s = False
		self.temp = 0
		self.temp2 = 3
		self.origh = self.rect.h
	def react(self,sprite=None):
		if self.s:
			if self.sword.f == 'r': self.sword.image = pygame.transform.rotate(self.sword.image, -22.5)
			else:
				self.sword.image = pygame.transform.flip(self.sword.image, True, False)
				self.sword.image = pygame.transform.rotate(self.sword.image, -22.5)
				self.sword.image = pygame.transform.flip(self.sword.image, True, False)
			self.loop = self.loop + 1
			if self.loop == 5:
				self.sword.image = self.sword.orig
				self.loop = 0
				self.s = False
				self.detract()
		for event in pygame.event.get():
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					self.stopm()
				if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
					self.j = 'falling'
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					if pygame.key.get_mods() == 1:
						self.sprintleft()
					else: self.left()
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					if pygame.key.get_mods() == 1:
						self.sprintright()
					else: self.right()
				if event.key == pygame.K_e:
					self.extend()
					self.s = True
				if event.key == pygame.K_SPACE or event.key == pygame.K_w or event.key == pygame.K_UP:
					self.jump()
		if self.f == 'l' and self.m == True:
			if pygame.key.get_mods == 1:
				self.sprintleft()
			else:
				self.left()
		if self.f == 'r' and self.m == True:
			if pygame.key.get_mods == 1:
				self.sprintright()
			else:
				self.right()
		if self.j != 'still':
			self.jump()
		self.swordfix()