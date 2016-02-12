def rStore(fn):
	with open(fn, 'r') as f:
		return [line[:-1:] if line[len(line)-1] == '\n' else line for line in f]
def rSpace(fn):
	with open(fn, 'r') as f:
		return f.read().replace('\n', ' ')
def rSeper(fn):
	a=""
	with open(fn, 'r') as f:
		for line in file:
			a+=line
		return a
def lst2str(lst):
	s = ""
	for item in lst:
		s+=str(item)+'\n'
	return s
def ow(fn, something):
	if something is list: something = lst2str(something)
	with open(fn, 'w') as f:
		f.write(str(something))
def aw(fn, something):
	if something is list: something = lst2str(something)
	with open(fn, 'a') as f:
		f.write(str(something))
def rPrint(fn):
	with open(fn, 'r') as f:
		for line in f: print f
try:
	print 'Testing functions...'
	print '------------------------'
	print '------------------------'
	print rStore('abc')
	print '------------------------'
	print rSpace('abc')
	print '------------------------'
	print lst2str(['a', 'b', 'c', 1, 2, 3])
	print '------------------------'
	ow('tst', "This is stupid")
	print rSpace('tst')
	print '------------------------'
	aw('tst', ", but it doesn't matter.")
	print rSpace('tst')
	print '------------------------'
	rPrint('abc')
	print '------------------------'
	print '------------------------'
	print 'Testing complete!'
	print '------------------------\n\n'
except:
	import sys
	print "An error occured when testing functions!\n" + str(sys.exc_info())