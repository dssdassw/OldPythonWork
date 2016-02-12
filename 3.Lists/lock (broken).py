import random
#can I pass variables and store them each in a seperate stack, accumulating as the function traces back?
#I can try...
def keygen(keys, kc, key):
	if key not in keys:
		key = keygen(keys, kc, random.randint(0,9))
	elif key in keys:
		kc = kc + 1
		keygen(keys, kc, key)
	"""if len(key) == 0:
		keys.append(random.randint(0,9))
		print keys
	if len(key) < 8:
		new = random.randint(0,9)
		print new
		if new in keys:
			print "Recursively calling..."
			keygen(keys)
		else: keys.append(new)"""
	if kc == 8:
		print "Returning one stack up...."
		return keygen(keys, kc, key)
		
a = []
keys = keygen(a, 0, 0)
print "recieved value:" + str(keys)