validDigits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
while True:
	try:
		#digits = raw_input("Please input a 9 or 16 digit long string of numbers: ")
		digits = '123456789'
		if len(digits) != 9 and len(digits) != 16: raise UserWarning
		for digit in digits:
			if digit not in validDigits:
				raise ValueError
		break
	except UserWarning:
		print "\'Please input a 9 or 16 digit long string.\'\n\'...input a 9 or 16 digit long string.\'\n\'...9 or 16 digit long string.\'\n\'...9 or 16 digit...\'\nHoo boy, I wonder where you went wrong!\nIt\'s OVER BETWEEN US."
		break
	except ValueError:
		print "I said OF NUMBERS."
def fsum(digits):
	dsum = 0
	flipper=1
	print "fsum:"
	for digit in range(len(digits)):
		flipper = -1*flipper
		print "FLIPPER:: " + str(flipper)
		if flipper == 1:
			dsum = dsum + int(digit)
		elif flipper == -1:
			print str(int(digit)*2) + " = " + str(digit) + " * 2"
			doubled = (int(digit))*2; doubled = str(doubled)
			print doubled
			if len(doubled) == 2:
				doubledA = int(doubled[0])
				print doubledA
				doubledB = int(doubled[1])
				print doubledB
				dsum = dsum + (doubledA + doubledB)
			else: dsum = dsum + int(digit)*2
			
	print "fsum end!"
	return dsum
del validDigits
print digits
print digits
print fsum(digits)
print fsum(digits)*9
print fsum(digits)*9%10

adigit = (fsum(digits)*9%10)
#print str(adigit)
	