cdnacct=0.0
usdacct=0.0
while True:
	try:
		print "\nCanadian account balance: $" + "%0.2f"%cdnacct + "\nAmerican account balance: $" + "%0.2f"%usdacct + "\n"
		choice = input("1. Deposit into Canadian account\n2. Deposit into American account\nAnything else exits.\nSelection: ")
		if choice == 1:
			cdnacct = cdnacct + input("How much would you like to deposit in this account? $")
		elif choice == 2:
			usdacct = usdacct+ input("How much would you like to deposit in this account? $")
		else: raise ValueError
	except NameError:
		print "Put in numbers."
	except SyntaxError:
		print "That doesn't make sense."
	except ValueError:
			choice=input("Leave?\n0 or False: no\nAnything else: yes\nDecision: ")
			if not choice: pass
			else:
				print "I suppose that is a yes."
				break
			
		
