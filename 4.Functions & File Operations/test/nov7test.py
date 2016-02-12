import func

def alphaCity(cityA, cityB):
	return cityA if cityA < cityB else cityB

cities = func.rStore('data.txt')
num = cities.pop(0)
print func.lst2str(cities[::-1])
print alphaCity(raw_input("Write a city name: "), raw_input("Now write another: ")) + ' comes first alphabetically.'
try: cities.insert(input("Where would you like me to add to this list? (First value is 0): "), raw_input("And what is it that you\'d like to add?: "))
except: print "I'm afraid I didn't understand that.\nToo bad, so sad."
finally: print func.lst2str(cities)
for city in cities: print city,':',len(city)