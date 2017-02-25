##Here what we are doing is just declaring a variable, and then printing some stuff

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not 10 things in that list. Let's fix that.")

##Here we declare a variable assigned to the ten_things var, but split

##Then we make a list called more_stuff

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

##Here we make a loop that is adding to more_stuff from stuff

while len(stuff) != 10:
    next_one = more_stuff.pop()             #Because there is nothing specified in .pop() the default is the last item

    print("Adding: ", next_one)

    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])             #Here we just say to grab the second item, this is becuase of cardinal nums

print(stuff[-1])            #Here we are grabbing the last item cause integers nad negativces

print(' '.join(stuff))          #Here we say to make everything in stuff back into one string

print("#".join(stuff))          #Same but sperate w/ #

print("#".join(stuff[3:5]))         #Here we say print eveything between item 4 and 6
