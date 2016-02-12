import sort #a bunch of functions I made during the searching and sorting unit that are very helpful.
lstfib = []
n1 = 1
n2 = 0
temp = n1
menuChoice = 0
c = 0
for i in range(0,20):
	temp = n1
	n1 = n2
	n2 = temp+n1
	lstfib.append(n2)
	print n2

while(1): #Instead of making while check a variable, which would impact performace (though I know it doesn't matter), I'm just going to use break to end the loop whenever I wish.
	menuChoice = input("Welcome to the Fibonacci Menu!\n\n1. Show the contents of the list\n2. Show the even values in the sequence only\n3. Remove all the odd values in the sequence\n4. Sort the list in reverse order\n5. Use a for loop to add all the numbers in the list and show the result\n6. Show all of the numbers containing at least 4 digits\n7. Exit\n> ")
	if menuChoice == 1:
		for i in lstfib: print i
	if menuChoice == 2:
		for i in lstfib:
			if i % 2 == 0: #because even numbers are all divisible by 2.
				print i
	if menuChoice == 3:
		c = 0
		while(c<len(lstfib)):
			if lstfib[c] % 2 != 0:
				retval = lstfib.pop(c) #for some reason pop doesn't actually pop.
				print retval
			else: print lstfib[c],"is an even number."
			c+=1
	if menuChoice == 4:
		print lstfib
		lstfib = sort.bubble(lstfib, False, 'rev')
		print lstfib
	if menuChoice == 5:
		ans = 0
		for i in lstfib: ans+=i
		print ans
	if menuChoice == 6:
		for i in lstfib:
			if i > 999:
				print i
	if menuChoice == 7:
		break
			