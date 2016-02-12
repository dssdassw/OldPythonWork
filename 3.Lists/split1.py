from splittools import *

while True:
	try:
		valid = False
		sixDigits = raw_input("Please input a 6 digit long string: ")
		if len(sixDigits) != 6: raise UserWarning
		valid = True
		break
	except UserWarning:
		print "\'Please input a 6 digit long string.\'\n\'...input a 6 digit long string.\'\n\'...6 digit long string.\'\n\'...6 digit...\'\nHoo boy, I wonder where you went wrong!\nIt\'s OVER BETWEEN US."
		break

if valid:
	chrlist = str_to_list(sixDigits)
	print chrlist
	print "Largest:.............. " + str(findgreatest(chrlist))
	print "Smallest:............. " + str(findleast(chrlist))
	print "Sum:.................. " + str(findsum(chrlist))
	print "Values greater than 5: " + str(findGT(chrlist, 5))
	print "Most used value:...... " + str(chrlist[findMostFrequent(chrlist)])
	