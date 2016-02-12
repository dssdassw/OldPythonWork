def str_to_list(str):
	lst = []
	for character in str:
		lst.append(character)
	return lst
def findgreatest(alist):
	greatest = alist[0]
	for item in alist:
		if item > greatest: greatest = item
	return greatest
def findleast(alist):
	least = alist[0]
	for item in alist:
		if item < least: least = item
	return least
def findsum(alist):
	listSum = 0
	for item in alist:
		while True:
			try:
				listSum = listSum + int(item)
				break
			except ValueError:
				print item + " can't be added to the sum, skipping..."
				break
	return listSum
def findGT(alist, comparison):
	values = []
	worked = False
	for item in alist:
		worked = False
		while True:
			try: item = int(item)
			except ValueError: print item + " can't be converted to integer, skipping..."
			break
		if worked:
			if item > int(comparison): values.append(item)
	return values
def findMostFrequent(alist):
	char = []
	uses = []
	freq = 0
	secondmost = 0
	for item in alist:
		if item not in char: char.append(item)
		uses.append(alist.count(item))
	for x in range(len(char)):
		if uses[x] > uses[freq]:
			secondmost = freq
			freq = x
	if uses[secondmost] == uses[freq]: print "... actually, no value is the most. One of the most, however, is... "
	return x