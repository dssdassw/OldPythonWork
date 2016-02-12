import pygame
from all import *
from object import object
from living import living
from player import Player
from sword import Sword
from initialization import gameinit

pygame.init()
w = 800; h = 450
screen = pygame.display.set_mode([w, h], pygame.DOUBLEBUF)
screct = pygame.Rect(0, 0, w, h)
backgr = pygame.Surface(screct.size)
screen.fill([0,0,0])
backgr.fill([0,0,0])
clock = pygame.time.Clock()
all = allspr()
#image, type, speed, damage, length
broadsword = Sword("spr/broadsword.png", 'broadsword', 10, 50, 10, 17, -1)
rapier = Sword("spr/rapier.png", 'rapier', 10, 76, 5, 17, -1)
scimitar = Sword("spr/scimitar.png", 'scimitar', 7, 55, 12, 15, -3)
greatsword = Sword("spr/greatsword.png", 'greatsword', 20, 20, 25, 25, -10)
shortsword = Sword("spr/shortsword.png", 'shortsword', 6, 20, 25, 25, 0)
choice = gameinit(w, h, screen, screct, backgr)
if choice == 0: player = Player(shortsword)
elif choice == 1: player = Player(broadsword)
elif choice == 2: player = Player(greatsword)
elif choice == 3: player = Player(scimitar)
elif choice == 4: player = Player(rapier)
else: print "A FATAL ERROR HAS OCCURED!"
dumbfuck = Player(rapier)
all.add(dumbfuck)
all.add(player)
all.add(player.sword)
temp = 0
temp2 = 3
screen.fill([0,0,0])
pygame.display.flip()
print screen.get_bytesize()
print (screen.get_bytesize() * (screen.get_width() * screen.get_height()))/1024/1024
def clockloop(clock):
	clock.tick_busy_loop(69.6969696969696969696969696969696969696969696969696969696969696969696969696969696969)
print player.rect.y, player.rect.bottom
while(True):
	clockloop(clock)
	all.clear(screen, backgr)
	player.react()
	pygame.display.update(all.draw(screen))