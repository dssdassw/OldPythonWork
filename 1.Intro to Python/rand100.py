import random
def rand(): num = random.randint(0, 120); return num
num = rand()
while not(num >= 100):
	print num
	num = rand()
print num