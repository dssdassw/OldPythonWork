import pygame
from living import living

class Enemy(living):
	def __init__(self, form_list):
		living.__init__(self, form_list)
		self.image, self.rect = self.loadr(form_list[0])
		self.orig = self.image
		self.timer = 0
		self.modder = 1
		self.speed = 1
	def aileft(self):
		if self.speed > 0: self.speed = self.speed * -1
		if self.f == 'r': self.f == 'l'; self.image = self.fliph(self.orig)
		self.speed = self.speed - self.modder
	def airight(self):
		if self.speed < 0: self.speed = self.speed * -1
		if self.f == 'l': self.f == 'r'; self.image = self.fliph(self.image)
		self.speed = self.speed + self.modder
	def aimove(self):
		self.rect.x = self.rect.x + self.speed
	def zombie(self, target):
		if self.rect.x > target.rect.x:
			self.rect.x = self.rect.x - 3
		elif self.rect.x < target.rect.x:
			self.rect.x = self.rect.x + 3
			
