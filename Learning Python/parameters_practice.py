from sys import argv

script, first, second, third = argv

name = input("Hello there! What is your name?")

age = int(input("How old are you?"))

print("So you told me, ", first)

print("You told me, ", second)

print("And you told me, ", third)

print("So you're name is %s, and you are %s years old" % (name, age))
