#here is a short Python script that will copy one file to another

#We see a new cmd exists, which checks if the file exists as a string, and returns a boolean
from sys import argv
from os.path import exists

#We unpack argv
script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

#here we open the original file, and then we read it
in_file = open(from_file)
indata = in_file.read()

#we ahve to use %d as it is a variable
print("The input file is %d bytes long" % len(indata))

#We check if the new file already exists
print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CRTL-C to abort.")
input()

#Here we open the to_file, and we write the contents of from_file to it
out_file = open(to_file, "w")
out_file.write(indata)

print("Alright all done.")

#Here we close the files
out_file.close()
in_file.close()
