print "Give me some numbers, and I'll calculate the average. Giving a\nnegative number or a zero will make me calculate the average."
incomplete = True
loops = 0
total = 0
while incomplete:
	try:
		num = input(">")
		if num < 1: raise ValueError
		else: total = total + num; loops = loops + 1
	except NameError:
		print "That is not a number."
	except TypeError:
		print "Something went wrong. Please only input numbers, not commas, etc."
	except SyntaxError:
		print "Yeah no."
	except ValueError:
		print "mean = (NUM1 + NUM2 + NUM3 + NUM4 + NUM5...)/numberofnumbers"
		print "mean = " + str(total) + "/" + str(loops)
		print "mean = " + str(total/loops)
		incomplete = False