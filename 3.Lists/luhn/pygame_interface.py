import pygame
import luhn
import pygame, string

pygame.init()
screen=pygame.display.set_mode([1280,720])
screct=screen.get_rect() #GET REEEEEEKT
background=(255,255,255)
font=pygame.font.Font(None,60)
strtext=""
listtxt=range(0)
screen.fill(background)
pygame.display.flip()
numbers = ['0','1','2','3','4','5','6','7','8','9']
indent = screct.w/18
ccnpos = (indent,screct.h/2-screct.h/3)
sinpos = (indent,screct.h/2)

while True:
	#4024007101220498
	event=pygame.event.poll()
	if (event.type==pygame.QUIT): break
	if (event.type==pygame.KEYDOWN):
		strtext=""
		if (event.key==pygame.K_BACKSPACE):
			if listtxt != []:
				listtxt.pop()
				for character in listtxt: strtext += character
		else:
			listtxt.append(chr(event.key))  #build up the strtext with each key press
			for character in listtxt: strtext += character
		screen.fill(background)
		for value in listtxt:
			if value in numbers: valid = True
			else:
				valid = False; break
		if valid:
			if luhn.ccn_valid(strtext) and len(strtext)>0 and len(strtext)==16:
				ccndiags = "CCN: VALID!"
				ccncolor = [0,255,0]
			else:
				ccndiags = "CCN: INVALID!"
				ccncolor = [255,0,0]
			if luhn.sin_valid(strtext) and len(strtext)==9:
				sindiags = "SIN: VALID!"
				sincolor = [0,255,0]
			else:
				sindiags = "SIN: INVALID!"
				sincolor = [255,0,0]
			if len(strtext) == 15: ccn_csum = "Valid check digit for this as a CCN: " + str(luhn.calc_ccn(int(strtext)))
			else: ccn_csum = " "
			if len(strtext) == 8: sin_csum = "Valid check digit for this as a SIN: " + str(luhn.calc_sin(strtext))
			else: sin_csum = " "
		else:
			ccndiags = "That won\'t work."
			ccn_csum = " "
			sindiags = "Numbers only, please."
			sin_csum = " "
			ccncolor = [255,175,0]
			sincolor = [255,175,0]
		text=font.render(strtext,True,(0,0,0),background)
		ccndiag=font.render(ccndiags,True,ccncolor,background)
		ccn_csumSurf = font.render(ccn_csum,True,(0,0,0),background)
		sindiag=font.render(sindiags,True,sincolor,background)
		sin_csumSurf = font.render(sin_csum,True,(0,0,0),background)
		textrect = text.get_rect()
		textrect.midtop = (screct.w/2,screct.h/2+screct.h/4)
		ccnrect = ccndiag.get_rect()
		ccnrect.x, ccnrect.y = ccnpos
		sinrect = sindiag.get_rect()
		sinrect.x, sinrect.y = sinpos
		screen.blit(text,(textrect.x, textrect.y))
		screen.blit(ccndiag,(ccnrect.x, ccnrect.y))
		screen.blit(ccn_csumSurf,(indent, (ccnrect.y + ccnrect.h)))
		screen.blit(sindiag,(sinrect.x, sinrect.y))
		screen.blit(sin_csumSurf,(indent, (sinrect.y + sinrect.h)))
		pygame.display.flip()