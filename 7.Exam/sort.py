def seq_search(val, lst):
	for item in lst:
		if item == val:
			return lst.index(item)
	
def bin_search(l, value, low = 0, high = -1): #from http://rosettacode.org/wiki/Binary_search#Python, recursive type.
	if not l: return -1
	if(high == -1): high = len(l)-1
	if low == high:
		if l[low] == value: return low
		else: return -1
	mid = (low+high)//2
	if l[mid] > value: return binary_search(l, value, low, mid-1)
	elif l[mid] < value: return binary_search(l, value, mid+1, high)
	else: return mid

def bubble(lst, show = False, direction = 'fwd'):
	c = len(lst)-2
	if direction == 'fwd':
		while c != 0:
			for val in range(len(lst)-1):
				try:
					if lst[val]>lst[val+1]:
						temp = lst[val+1]
						lst[val+1] = lst[val]
						lst[val] = temp
				except:
					if lst[val-1]>lst[val]:
						temp = lst[val-1]
						lst[val-1] = lst[val]
						lst[val] = temp
			if show: print lst
			c -= 1
	elif direction == 'rev':
		while c != 0:
			for val in range(len(lst)-1):
				try:
					if lst[val]<lst[val+1]:
						temp = lst[val+1]
						lst[val+1] = lst[val]
						lst[val] = temp
				except:
					if lst[val-1]<lst[val]:
						temp = lst[val-1]
						lst[val-1] = lst[val]
						lst[val] = temp
			if show: print lst
			c -= 1
	else: print "Invalid direction. Type 'rev' for reverse sorting, and nothing or 'fwd' for forward sorting."
	return lst

def insertion(lst): #heavily based on http://www.teachingtree.co/watch/insertion-sort
	for index in range(1, len(lst)):
		v = lst[index]
		i = index - 1
		while i>=0:
			if v < lst[i]:
				lst[i+1] = lst[i]
				lst[i] = v
				i -= 1
			else:
				return lst