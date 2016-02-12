while True:
	l = len(raw_input("Password: "))
	if l < 3: print 'Too short!'
	elif l > 10: print 'Too long!'
	else: 
		print 'Password accepted!'
		break
