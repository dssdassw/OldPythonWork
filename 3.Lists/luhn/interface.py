import luhn

"""\
def get_csum(num):
	def of(digits):
		return [int(d) for d in str(digits)]
	digits = of(num)
	odd = digits[-1::-2] #From -1 to (assumed) end, by step -2
	even = digits[-2::-2]
	csum = 0; csum += sum(odd)
	for digit in even:
		csum += sum(of(digit*2))
	return csum % 10

def calc(num):
	checkdigit = get_csum(int(num) * 10)
	return check_digit if check_digit == 0 else 10 - check_digit

def rand_card_number():
	return ''.join([str(random.randint(0,9)) for i in range(0,(random.choice([9,16])))])"""
validDigits=['0','1','2','3','4','5','6','7','8','9']
while True:
	try:
		digits = raw_input("Please input a 9 or 16 digit long string of numbers: ")
		if len(digits) != 9 and len(digits) != 16: raise UserWarning
		for digit in digits:
			if digit not in validDigits:
				raise ValueError
		break
	except UserWarning:
		print "\'Please input a 9 or 16 digit long string.\'\n\'...input a 9 or 16 digit long string.\'\n\'...9 or 16 digit long string.\'\n\'...9 or 16 digit...\'\nHoo boy, I wonder where you went wrong!\nIt\'s OVER BETWEEN US."
		break
	except ValueError:
		print "I said OF NUMBERS."
del validDigits
print luhn.get_csum(digits)
luhn.alt_csum(digits)