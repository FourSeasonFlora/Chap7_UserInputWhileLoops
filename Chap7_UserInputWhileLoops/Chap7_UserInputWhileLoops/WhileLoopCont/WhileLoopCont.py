#refresh
makingplans = "\nWhere would you like to go for dinner? "
makingplans += "Enter 'quit' to exit the PlanMaker.\n"
thedecider =""
while thedecider != 'quit':
    thedecider = input (makingplans)
    if thedecider != 'quit':
        print (f'\n{thedecider.title()} has been recorded.')

#using a flag
#starts while loop as active. if statments checks the input for quit. aka to see if its false.
shoppinglist = "\nPlease provide the item you would like to add to the shopping list. "
shoppinglist += "Enter 'quit' to exit The List Maker.\n"
shopping =""
working = True
while working:
    shopping = input (shoppinglist)
    if shopping == 'quit':
        working = False
    elif shopping == 'cheddar':
        print (f'\nGet some {shopping.title()}!')
    else:
        print (f'\n{shopping.title()} has been recorded.')

#filling a dictionary with user input
cities = {}
active_cities = True
while active_cities:
    places = input ('\nPlease enter a city: ')
    school = input ('\nPlease provide coresponding school district: ')
    cities [places] = school  
    anotherone = input ('\nAny other cities you would like to add to the list? y/n: ')
    if anotherone == 'n':
        active_cities = False
print ('\nThis is our list...\n')
for places, school in cities.items ():
    print (f'{places.title()} is in {school} district.')