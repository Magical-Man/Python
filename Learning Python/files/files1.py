#.close to close the file
#read to read the contents
#readline to read one line
#truncate to emptie the fule
#write("Stuff") to add to the file

#Now we will make a basic text editor.

#Here we import argv
from sys import argv
script, filename = argv

#Now we print some lines askign the user
print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

#Here we ask them what they want to do.
raw_raw_input("?")

#Now we tell them we are oppening, and then we open the file, but we specify
#To be in write mode with w
print("Opening the file...")
target = open(filename, "w")

#Then we erase the current contents of the file
print("Truncating the file. Goodbye!")
target.truncate()

#Now we ask the user for some information
print("Now I'm going to ask you for three lines.")

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print("I'm going to write these to the file.")

#And then down here, we write all of the users info to the file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#Then here, we close the file
print("And finally, we close it.")
target.close()
