import random
key = [random.randint(0,10), random.randint(0,10)]
correct = False
while not correct:
	try:
		print key
		xguess = input("Guess a x coordinate from 0 to 10: ")
		yguess = input("Guess a y coordinate from 0 to 10: ")
		guess = [xguess,yguess]
		if guess == key:
			print "Correct."
			correct = True
		else: print "Wrong."
	except NameError:
		"NUMBERS. PLEASE USE NUMBERS GODDAMNIT."