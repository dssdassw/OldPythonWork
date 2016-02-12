import random

price = random.uniform(1.00, 100.00)
price = round(price, 2)
print "Let\'s say you payed $" + str(price) + " for something."
print "You'd pay $" + str(round((1.13*price), 2)) + " after tax for that item"