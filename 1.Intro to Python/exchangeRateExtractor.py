import urllib

def extract(URL, find, offset1, offset2):
	a = ""
	b = []
	c = []
	d = ''
	found = False
	rate = 0.0
	web = urllib.urlopen(URL)
	for line in web.readlines():
		if find in line:
			found = True
			a = line
	if found == False: return -1
	del found
	for letter in range(offset1,offset2):#1796 1802
		b.append(a[letter])
	for letter in range(0,6):
		c.append(b[letter])
	for number in c:
		d = d + number
	rate=float(d)
	return rate

#Program is a COMPLETE MESS, but without an external library, it's the only way I can figure is even possible.
#Reasons I hate it:
#-requires trial & error to find out where exactly the number is
#-requires you to actually provide the function the exact character the number begins at, meaning...
#-if Yahoo changes it's HTML just one character, EVERYTHING WILL BREAK.
#-and for some reason the USD -> CAD conversion site has nonstandard HTML, it requires a different character offset for some reason.
