from security import protect
from exchangeRateExtractor import extract
import urllib
import datetime

transac=open('transac.txt', 'r+')
lastrem=open('lastconvrates.txt', 'r+')
cdnrate = extract('https://ca.finance.yahoo.com/q?s=CADUSD=X', "<span id=\"yfs_t10_cadusd=x\">", 1796, 1802)
usdrate = extract('https://ca.finance.yahoo.com/q?s=USDCAD=X', "<span id=\"yfs_l10_usdcad=x\"", 1792, 1798)
if cdnrate == -1: cdnrate=int(lastrem.readline())
elif usdrate == -1:
	for num in range(0,2):
		 usarate=lastrem.readline()
else: lastrem.write(str(cdnrate) + "\n" + str(usdrate) + "\n" + str(datetime.datetime.now())); lastrem.close()
print "Currecy conversion rates successfully receved for " + str(datetime.datetime.now())
print "CAD -> USD: " + str(cdnrate)
print "USD -> CAD: " + str(usdrate)
cdnacct=0.0
usdacct=0.0
invalue=0.0
protect()
while True:
	try:
		print "\nCanadian account balance: $" + "%0.2f"%cdnacct + "\nAmerican account balance: $" + "%0.2f"%usdacct + "\n"
		choice = input("1. Deposit into Canadian account\n2. Deposit into American account\n3. Transfer funds from CDN to US\n4. Transfer funds from US to CDN\n5. View your transaction history.\n Anything else exits.\nSelection: ")
		if choice == 5:
			for line in transac:
				transac.readlne()
		if choice == 1:
			invalue = input("How much would you like to deposit in this account? $")
			cdnacct = cdnacct + invalue
			transac.write(str(datetime.datetime.now()) + ": deposited $" + str(invalue) + " into Canadian acount.")
		elif choice == 2:
			input("How much would you like to deposit in this account? $")
			usdacct = usdacct + invalue
			transac.write(str(datetime.datetime.now()) + ": deposited $" + str(invalue) + " into American acount.")
		elif choice == 3:
			invalue=input("How much would you like to transfer? $")
			temp=cdnrate*invalue
			if temp > cdnacct: raise OverflowError
			else:
				transac.write(str(datetime.datetime.now()) + ": transferred $" + str(invalue) + " CAD into American account. ($" + str(temp) + " USD)")
				cdnacct=cdnacct-temp
				usdacct=usdacct+temp; del temp
		elif choice == 4:
			invalue=input("How much would you like to transfer? $")
			temp = usdrate*invalue
			if temp > usdacct: raise OverflowError
			else:
				transac.write(str(datetime.datetime.now()) + ": transferred $" + str(invalue) + " USD into Canadian account. ($" + str(temp) + " CAD)")
				usdacct=usdacct-temp
				cdnacct=cdnacct+temp; del temp
		else: raise ValueError
		del choice
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
			if choice: transac.close(); break
				
