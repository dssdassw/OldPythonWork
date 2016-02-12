import random
randlist = []
for i in range(20):
	randlist.append(random.randint(0,999999))
randlist.sort()
print randlist[0], randlist[(len(randlist) - 1)]