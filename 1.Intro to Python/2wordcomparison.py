satisfied = False
while not satisfied:
	wordA = raw_input("Give me a word.\n")
	wordB = raw_input("Give me another word.\n")
	if wordA != wordB: satisfied = True
if wordA > wordB: print wordB + " would come first in a dictionary."
else: print wordA + " would come first in a dictionary."
