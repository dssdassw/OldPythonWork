import random
diceA = random.randint(1,6)
diceB = random.randint(1,6)
while diceA != diceB:
	print diceA, diceB
	diceA = random.randint(1,6)
	diceB = random.randint(1,6)
print diceA, diceB