import random

class plane:
	def __init__(self, cost, low, high, predetermined = False, predeterminedValue = 0):
		self.charges = []
		self.low = low; self.high = high
		self.cost = float(cost); self.ocost = float(cost)
		self.charges.append("Base flight price: $" + str(self.cost))
		self.booked = False
		if not predetermined: self.seats = random.randint(low, high)
		else: self.seats = predeterminedValue
		self.hst = 0.0
	def book(self, seats, dtf):
		if seats > self.seats:
			print "There aren't enough seats to accomotate you. Please wait until the day of your flight, maybe enough people will cancel their flights."
			while dtf!=0:
				dtf = dtf - 1
				print "\n" + str(dtf) + " days to flight...\n"
				self.seats = self.seats + random.randint(0, 7)
				if self.seats < -1: print str(-1*self.seats) + " people remain on the waiting list."
				elif self.seats > 0:
					print str(self.seats) + " seats are open."
					if self.seats > seats:
						print "You made the flight!"
						return True
			else:
				print "\nSorry, this flight doesn\'t have enough seats to accomodate you.\nChoose another flight or shrink the number of people you are seating.\nI should inform you that on this flight, there are " + str(self.seats) + " available."
			return False
		else:
			self.booked = True
			print "Alright, I\'ll reserve " + str(seats) + " seats for you."
			return True
	def upgrade(self):
		self.charges.append("Upgrade to first class: + $" + str(self.cost*0.1))
		self.cost = self.cost*1.10
	def baggage(self, weight):
		if weight > 20:
			print "That means you\'ll be charged $" + str(10*(weight-20)) + " for being " + str(weight-20) + " over the 20kg limit."
			self.charges.append(str(weight-20) + " kg over 20 kg limit: + $" + str(10*(weight-20)))
			self.cost = self.cost + 10*(weight-20)
		else:
			print "You aren\'t over the 20kg limit, we won\'t charge you."
	def checkout(self):
		self.charges.append("HST: + $" + str(0.13*self.cost))
		self.hst = 0.13*self.cost; self.cost = self.cost+self.hst
		b = 0
		print "\n"
		for charge in self.charges:
			a = len(charge)
			if a > b: b = a
		for charge in self.charges:
			print (len(charge)-b)*" " + charge
		print "---------------------------------\nTotal: $" + str(self.cost)
	def cancel(self):
		print "Cancelling this flight will incur you a $" + str(0.2*self.cost) + " charge, but we will reimburse you of your $ " + str(self.hst) + " HST."
		print "This means that, in total, you will be charged " + str((0.2*self.cost) - self.hst) + "."
		while True:
			try:
				choice = input("Is this what you want to do? (If it is, type 1 or True. Otherwise, type anything else.)\n")
				break
			except NameError: print "This is a very serious matter. Please don\'t fool around."
		print self.charges, self.low, self.high, self.cost, self.ocost, self.booked, self.seats, self.hst
		if choice == True: self.__init__(self.ocost, self.low, self.high, True, self.seats)
		print self.charges, self.low, self.high, self.cost, self.ocost, self.booked, self.seats, self.hst
