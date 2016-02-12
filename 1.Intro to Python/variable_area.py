import math

incomplete = True
while incomplete:
	choice = input("Choose:\n1. Area of a circle\n2. Area of a rectangle\n3. Area of a triangle\n -NOTE: Anything but these 3 exits.-\n\n")
	if choice == 1:
		print "The area of a circle is " + str(math.pi) + " * (2*radius)"
		passing = False
		while not passing:
			try:
				radius = input("Tell me the radius.\n")
				passing = True
			except NameError:
				print "That is not a number.\n"
		print "The circle's area is " + str(math.pi * (radius*2)) + "."
		del passing
	elif choice == 2:
		print "The area of a rectangle is length * width."
		passing = False
		while not passing:
			try:
				l = input("Tell me the length.\n")
				w = input("Tell me the width.\n")
				passing = True
			except NameError:
				print "Yeah, those should be numbers."
		print "The rectangle's area is " + str(l * w) + "."
		del passing
	elif choice == 3:
		print "The area of a triangle is base * height / 2."
		passing = False
		while not passing:
			try:
				base = input("Tell me the base.\n")
				height = input("Tell me the height.\n")
				passing = True
			except NameError:
				print "Both base and height should be numbers."
		print "The triangle's area is " + str((base * height)/2) + "."
		del passing
	else: break