def choose(enum_choices, choicelist):
	ch = 1
	if len(choicelist) == enum_choices:
		querystr = ""
		choice_n = 0
		for choice in choicelist:
			choice_n += 1
			querystr += (str(choice_n) + ". " + choice + "\n")
		querystr += "> "
		while True:
			try:
				ch = input(querystr)
				if ch not in range(enum_choices+1): raise UserWarning
				break
			except: print "Invalid."
	return ch
def reader(enc, fn):
	with open(fn, 'r') as f:
		if enc == 1:
			return f.read().replace('\n', ' ')
		elif enc == 2:
			ll = [line[:-1] for line in f]
			lstr = ""
			for item in ll:
				lstr = lstr + item + ", "
		elif enc == 3:
			for line in f: print line
		else: print "ERROR"
def writer(fn, to_write):
	if to_write is list:
		o = ""
		for v in to_write: o += (v + " ")
		to_write = str(o)
	with open(fn, 'w') as f:
		a = reader(1,fn)
		f.write(a + str(to_write))
def get_num(inmsg = "Input > "):
	while True:
		try:
			inp = input(inmsg)
			return inp #can probably shorten to one line.
		except:
			print "That's not a number!"
		