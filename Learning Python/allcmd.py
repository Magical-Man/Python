assert 2 + 2 == 4, "Huston, we have a probelm"

#If the above was == 5, there would be an error.

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break

    else:
        #loop fell through without finding a factor
        print(n, 'is a prime number')

#Basically what break does is loop us back to the top of a loop.

#Here is an example of classes

class Dog:

    tricks = []

    def __init__ (self, name):
        self.name = name

    def add_tricks(self, trick):
        self.tricks.append(trick)

'''This is a class, it says that the variable in the class, or the object, is this list. By using __init__ it is
a bit like argv and lets you add arguments to your functions. Then by using the .\'s we are able to call the functions.
'''

#The thing that the continue statement does is just says to go back to the start of the loop and keep looping.

##Also remember that you have a quizlet to STUDY!!!!
