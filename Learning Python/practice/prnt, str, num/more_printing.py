formatter = "%r %r %r %r"

#Here we aer saying that print the variable formatter, and use 1234 to sub for %r
print (formatter % (1, 2, 3, 4))


print (formatter  % ("one", "two", "three", "four"))

print (formatter % (True, False, False, True))

print (formatter % (formatter, formatter, formatter, formatter))

#Here we are saying to print the var formatter and to use the four strings as subs for %r
print (formatter % (
    "I had this thing.",
    "That ou couyld type up right.",
    "But it didn't sing.",
    "SO I said goodnight."
    )
)




#Here we declare two variabels
days = "Mon Tue Wed The Fri Sat Sun"


#The \n is saying to print that thing on a new line, they are called newlines
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

#Here we are printing "Here are the days", and then we are displaying the variable days
print ("Here are the days: "), days

#Same as above buty with months
print ("Here are the months: "), months


#By using the triple " we are able to make a multi-line string
print"""
There's something going on here.
With the gree double quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

#By using a \ (backslash) you can escape quotes, so that if you had "Hello "I understand " Joe"
#It will not be confused by the middle quites , so you would do "Hello \" I understand\" Joe"

'''
what
is
the
meaning
of
this'''
