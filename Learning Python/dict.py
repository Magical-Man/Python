#Creates a mapping of state to abbreviation
states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'NY',
    'Michigan' : 'MI',
}

#Creates a basic set of states and some cities in them
cities = {
    'CA' : 'San Fransisco',
    'MI' : 'Detroit',
    'FL' : 'Jacksonville'

}

#Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#Print some states
print('-' * 10)
print("Michigans abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#Do it by using the st ae then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])

#Print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

#Print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("%s Has the city %s" % (abbrev, city))

#Now do both at the same time
print('-' * 10)
for state, abbrev in states.items():
    print("%s state is abbreviated %s and has the city %s" % (state, abbrev, cities[abbrev]))

print('-' * 10)
#Safley get a abbreviation by state that might not be there

if not state:
    print("Sorry, no Texas.")

#Get a city with a defualt value
city = cities.get('TX', 'Does Not Exist')
print("The city for the state 'TX' is: %s" % city)

#The .items() module will print the thing, iwht the assignment

#A dictionary in this is jsut like in real life, where the x is the term and the y is the def
