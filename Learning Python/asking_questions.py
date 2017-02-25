print ("How old are you?", )

age = int(raw_input())
print ("How tall are you?", )

height = raw_input()

print ("How much do you weigh?", )

weight = raw_input()

print ('So, youre %r old, %r tall and %r heavy.' % (
    age, height, weight)
    )


#So here we are printing things, and then asking questions, and then , we are using the questions to form a scentance.

print("What is your name?", )

name = raw_input()

print("Do you have siblings; answer yes or no", )

sib = raw_input()

if sib == "yes":
    print("What are their names?", )

    sib_name = raw_input()

    print ("So their names are %s" % (
    sib_name)
    )

elif sib == "Yes":
    print("What are their names?", )

    sib_name = raw_input()

    print ("So their name(s) are/is %s." % (
    sib_name)
    )

else:
    print("That is too bad.")
