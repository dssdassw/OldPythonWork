import pygame
import utils

fpsClock = pygame.time.Clock()
reusedValue = -1
screen,screct = utils.pygameSetup(1280, 720, "Code Playground")
choice = utils.choose("Are you epileptic? 1 or True = yes, 0 or False = no")
if choice:
	while True:
		fpsClock.tick(75)
		reusedValue = utils.strobe(screen, reusedValue)
		pygame.display.flip()