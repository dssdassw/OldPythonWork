from person import person
incomplete = True
press = person('press')
kardashian = person('celeb')
print "Note, kicking has a lower hit chance than punching, but does higher damage.\n"

while incomplete:
	kardashian.user(press)
	if not press.alive: break
	press.ai(kardashian)
	if not kardashian.alive: break

print "\nHere are your stats!\nHealth lost: " + str(kardashian.healthorig - kardashian.health) + " points.\nHits taken: " + str(kardashian.hits_taken) + "\nSuccessful hits: " + str(kardashian.hits) + "\nMisses: " + str(kardashian.misses) + "\nHit percent: " + str(100*(float(kardashian.hits)/float(kardashian.hits+kardashian.misses))) + "%"
