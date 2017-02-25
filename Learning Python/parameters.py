from sys import argv

script, first, second, third  = argv

print("The first script is called: ", script)
print("Your first Variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

#On line one we have an import, which is adding modules to your script from Python feature set
#argv is arugment value, and it holds all of the arguments that we pass to Python
#In line 3 we are unpacking argv so that, rather than holding all the arguments, it expands to fiour different files
#This sounds like unzipping a files
#Then we are just printing all of the variables
