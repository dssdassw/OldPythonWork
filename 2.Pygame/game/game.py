import pygame
import utils
import time
from player import Player
from enemy import Enemy
#Mirror's Edge, except less wall jumping, and more enemy dodging. Fighting should be just as one-sided towards the enemy. Oh, and stick figure graphics.
#... because I can't do any better art, and I won't even be satisfied with one sprite until I've been working on it for hours.
#I want to expand on this game at some point. It's a pretty good base, I even derived an "engine" of sorts from it's earlier form.
clock = pygame.time.Clock()
pygame.init()
all = pygame.sprite.RenderUpdates()
enemies = pygame.sprite.RenderUpdates()
hit = pygame.sprite.Group()
screen, screct, backgr = utils.pygameSetup(1280, 720, "Stick Figure Ninja", [255,255,255])
player = Player(["spr/s.png", "spr/s2.png", "spr/sj1.png", "spr/sj2.png", "spr/ss.png", "spr/sw1.png", "spr/sw2.png", "spr/sw3.png", "spr/sw3.png", "spr/sw4.png"])
enemy = Enemy(["spr/es.png", "spr/es2.png", "spr/esj1.png", "spr/esj2.png", "spr/ess.png", "spr/esw1.png", "spr/esw2.png", "spr/esw3.png", "spr/esw4.png"])
player.rect.y = 225; enemy.rect.y = 225
all.add(player)
all.add(enemy)
enemies.add(enemy)
player.rect.x = player.rect.x + 50
enemy.rect.x = screct.w/2
screen.fill([0,0,0])
player.y = player.rect.y
hits = 0
flist=pygame.font.get_fonts()
flist.sort()
for item in flist: print item
font = pygame.font.SysFont('consolas',25)
text = font.render("You can do eet", False, [0,0,0], [255,255,255])
health=font.render("You can do eet 2", False, [0,0,0], [255,255,255])
timertop=time.time()+(10)
win = False
while True:
	screen.fill([255,255,255])
	if player.health <= 0: break
	if time.time() > timertop:
		win = True; break
	text = font.render("Survive for " + str(timertop-time.time()) + " more seconds!", False, [0,0,0], [255,255,255])
	health=font.render("Health remaining: " + str(player.health), False, [0,0,0], [255,255,255])
	screen.blit(text, (screct.w/2-text.get_width(),screct.h/2))
	screen.blit(health, (screct.w/2-text.get_width(),screct.h/2-text.get_height()))
	clock.tick_busy_loop(60)
	player.react()
	enemy.zombie(player)
	for sprite in all:
		hit = pygame.sprite.spritecollide(sprite, all, False, pygame.sprite.collide_mask)
	if player in hit:
		if pygame.sprite.collide_mask(player, enemy) != None: #get these bastards to actually work later plz
			if not player.sliding: player.health = player.health - 5; print player.health
			hits = hits + 1
			print "hit number " + str(hits)
	if player.m:
		if player.f == 'l': player.left()
		elif player.f == 'r': player.right()
	pygame.display.update(all.draw(screen))
	pygame.display.flip()
if win:
	while True:
		text = font.render("YOU WIN!!!", False, [0,0,0], [255,255,255])
		screen.blit(text, (screct.w/2-text.get_width(),screct.h/2-text.get_height()))
		pygame.display.flip()
else:
	while True:
		text = font.render("You lose...", False, [0,0,0], [255,255,255])
		screen.blit(text, (screct.w/2-text.get_width()/2,screct.h/2-text.get_height()))
		pygame.display.flip()