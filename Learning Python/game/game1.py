print("**** Answer all questions with a number, and just a number. Also only use numbers listed before the quetions. ****")

print("You enter a dark room with 5 doors, each one has a powerful rune on it."
" Which one do you decide to go through, 1, 2, 3, 4, or 5")

door = raw_input("> ")

if door == "1":
    print("There's a giant bear here eatinga a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = raw_input("> ")

    if bear == "1":
        print("The bear eats your face off. Good Job!")
    elif bear == "2":
        print("The bear ears your legs off. Good Job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss at Cithulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good Job!")

    else:
        print("The insanity rots your eyes into a pool of muck. Good Job!")

elif door == "3":
    print("Here you see the powerful wizard ZAC.")
    print("1. Say \'Hello there Zac, how are ya?\'")
    print("2. Stay silent and wait for the all powerful to speak.")
    print("3. Brutally run at the ZAC and attack it with only your hands")

    attack = raw_input("> ")

    if attack == "1":
        print("ZAC says, \'I am not just Zac, I am the all powerful Wizard ZAC, bow!!\'")
        print("1. Bow")
        print("2. Stay standing")

        bow = raw_input("> ")

        if bow == "1":
            print("Thank you. The all powerful ZAC grants you immortality, you live forever with your cat.")
        elif bow == "2":
            print("The all powerful ZAC melts you with lasers from his eyes.")
        else:
            print("\'Too indpendant, you will be obliterated.\' ZAC smashes you with his fist.")

    elif attack == "2":
        print("Thank you for patienly waiting, I have decided to let you go, but if you don't go to school I will kill you.")

    elif attack == "3":
        print("\'OBEY OBEY OBEY OBEY OBEY OBEY\'")
        print("1. Rethink your decision and bow to ZAC")
        print("2. Remain standing in indpendance")

        obey = raw_input("> ")

        if obey == "1":
            print("\'You are lucky to be given another change, you may go and be free.\'")
        elif obey == "2":
            print("\'You were warned.\' ZAC kills you with his fire breath.")
        else:
            print("\'That is not the answer that I was looking for. Death.\' ZAC kills you with magic power.")

    else:
        print("\'That was not one of your options, you will now be destroyed\' ZAC kills you with magical vinegar")

elif door == "4":
    print("You see the almighty Gattis towering above you, he is in a happy mood, and reminds you to practice every day.")
    print("1. Do not practice, play out of tune, and refuse to be good")
    print("2. Practic, play well, be nice, and don't mess up")

    practice = raw_input("> ")

    if practice == "1":
        print("\'You have a playing test now, 0 or 100.\'")
        print("1. Prepare for the playing test")
        print("2. Do not perpare for the palying test")
        test = raw_input("> ")

        if test == "1":
            print("Bravo, you got a 100 and you became a millionare, congrats!")
        elif test == "2":
            print("SUFFER THE WRATH OF GATTIS: You are crippled by the punisher, everyone you know gets the Black Death, you are the last human alive.")
        else:
            print("That is unacceptable. You suddenly have a heart attack and die.")

    elif practice == "2":
        print("You go on to start the next Apple Inc. you become a billionare celebrity")

    else:
        print("Whatever that was it was no good. Die.")

elif door == "5":
    print("You enter a dark room, full of mirrors.")
    print("Suddenly, a ghost appears, what do you do?")
    print("1. Attack the ghost")
    print("2. Walk into the ghost")

    ghost = raw_input("> ")

    if ghost == "1":
        print("You go through the ghost, and in rage it attacks and kills you.")

    elif ghost == "2":
        print("The ghost does, nothing, you escape and just go home.")

    else:
        print("That is a bad answer, you go to prison for the rest of your life")

else:
    print("You stumble around and fall on a knife and die. Good Job!")

print("Thank you for playing this short Python based game.")

##A key thing we are doing is putting if inside of if
