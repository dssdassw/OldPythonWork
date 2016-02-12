import tools #tools.reader(1, 'friends'). Output can be split by the ' '.

def get_choice():
	print "-- FRIENDS LIST --"
	return tools.choose(5, ["Add friends", "Read friends list from file", "Write friends list to file", "Print friends list", "Exit"])
friends = [] #If you want it to initialize with the values in the file, do that after.
i = get_choice()
while True:
	if i == 1:
		tmp = " "
		while tmp != "":
			tmp = raw_input("New friend\'s name (Enter to end): ")
			if tmp not in friends and tmp != "": friends.append(tmp)
		if len(friends) == 0: friends.append("Greg")
	elif i == 2:
		friends += [a for a in tools.reader(1, 'friends').rsplit() if a not in friends]
	elif i == 3:
		tools.writer('friends', friends)
	elif i == 4: tools.reader(3, 'friends')
	elif i == 5: break
	i = get_choice()
	