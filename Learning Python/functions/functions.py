#Functions let you make our own mini-scripts or tiny commands.
#We create functions by using th word def in python

#This function is like argv scripts

#So here we create a function named print_two, and we call *args on it, just
#Like argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1: %r, arg2: %r" %(arg1, arg2))

#Okay, so the *args is actallty pointless there lets just do

def print_two_again(arg1, arg2):
    print("arg1: %r, arg2: %r" %(arg1, arg2))

#Now here is one that just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)

#This one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Charlie", "Odulio")
print_two_again("Charlie", "Odulio")
print_one("First Place!")
print_none()

'''
Some more notes

Always as a colin after the function parenthesis, ;
Always indent
No duplicate arguments in parenthesis
Print, execpt, len, all that is bassiclaly a function
To run, call, or use a function all use the same thing
'''
