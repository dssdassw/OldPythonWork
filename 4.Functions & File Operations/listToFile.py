def writeToFile(data, file):
	with open(file, 'w') as datafile:
		for piece in data: datafile.write(str(piece))

while True:
	try:
		filen = raw_input("filename: ")
		with open(filen, 'r') as f:
			print "Contents of file (WILL BE OVERWRITTEN ON WRITE!): " + f.read()
		writeToFile(list(raw_input("write something I\'m giving up on you\n")),filen)
		with open(filen, 'r') as f:
			print "Contents of file: " + f.read()
	except:
		print "GODDAMNIT MAN, SNAP OUT OF IT!"