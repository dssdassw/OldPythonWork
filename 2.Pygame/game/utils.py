import pygame
import random

def pygameSetup(w, h, caption="Pygame Window", color=[0,0,0], bkgrcolor=None):
	if bkgrcolor == None: bkgrcolor = color
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode([w,h])
	screct = screen.get_rect()
	backgr = pygame.Surface(screct.size)
	screen.fill(color)
	backgr.fill(bkgrcolor)
	pygame.display.flip()
	pygame.display.set_caption(caption)
	return screen, screct, pygame.Surface(screct.size)

def randrgb():
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	return (r, g, b)

def rainbow_strobe(surf):
	surf.fill(randrgb)
	return surf
	
def strobe(surf, val=-1):
	val = val * (-1)
	if val == 1:
		surf.fill([255,255,255])
	else:
		surf.fill([0,0,0])
	return val
	
def choose(prompt):
	try:
		choice = input(prompt)
		if choice < 0 or choice > 4: raise ValueError
		return choice
	except NameError: print "Excuse me?"
	except ValueError: print "That\'s not a valid option.\n"
	except OverflowError: print "There just isn\'t enough room.\nIf you\'re really desperate, you can wait to see if some people cancel their flights last-minute.\n"
	except SyntaxError: print "Do you need a translator?"
