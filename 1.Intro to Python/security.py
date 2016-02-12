def protect(): #this function has a misleading name
	correct = False
	password = 'password'
	guess = ''
	loop = -1
	while guess != password:
		guess = raw_input("Password: ")
		loop = loop + 1
	print "You entered an incorrect password " + str(loop) + " times."
