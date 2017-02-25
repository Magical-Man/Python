people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")

elif cars < people:
    print("We should not take the cars.")

else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")

elif trucks < cars:
    print("Maybe we could take the trucks.")

else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")

else:
    print("Find, let's stay home then.")

'''
I think that else and elif are more blocks of code to execute
if something is true or not.
If multiple elifs are true, python will run them from the top
'''
