import pygame
print "fileops: pygame imported!"

def globalload(file):
	image = pygame.image.load(file)
	return image, image.get_rect()
def globalloadnorect(file):
	image = pygame.image.load(file)
	return image
def globalimgload(image):
	return image, image.get_rect()

