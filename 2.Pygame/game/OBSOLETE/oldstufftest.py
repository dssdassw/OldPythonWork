import pygame
import utils
from clean_player import Player

clock = pygame.time.Clock()
pygame.init()
all = pygame.sprite.RenderUpdates()
screen, screct, backgr = utils.pygameSetup(1280, 720, "TEST POST PLEASE IGNORE")
player = Player("spr/p.png")
enemy = Player("spr/e.png")
player.rect.y = 225; enemy.rect.y = 225
all.add(player)
all.add(enemy)
player.rect.x = player.rect.x + 50
screen.fill([0,0,0])
temp = (0,0)
while True:
	screen.fill([0,0,0])
	clock.tick(60)
	player.react()
	if player.rect.colliderect(enemy.rect):
		print "BOOMHEADSHOT"
		player.rect.x = player.rect.x + 100
	if player.m:
		if player.f == 'l':
			player.left()
		elif player.f == 'r':
			player.right()
	pygame.display.update(all.draw(screen))
	#pygame.display.update(changed)
	#pygame.time.delay(50)