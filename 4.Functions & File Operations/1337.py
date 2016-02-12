# -*- coding: UTF-8 -*-

def make1337(s):
	import string
	s = s.replace('A', '4')
	s = s.replace('C', '(')
	s = s.replace('E', '3')
	s = s.replace('l', '|')
	s = s.replace('L', u'\u255A') #lolwut
	s = s.replace('M', "/\\/\\")
	s = s.replace('N', "/\\/")
	s = s.replace('S', '$')
	s = s.replace('T', '7')
	s = s.replace('W', "\\/\\/")
	s = s.replace('X', '><')
	return s
not1337 = raw_input("Input a message: ")
print make1337(not1337)