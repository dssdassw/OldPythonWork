fwd = raw_input("Give me something to work with.\n")
print "\n\n"
lst = list(fwd)
lst.reverse()
rev = ''
for letter in lst:
	rev = rev + letter
print fwd + " backwards is " + rev
