import random
lock = []
lockstr = ""

#Program would look like it does everything by magic if these functions were moved to a different file.
def keygen(lock):
	while len(lock) != 8:
		newkey = random.randint(0,9)
		if newkey not in lock:
			lock.append(newkey)
	lockstr = ""
	for digit in lock: lockstr = lockstr + str(digit)
	return lock, lockstr
def hack(lock):
	slot = 0
	hackedval = ""
	while slot != 8:
		digit = random.randint(0,9)
		if digit == lock[slot]:
			print str(digit) + "... correct for that slot\n"
			hackedval = hackedval + str(digit)
			slot = slot + 1
		else: 
			print str(digit) + "... incorrect for slot #" + str(slot+1)
	print "M45t3r-h4><><0r.9001 has\ndiscovered that the value\nis " + hackedval
#But I'm not going to do that, because I don't really feel like it.

lock, lockstr = keygen(lock)
print "--------------------------\n     LOCK COMBINATION\n--------------------------\n---------" + lockstr + "---------\n--------------------------"
print "\nNow, watch the terribly\ninefficient hacker try to\nfigure that out.\n\n"
hack(lock)