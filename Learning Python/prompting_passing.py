from sys import argv

script, user_name = argv
prompt = "> "

print("Hi %s, I'm the %s script." % (user_name, script))

print("I'd like to ask you a few questions.")

print("Do you like me %s" % user_name)
like = input(prompt)

print("Where do you live %s" % user_name)
live = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said %r about liking me, you live in %r, (not sure where that
is), and you have a(n) %r computer, nice!
""" % (like, live, computer))

#So what we aer doing here is we are gving the user a seires of prompts, and
#Then we are collecting them into print statements.
#The prompt is jsut a variable and is not a functions.
