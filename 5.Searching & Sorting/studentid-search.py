import random
import tools

numbers=[]
for i in range(0,10): #THINK OF A BETTER WAY TO DO THIS LATER
	invalid = True
	while invalid:
		number = random.randint(0,101)
		if number not in numbers:
			numbers.append(number)
			invalid = False

if get_num("Guess a number from 0 to 100. If it's in a list of 10 numbers, you win!") in numbers:
	print 'You win!'
else:
	print 'You lose...'