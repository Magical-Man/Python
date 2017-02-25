#By using = and the return command, we can set variables to be a value form of
#A function

def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(10, 3)
height = subtract(100, 33)
weight = multiply(55, 2)
iq = divide(1000, 5)

print("Age: %d \n Height: %d \n Weight: %d \n IQ: %d"
% (age, height, weight, iq))

#A puzzle for extra credit!
print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: " + str(what) + " iCan you do it by hand?")
