from datetime import date
import random

datel = []
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
suff = ""

def get_suffix(datel):
	if datel[0] == 1:
		return "st, "
	elif datel[0] == 2:
		return "nd, "
	elif datel[0] == 3:
		return "rd, "
	else: return "th, "
while True:
	while True:	
		try:
			choice = input("1. Use current date.\n2. Use a randomly generated date.\nAnything else will exit.\n")
			break
		except ValueError: print "What?"
		except NameError: print "What?"
		except SyntaxError: print "What?"
		except OverflowError: print "That's invalid."
	if choice == 1:
		dtoday = str(date.today())
		print dtoday
		for res in dtoday.split('-', -1):
			datel.append(res)		
		print datel
		suff = get_suffix(datel)
		datel[2] = months[int(datel[2])]
		print datel[2], str(datel[1]) + suff + str(datel[0])
	elif choice == 2:
		d_in_m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		y = random.randint(1900, 2100)
		m = random.choice(months) #even though they are arranged in a different order on output, they have to be assigned like this so that you don't have, say the 30th of February.
		d = random.randint(1, d_in_m[months.index(m)])
		datel = [y, d, m]
		suff = get_suffix(datel)
		print datel[2], str(datel[1]) + suff + str(datel[0])
	else: break