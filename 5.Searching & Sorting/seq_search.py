import sort
import random

nums = [random.randint(0,26), random.randint(0,26), random.randint(0,26), random.randint(0,26), random.randint(0,26), random.randint(0,26), random.randint(0,26), random.randint(0,26), random.randint(0,26), random.randint(0,26)]
a = sort.seq_search(input("Input a number from 0 to 25. If the number\nis in a list of 10 random numbers in that range, I'll tell you where.\n> "), nums)
if a != None:
	print "Value found at the index of",a
else: print "Value not found..."