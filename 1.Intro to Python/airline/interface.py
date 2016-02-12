import random; from plane import plane; from functions import *
#Added a functional waiting list, 
hamilton = plane(500, 0, 20)
bahamas = plane(1000, -20, 5)
moscow = plane(1700, -5, 10)
print "HAMILTON FLIGHT SEATS:" + str(hamilton.seats) + "\nBAHAMAS FLIGHT SEATS:" + str(bahamas.seats) + "\nMOSCOW FLIGHT SEATS: " + str(moscow.seats)
choice = 0
notdone = True
print "Welcome to Toronto International Airport!"

while notdone:
	choice = choose("\n1. Book a flight\n2. Cancel a flight\n3. File a complaint\n4. Exit\n")
	if choice == 1:
		choice = choose("Book a flight to...\n1. Hamilton\n2. The Bahamas\n3. Moscow\n")
		if choice == 1:
			booking(hamilton)
		elif choice == 2:
			booking(bahamas)
		elif choice == 3:
			booking(moscow)
			
	if choice == 2:
		choice = choose("Cancel which flight?\n1. Hamilton\n2. The Bahamas\n3. Moscow\n")
		if choice == 1:
			if hamilton.booked: hamilton.cancel()
		elif choice == 2:
			if bahamas.booked: bahamas.cancel()
		elif choice == 3:
			if moscow.booked: moscow.cancel()
	
	if choice == 3:
		temp = random.randint(1, 6)
		if temp > 2:
			complaint = raw_input("On behalf of the Toronto International Airport, I apologize.\nPlease issue your complaint and I will pass it on to my superiors.\n")
			print "Thank you, and once again, we apologize. You will be granted a $" + str(10*len(complaint)) + " dollar settlement."
		else: print "Sorry, but we waited six weeks and did not hear from you, therefore you may no longer issue any complaints."
	
	if choice == 4:
		break
