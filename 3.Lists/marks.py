while True:
	try:
		marks = []
		names = []
		for counter in range(0,2):
			marks.append(input("Give me a mark from 0 to 100.\n"))
			names.append(raw_input("Now the name of the student whose mark this is.\n"))
			if marks[counter] > 100: raise OverflowError
			elif marks[counter] < 0: raise OverflowError
		print "Thanks."
		print "Marks over 80:"
		for mark in marks:
			if mark > 80: print names[marks.index(mark)] + ": " + str(mark)
		break
	except ValueError: print "What?"
	except NameError: print "What?"
	except SyntaxError: print "What?"
	except OverflowError: print "That's not a valid mark."