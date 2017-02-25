#The variables in our functions are not connected to the vars in our script

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d chesses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man, that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from out script:")
ammount_of_chesses = 10
ammount_of_crackers = 50

cheese_and_crackers(ammount_of_chesses, ammount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(ammount_of_chesses + 100, ammount_of_crackers + 1000)

#here we just show the different ways that we can pass in func arguments
