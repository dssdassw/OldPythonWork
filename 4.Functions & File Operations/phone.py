import string
#Toronto (416 or 647) or the GTA (905 or 289)
#I don't think using substring is the most logical thing here.
#Because the area code is always at the beginning of the string.
#So I should instead just check the first three digits against the codes.
phonenum = raw_input("What's your phone number? Note, if you input something larger than 10\nnumbers long, it'll be shortened to 10 numbers.\n> ")
phonenum = phonenum.replace(" ", ""); phonenum = phonenum.replace("-", "")
phonenum = phonenum.replace("(", ""); phonenum = phonenum.replace(")", "")
areacode = str(phonenum[:3:])
if areacode == '416' or areacode == '647':
	print "You live in Toronto, then?"
elif areacode == '905' or areacode == '289':
	print "You live in the GTA?"
else:
	print "...and where might that be?"