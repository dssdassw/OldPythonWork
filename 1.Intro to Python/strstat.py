import string

inp = raw_input("Give me a string.\n")
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
letterc = 0; vowelc = 0; spacec = 0; specc = 0
for letter in inp:
	if letter in string.ascii_letters:
		letterc = letterc + 1
	elif letter not in string.whitespace: specc = specc + 1
	if letter in vowels:
		vowelc = vowelc + 1
	if letter in string.whitespace:
		spacec = spacec + 1
print "Letters: " + str(letterc) + "\nVowels (including y): " + str(vowelc) + "\nSpaces: " + str(spacec) + "\nOther (not including spaces): " + str(specc)
