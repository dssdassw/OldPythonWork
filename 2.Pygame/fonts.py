import pygame
import random
import utils
#utils in incomplete!
pygame.init()
fpsClock = pygame.time.Clock()
print pygame.font.get_init()
all_fonts = pygame.font.get_fonts()
rgb=utils.randrgb()
for font in all_fonts:
	print font
print "DEFAULT FONT: " + str(pygame.font.get_default_font())
screen, screct = utils.pygameSetup(1280, 720, "Fonts lesson")
cnew = pygame.font.SysFont("couriernew",15,False,False)
text = cnew.render("I HATE YOU", False, [0,0,0])
while True:
	fpsClock.tick(10)
	rgb=utils.randrgb()
	screen.fill(rgb)
	screen.blit(text, [screct.w/2, screct.h/2])
	pygame.display.flip()
