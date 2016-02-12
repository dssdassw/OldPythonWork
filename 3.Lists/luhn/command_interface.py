import luhn

#check number: 4024007101220498
#test SIN num: 514055673
running = True
while running:
	while True:
		try:
			choice = input("\n1. Generate a valid credit card and a valid social insurance number\n2. Check a credit card or social insurance number for validity.\n3. Exit\n")
			if choice != 1 and choice != 2 and choice != 3: raise UserWarning
			break
		except UserWarning: print "That\'s not a valid choice."
		except ValueError: print "What?"
		except TypeError: print "What?"
		except NameError: print "What?"
		except SyntaxError: print "What?"

	if choice == 1:
		print "Random credit card number:",luhn.rand_ccn()
		print "Random Canadian Social Insurance Number:",luhn.rand_sin()

	elif choice == 2:
		validDigits=['0','1','2','3','4','5','6','7','8','9']
		while True:
			try:
				digits = raw_input("Please input a 9 or 16 digit long string of numbers to check for validity: ")
				if len(digits) != 9 and len(digits) != 16: raise UserWarning
				for digit in digits:
					if digit not in validDigits:
						raise ValueError
				break
			except UserWarning:
				print "\'Please input a 9 or 16 digit long string.\'\n\'...input a 9 or 16 digit long string.\'\n\'...9 or 16 digit long string.\'\n\'...9 or 16 digit...\'\nHoo boy, I wonder where you went wrong!"
			except ValueError:
				print "I said OF NUMBERS."
		del validDigits
		sin_num = digits
		ccn_num = digits
		if luhn.ccn_valid(ccn_num): print digits,"is a valid credit card number."
		else: print digits,"is not a valid credit card number."
		if luhn.sin_valid(sin_num): print digits,"is a valid Canadian Social Insurance Number."
		else: print digits,"is not a valid Canadian Social Insurance Number."

	elif choice == 3: break