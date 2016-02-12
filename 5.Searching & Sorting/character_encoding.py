c1 = 'a'
print ord(c1)
print ord(c1)

#print ASCII number for every letter in the string
str = "This is a test"
for c in range(0, len(str)):
	print ord(str[c])

#number --> letter
num1 = 90 #Z
print chr(num1)

#print the character for every number in the range 97-122
for c in range(1,255):
	print c,chr(c),