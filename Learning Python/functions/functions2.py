#Here we will see how many ways we can pass an arg

def some_numbers(number1, number2, number3):
    print("So the first number you picked was %d." % int(number1))
    print("So the second number you picked was %d." % int(number2))
    print("So the third number you picked was %d." % int(number3))
    total = number1 + number2 + number3
    print("So in total your numbers added up to %d" % total)

print("Way1")

some_numbers(1, 2, 3)

print("Way2")

num1 = 1
num2 = 3
num3 = 3
some_numbers(num1, num2, num3)

print("Way3")

some_numbers(1 + 0, 1 + 1, 1 + 2)

print("Way4")

some_numbers(num1 + 0, num2 + 1, num3 + 1)

print("Way5")

num1 = int(input("What is num 1"))
num2 = int(input("What is num 2"))
num3 = int(input("What is num 3"))

some_numbers(num1, num2, num3)

print("Way 6")

print("What is num1")

num1 = int(input("> "))

print("What is num2")

num2 = int(input("> "))

print("What is num3")

num3 = int(input("> "))

some_numbers(num1, num2, num3)


print("Way 7")

num1 = 1
num2 = 2
num3 = int(input("What is num3"))

some_numbers(num1, num2, num3)
