import pygame
import utils

screen, screct = utils.pygameSetup(1280, 720, "Shape testing: DUMB STATIC GRAPHIC")
body = pygame.Surface([90, 160])
body.fill([0, 0, 0, .5])
bodyrect = body.get_rect()
bodyrect.x = screct.w/2
bodyrect.y = (screct.h/2)-(bodyrect.h/2)
drawitplzx, drawitplzy = bodyrect.midleft
print bodyrect.bottomleft, bodyrect.bottom
workx, worky = bodyrect.midleft
workx = workx - bodyrect.w/2

while True:
	screen.fill([255,255,255])
	pygame.draw.line(screen, [0,0,0], [bodyrect.x, bodyrect.y+(bodyrect.y/2)], [bodyrect.x,bodyrect.y])
	pygame.draw.circle(screen, [0,0,0], [(bodyrect.x), (bodyrect.y-50)], 50)
	pygame.draw.line(screen, [0,0,0], [bodyrect.x,bodyrect.y+15],[drawitplzx+45, drawitplzy])
	pygame.draw.line(screen, [0,0,0], [bodyrect.x,bodyrect.y+15], [workx, worky])
	pygame.draw.line(screen, [0,0,0], [bodyrect.x, bodyrect.bottom-20], [bodyrect.x+15, bodyrect.bottom+100])
	pygame.draw.line(screen, [0,0,0], [bodyrect.x, bodyrect.bottom-20], [bodyrect.x-15, bodyrect.bottom+100])
	pygame.display.flip()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			break

