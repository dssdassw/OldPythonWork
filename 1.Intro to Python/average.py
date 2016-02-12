print "Give me 5 numbers, and I'll calculate the average. Floating point numbers work."
avg=0.0
incomplete = True
while incomplete:
	try:
		n1 = float(input("NUM1: "))
		n2 = float(input("NUM2: "))
		n3 = float(input("NUM3: ")) 
		n4 = float(input("NUM4: "))
		n5 = float(input("NUM5: "))
		print "mean = (NUM1 + NUM2 + NUM3 + NUM4 + NUM5)/5"
		print "mean = (" + str(n1) + " + " + str(n2) + " + " + str(n3) + " + " + str(n4) + " + " +str(n5) + " + " + ")/5"
		print "mean = " + str(n1+n2+n3+n4+n5) + " /5"
		print "mean = " + str((n1+n2+n3+n4+n5)/5)
		incomplete = False
	except NameError:
		print "That is not a number."
	except TypeError:
		print "Something went wrong. Please only input numbers, not commas, etc."