bed = raw_input("TELL GOLDILOCKS A STRING PLEASE\n")
if len(bed) < 8:
	print "GOLDILOCKS HATES YOU AND YOUR CHOICE OF STRING LENGTH. IT WAS TOO DAMN SHORT."
elif len(bed) > 8:
	print "GOLDILOCKS HATES YOU AND YOUR CHOICE OF STRING LENGTH. IT WAS TOO DAMN LONG."
else:
	print "Finally, Goldilocks is pleased with something."
