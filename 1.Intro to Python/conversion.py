cdn = 0.0
usd = 0.0
while True:
	try:
		choice = input("Would you like to convert CDN to USD or vice versa?\n1. CDN -> USD\n2. USD -> CDN\n")
		if choice == 1:
			print "As of 9/9/2014, 1 CDN = 0.91 USD."
			cdn = float(input("What value would you like to convert to USD? $"))
			usd = 0.91*cdn
			print "Value in USD: $","%0.2f"%usd
		elif choice == 2:
			print "As of 0/0/2014, 1 USD = 1.1 CDN."
			usd = float(input("What value would you like to convert to CDN? $"))
			cdn = 1.1*usd
			print "Value in CDN: $","%0.2f"%cdn
		else: raise ValueError
		break
	except NameError:
		print "Put in numbers."
	except SyntaxError:
		print "That doesn't make sense."
	except ValueError:
			print "That isn't a valid option."
