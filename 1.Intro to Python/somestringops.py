#I am not going to follow the doc exactly because that's too boring.
msg = 'This message is 2secret4you'
print "I have made a super secret message. You will only be able to read it one character at a time."
print "Which character would you like to see? The string is " + str(len(msg)) + " characters big, and the index starts at 0.\n"
while True:
	try:
		index = input("")
		if index < 0 or index > (len(msg)+1):
			raise ValueError
		print str(index) + "th character: " + str(msg[index])
	except NameError:
		print "Why do people insist on inputting non-numerical values..."
	except SyntaxError:
		print "Whatever you just put in doesn't make sense."
	except ValueError:
		print "I take it you want to leave."
		break
		
guess = raw_input("So what do you think the message said? Caps count.\n")
if guess == msg: print "Spot on."
elif guess > msg: print "The first characer in your guess comes before the first character of the right message in the alphabet."
elif guess < msg: print "The first characer in your guess comes after the first character of the right message in the alphabet."
