cdnacct=0.0
usdacct=0.0
while True:
	try:
		print "\nCanadian account balance: $" + "%0.2f"%cdnacct + "\nAmerican account balance: $" + "%0.2f"%usdacct + "\n"
		choice = input("1. Deposit into Canadian account\n2. Deposit into American account\n3. Transfer funds from CDN to US\n4. Transfer funds from US to CDN\nAnything else exits.\nSelection: ")
		if choice == 1:
			cdnacct = cdnacct + input("How much would you like to deposit in this account? $")
		elif choice == 2:
			usdacct = usdacct+ input("How much would you like to deposit in this account? $")
		elif choice == 3:
			temp=input("How much would you like to transfer? $")
			if temp > cdnacct: raise OverflowError
			else:
				cdnacct=cdnacct-temp
				usdacct=usdacct+temp; del temp
		elif choice == 4:
			temp=input("How much would you like to transfer? $")
			if temp > usdacct: raise OverflowError
			else:
				usdacct=usdacct-temp
				cdnacct=cdnacct+temp; del temp
		else: raise ValueError
	except NameError:
		print "Put in numbers."
	except SyntaxError:
		print "That doesn't make sense."
	except OverflowError:
		del temp
		print "Thats more than you have in your account, aborting operation."
		choice == None
	except ValueError:
			choice=input("Leave?\n0 or False: no\nAnything else: yes\nDecision: ")
			if not choice: pass
			else:
				print "I suppose that is a yes."
				break
			
		
