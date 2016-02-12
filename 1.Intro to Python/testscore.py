incomplete = True
print "Let\'s calculate your test percent."
while incomplete:
	try:
		marks = float(input("First, tell me how many marks you got.\n"))
		total = float(input("Next, how many marks total were on it?\n"))
		if total == 0: raise ZeroDivisionError
		if total < marks: raise ValueError
		print "percent = marks / total"
		print "percent = 100 * " + str(marks) + " / " + str(total)
		print "percent = 100 * " + str(marks/total)
		print "percent = " + str(100*(marks/total))
		print "\nYou got " + str(round((100*(marks/total)), 2)) + "% on the test."
		incomplete = False
	except NameError:
		print "That is not a number."
	except TypeError:
		print "Something went wrong. Please only input numbers, not commas, etc."
	except ZeroDivisionError:
		print "Thats bullshit. The test was not out of zero."
	except ValueError:
		print "Thats impossible. Damn liar."