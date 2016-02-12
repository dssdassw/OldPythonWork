incomplete = True
print "Let\'s calculate the area of a rectangle."
while incomplete:
	try:
		l = input("First, the length. What is it?\n")
		w = input("Next, the width. What is that?\n")
		print "a = l * w"
		print "a = " + str(l) + " * " + str(w)
		print "a = " + str(l*w)
		incomplete = False
	except NameError:
		print "That is not a number."
	except TypeError:
		print "Something went wrong. Please only input numbers, not commas, etc."