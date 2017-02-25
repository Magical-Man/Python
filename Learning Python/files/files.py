#Working with files is an easy way to ERASE your work if you are not careful.

#This file will be working iwth reading_sample.txt
#we want to open this file, but we do not want to hard code it in
#Hard coding is when we just put something in as a string, we want the user to pick

#here we import argv
from sys import argv

scipt, filename = argv

#here we set the variable txt to open the filename
txt = open(filename)

#here we say print the name of the file, and the var txt, but read the contents of txt
print("Here's your file %r: " % filename)
print(txt.read())

#Here we repeat the process, but rather than using argv, we use input
print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print txt_again.read()

#here we close the files, which is always important
txt.close
txt_again.close
