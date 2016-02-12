from splittools import findgreatest, findleast
import random

lst = [8,7,6,5,4,3,2,1]
while (findgreatest(lst) != lst[7] and findleast(lst) != lst[0] or lst[0] == lst[7]):
	lst = []
	for i in range(0,8):
		lst.append(random.randint(0,9))
	print lst