import math
passing = False
print "This program will calculate the area of a circle to the nearest accuracy."

while not passing:
	try:
		radius = input("Tell me the radius.\n")
		passing = True
	except NameError:
		print "That is not a number.\n"
diameter = 2 * radius
area = math.pi * diameter
print "The circle's area is " + str(area) + "."
