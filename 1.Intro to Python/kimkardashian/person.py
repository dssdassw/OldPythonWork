import random
class person:
	def __init__(self, type):
		if type == 'press':
			fn = ['Jim', 'Bill', 'Bob', 'John', 'Jack', 'Mack', 'Chris'] #the press names are all male because I don't really know why. 7
			ln = ['Jackson', 'Smith', 'Carrier', 'Edmond', 'Cooper', 'White', 'Grayson']
			self.name = random.choice(fn) + ' ' + random.choice(ln)
			classes = ['Lead reporter', 'Veteran reporter', 'Esteemed journalist', 'Intern']
			self.job = random.choice(classes)
			lpv = 0 #lowest possible value, for max health
			hpv = 100
			if self.job == classes[0]: lpv = 75
			elif self.job == classes[1]: lpv = 60
			elif self.job == classes[2]: lpv = 50
			elif self.job == classes[3]: lpv = 40
			print self.job + ' ' + self.name + " of the Nobodycares Press!"
			hpv = lpv + 25
			self.health = random.randint(lpv,hpv)
			del classes
		elif type == 'celeb':
			fn = ['Khloe', 'Kim', 'Kylie', 'Kourtney']
			self.name = random.choice(fn) + ' Kardashian'
			classes = ['Director', 'Actor', 'Stage hand', 'Reality TV star']
			self.job = random.choice(classes)
			lpv = 0
			if self.job == classes[0]: lpv = 75
			elif self.job == classes[1]: lpv = 60
			elif self.job == classes[2]: lpv = 50
			elif self.job == classes[3]: lpv = 40
			hpv = lpv + 25
			print self.name + " is being assaulted by the papparazzi, who want the scoop on her decision to become a " + self.job + "!"
			self.health = random.randint(lpv,hpv)
			del classes
		self.healthorig = self.health
		self.hits = 0
		self.misses = 0
		self.hits_taken = 0
		self.alive = True
	def assess(self):
		if self.health < 0:
			print self.name + " was defeated!"
			self.alive = False
	def user(self, target):
		done=False
		print self.name + " health: " + str(self.health)
		print target.name + " health: " + str(target.health)
		print "\n"
		while not done:
			try:
				choice = input("1. Punch\n2. Kick\n")
				if choice == 1: self.punch(target)
				elif choice == 2: self.kick(target)
				else: raise ValueError
				done = True
			except NameError:
				print "Put in numbers."
			except SyntaxError:
				print "That doesn't make sense."
			except ValueError:
				print "That isn't a valid option."
		target.assess()
		del done
	def ai(self, target):
		choice = random.randint(0,1)
		if choice == 0: self.punch(target)
		if choice == 1: self.kick(target)
		target.assess()
	def punch(self, target):
		hit = random.randint(0,4)
		if hit > 3:
			print self.name + ' missed.'
			self.misses = self.misses + 1
		else:
			damage = random.randint(10,20)
			self.hits = self.hits + 1
			target.hits_taken = target.hits_taken + 1
			target.health = target.health - damage
			print self.name + ' dealt ' + str(damage) + ' damage to ' + target.name + '!'
			del damage
	def kick(self, target):
		hit = random.randint(0,4)
		if hit > 2:
			print self.name + ' missed.'
			self.misses = self.misses + 1
		else:
			damage = random.randint(20,30)
			self.hits = self.hits + 1
			target.hits_taken = target.hits_taken + 1
			target.health = target.health - damage
			print self.name + ' dealt ' + str(damage) + ' damage to ' + target.name + '!'
			del damage
