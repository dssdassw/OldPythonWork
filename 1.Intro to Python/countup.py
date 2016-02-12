#this program is pretty much pointless and has absolutely no practical applications unless you don't know how to count.
while not passed:
	try:
		start = input("Tell me the start.\n")
		end = input("Tell me the end.\n")
		if start > end:
			raise ValueError
		between = range(start, end)
		for n in between:
			print str(n) + ", "
		passed = True
	except NameError:
		print "You idiot, that is not a number."
	except TypeError:
		print "Something went wrong. Please only input numbers, not commas, etc."
	except ValueError:
		print "The start should be less than the end."