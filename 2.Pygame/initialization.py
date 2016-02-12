import pygame
pygame.init()
def gameinit(w, h, screen, screct, backgr):
	shortsword = pygame.image.load("spr/shortsword.png"); shortswordrect = shortsword.get_rect()
	broadsword = pygame.image.load("spr/broadsword.png"); broadswordrect = broadsword.get_rect()
	greatsword = pygame.image.load("spr/greatsword.png"); greatswordrect = greatsword.get_rect()
	scimitar = pygame.image.load("spr/scimitar.png"); scimitarrect = scimitar.get_rect()
	rapier = pygame.image.load("spr/rapier.png"); rapierrect = rapier.get_rect()
	shortsword = pygame.transform.scale(shortsword, ((shortswordrect.w*2), (shortswordrect.h*2))); shortswordrect = shortsword.get_rect()
	broadsword = pygame.transform.scale(broadsword, ((broadswordrect.w*2), (broadswordrect.h*2))); broadswordrect = broadsword.get_rect()
	greatsword = pygame.transform.scale(greatsword, ((greatswordrect.w*2), (greatswordrect.h*2))); greatswordrect = greatsword.get_rect()
	scimitar = pygame.transform.scale(scimitar, ((scimitarrect.w*2), (scimitarrect.h*2))); scimitarrect = scimitar.get_rect()
	rapier = pygame.transform.scale(rapier, ((rapierrect.w*2), (rapierrect.h*2))); rapierrect = rapier.get_rect()
	complete = False
	while not complete:
		screen.fill([80,80,80])
		screen.blit(shortsword, ((w/2/2), (h/2/2))); shortswordrect.x = (w/2/2); shortswordrect.y = (h/2/2)
		screen.blit(broadsword, ((w/2), (h/2/2))); broadswordrect.x = (w/2); broadswordrect.y = (h/2/2)
		screen.blit(greatsword, ((w/2+w/2/2), (h/2/2))); greatswordrect.x = (w/2 + w/2/2); greatswordrect.y = (h/2/2)
		screen.blit(scimitar, ((w/2/2), (h/2/2+h/2/2))); scimitarrect.x = (w/2/2); scimitarrect.y = (h/2/2 + h/2/2)
		screen.blit(rapier, ((w/2), (h/2/2+h/2/2))); rapierrect.x = (w/2); rapierrect.y = (h/2/2 + h/2/2)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if shortswordrect.collidepoint(event.pos): return 0
				elif broadswordrect.collidepoint(event.pos): return 1
				elif greatswordrect.collidepoint(event.pos): return 2
				elif scimitarrect.collidepoint(event.pos): return 3
				elif rapierrect.collidepoint(event.pos): return 4
				else: pass
			else: pass

