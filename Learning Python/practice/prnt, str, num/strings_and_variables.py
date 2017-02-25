#variables are just like variables in math, and they can be changed as well

#DON"T EVER START A VARIABLE WITH A NUMBER, also some words that already act as functions won't work!'"

my_variable = "this is a string"

my_second_variable = "this is some more stuff"

my_combined_variable = my_variable + " " + my_second_variable

print(my_combined_variable)

#or you can do it like this cand you can make a dilimeter, this makes it so you can have a string on multiple lines. No foregin things, just do US things.

my_html = '''
    <html>
        <head>
            <title>Look at me!</title>
        </head>
        <body>
            <h1> Hello World!</h1>
        </body>
    </html>
'''
#concantonation is adding together two strings

#here is another method of doing this

animal = "cat"

print("%s ran over the hill" % animal)

# the %s is a placeholder, and the % is saying what to fill in, kind of like cariables.
# the %r is used in debugginhg as it is more raw, and use the others for displaying to users
#In python a line longer than 80 characters is bad style
