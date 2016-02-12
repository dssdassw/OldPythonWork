import pygame
from living import living
#formerly named "clean_player" because it's a cleaned up version of the old one.

class Player(living):
	def __init__(self, form_list):
		living.__init__(self, form_list)
		self.image, self.rect = self.loadr(form_list[0])
		self.y = self.rect.y
		self.orig = self.image
		self.f = 'r'
		self.j = False
		self.m = False
		self.maskinit()
	def react(self,sprite=None):
		for event in pygame.event.get():
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: self.stopm()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a or event.key == pygame.K_LEFT:
					if pygame.key.get_mods() == 1: self.sprintleft()
					else: self.left()
				if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
					if pygame.key.get_mods() == 1: self.sprintright()
					else: self.right()
				if event.key == pygame.K_e:
					self.sliding = True
					if self.f == 'l': self.x = self.rect.x - 25
					else: self.x = self.rect.x + 25
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
			self.imageswap(2)
			self.jump()
		else: self.resetJump()
		if self.sliding:
			self.imageswap(4)
			self.slide(self.f)