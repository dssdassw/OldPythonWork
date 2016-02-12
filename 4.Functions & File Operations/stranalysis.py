import string
#The a team here is the best of all the a teams in the country, or at least that is what I think of our a team. 27 words, 4 'the's, 4 single-chr words, 
astr = raw_input("Type something in. Any length is fine, preferably something long.\n")
print 'Number of characters in the string             :',len(astr)
print "Number of times 'the' appears                  :",astr.count('the') + astr.count('The')
print 'Number of times a single-character word appears:',sum([1 for val in astr.split() if len(val) == 1])
print 'Number of words                                :',len(astr.split())