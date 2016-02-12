ascii = [ord(char) for char in raw_input("Give me a string.\n")]; print ascii
asciiPLUS = [num+1 for num in ascii]; print asciiPLUS
for num in range(len(asciiPLUS)):
	if asciiPLUS[num] == ord('{'):
		asciiPLUS[num] = ord('a')
	if asciiPLUS[num] == ord('['):
		asciiPLUS[num] = ord('A')
print asciiPLUS
chrasciiPLUS = [chr(num) for num in asciiPLUS]
s = ''
for value in chrasciiPLUS: s += value
print s