import pygame
print "main: pygame imported!"
import random
print "main: random imported!"
import time
print "main: time imported!"
from pygame.locals import *
print "main: pygame.locals imported!"
import pygame.mixer
print "mainL mixer imported!"
from player import Player
print "main: player imported!"
from enemy import Enemy
print "main: enemy imported!"

all = pygame.sprite.Group()
screen = pygame.display.set_mode([1280, 720])
screct = pygame.Rect(0, 0, 1280, 720)
backgr = pygame.Surface(screct.size)
pygame.init()
player = Player(screen)
enemy = Enemy(screen)
all.add(player)
all.add(enemy)

while(True):
	screen.fill((255,255,255))
	if player.alive == True:
		player.loopresp(screen)
		if player.state == 1:
			player.jump()
	else:
		player.sprfileswp(player.deadfile)
	if player.shootstg == 1:
		#rectangur currishunz
		if player.bullet.colliderect(enemy.rect) and enemy.alive == True:
			enemy.alive = False
			enemy.sprfileswp(enemy.deadfile)
			pygame.mixer.Sound.play(enemy.aaAaa)
	if player.gunup == True:
		enemy.roll_high()
	elif player.moving == True:
		enemy.roll_med()
	else:
		enemy.roll_low()
	pygame.time.delay(1)
	if enemy.alive == True:
		enemy.loopresp(screen)
		if enemy.bullet.colliderect(player.rect) and player.alive == True:
			player.alive = False
			player.sprfileswp(player.deadfile)
			pygame.mixer.Sound.play(player.aaAaa)
	if player.d == 0:
		player.moveleft()
	elif player.d == 1:
		player.moveright()
	elif player.d == 2:
		player.movedown()
	elif player.d == 3:
		player.moveup()
	else:
		player.nomove()
	if player.gunup == False:
		player.sprfileswp(player.calmfile)
	all.draw(screen)
	pygame.display.flip()
	pygame.time.delay(10)