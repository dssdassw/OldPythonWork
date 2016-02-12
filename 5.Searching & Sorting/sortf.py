def bubble(lst):
	for val in range(len(lst)):
		if lst[val]<lst[val+1]:
			temp = lst[val]
			lst[val]=lst[val+1]
			lst[val+1]=temp
	return lst
		