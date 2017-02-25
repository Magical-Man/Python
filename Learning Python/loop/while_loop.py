#A while loop will continue to execute code as long as the code block under it is true

#While loops are generally avioded, as if they never turn false, then they go on forever

#It is essentialy an if statement, that repeats its code every time it remains true

print("What is the increase increment")

def loop(increment):
    i = 0
    numbers = []

    while i < 10:
        print("At the top i is %d" % i)
        numbers.append(i)

        i += increment

        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

        print("The numbers:")
        for num in numbers:
            print(num)

loop(input("> "))
