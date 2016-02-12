import random
from tools import conv_str

def of(digits):
	return [int(d) for d in str(digits)]

def add_of_single(numlist):
	for num in numlist:
		if len(list(str(num)))>1: num = int(str(num)[0]) + int(str(num)[1])
		else: pass
	return numlist

def pop_conv(strnum):
	num = list(str(strnum))
	last = 0
	if len(strnum)>0: last = int(num.pop())
	num = conv_str(num)
	return num, last

def lastof(num):
	return str(num)[len(str(num))-1]

def get_csum(num, printvalues = False):
	digits = of(num)
	odd = digits[-1::-2] #From -1 to (assumed) end, by step -2
	even = digits[-2::-2]
	if printvalues: print odd,even
	csum = 0; csum += sum(odd)
	for digit in even:
		csum += sum(of(digit*2))
	return csum % 10

def calc_ccn(num): #Solely returns the check digit.
	try:
		check_digit = get_csum(int(num) * 10)
		return check_digit if check_digit == 0 else 10 - check_digit
	except ValueError:
		print "Error."
		return ''

def ccn_valid(num):
	return get_csum(num) == 0

def sin_valid(num, printvalues = False):
	num, check_digit = pop_conv(num)
	if calc_sin(num) == check_digit: return True
	else: return False

def calc_sin(num):
	try:
		sin = (10 - int(lastof(sum([int(number) for number in num[::2]]) + sum(add_of_single([int(number)*2 for number in num[1::2]])))))
		if sin == 10: sin = 1
		return sin
	except ValueError:
		print "Error"
		return ''

def rand_ccn():
	ccn = ''.join([str(random.randint(0,9)) for i in range(15)])
	ccn += str(calc_ccn(ccn))
	return ccn

def rand_sin():
	sin = ''.join([str(random.randint(0,9)) for i in range(8)])
	if sin[len(sin)-1] == 0: sin.pop()
	sin += str(calc_sin(sin))
	return sin

def alt_valid(num):
	num, last = pop_conv(num)
	digits = of(num)
	digits = digits[::-1]
	digits = of(num)
	odd = [val*2 for val in digits[0::2]]
	for val in odd:
		if val > 9: val -= 9
	even = digits[1::2]
	final = of((sum(even) + sum(odd) + last))
	if final[len(final)-1] == last: return True
	else: return False