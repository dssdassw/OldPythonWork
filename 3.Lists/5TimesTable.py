table = [[]]
table = [[0 for x in range(10)] for x in range(10)] 
x = 0
y = 0
for x in range(10):
	for y in range(10):
		table[x][y] = x * 5
for x in range(y):
	print table[x][y]