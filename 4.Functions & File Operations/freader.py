def reader(enc, fn):
	with open(fn, 'r') as f:
		if enc == 1:
			print f.read().replace('\n', ' ')
		elif enc == 2:
			ll = [line[:-1] for line in f]
			lstr = ""
			for item in ll:
				lstr = lstr + item + ", "
			print lstr
		elif enc == 3:
			for line in f: print line
		else: print "ERROR"

while True:
	inp = input("I'll read a file for you. How do you want it to be read?\n1. Each item seperated by a single space\n2. Comma-seperated items\n3. Each item on it\'s own line.\n") 
	reader(inp, 'fl')
	break