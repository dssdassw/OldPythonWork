def choose(prompt):
	while True: #PLEASE TAKE CARE TO ALWAYS ENCASE TRY INSIDE OF A WHILE! OTHERWISE, IT FALLS THROUGH LIKE A SWITCH-CASE!
		try:
			choice = input(prompt)
			if choice < 0 or choice > 4: raise ValueError
			return choice
			break
		except NameError: print "Excuse me?"
		except ValueError: print "That\'s not a valid option.\n"
		except OverflowError: print "There just isn\'t enough room.\nIf you\'re really desperate, you can wait to see if some people cancel their flights last-minute.\n"
		except SyntaxError: print "Do you need a translator?"

def booking(flight):
	try:
		if not flight.book(input("How many seats would you like to book?\n"), input("\n--and in how many days will you fly?\n")): raise OverflowError
		while(finalchoice(flight)): pass
	except NameError: print "Excuse me?"
	except ValueError: print "That\'s not a valid option.\n"
	except OverflowError: print "There just isn\'t enough room."
	except SyntaxError: print "Do you need a translator?"
	
def finalchoice(flight):
	choice = choose("\n1. Checkout\n2. Pay for heavy baggage\n3. Upgrade to first class\n")
	if choice == 1:
		flight.checkout()
		return False
	elif choice == 2:
		flight.baggage(input("How much, in kilograms, are you carrying?"))
		return True
	elif choice == 3:
		flight.upgrade()
		return True
