from sys import exit
import random

print("What is your name?")

name = raw_input("> ")

def start():
    print("Welcome to the ultimate quest for riches and glory!")

    print("You may move any of eight cardinal directions, which are as follows: \nn \nne \ne \nse \ns \nsw \nw \nnw")

    print("To use these directions, type the letters as are above, and not the full name")

    print("Your goal is to reach the treausre room and to claim the ultimate prize, \nThe Jewl of Babylon")

    print("In order to get here, you will face a variety of differenct rooms and have to navigate your way through the world.")

    print("In each room you will face several encounters, and if you prevail, then you will be able to select a direction and move on.")

    print("In each encounter you will be faced with 2 choices. Just type the number of the choice you want, and press enter to select it.")

    print("So good luck, and best of whishes %s" % name)
    print("PS. Pro-Tip: Draw a map on real paper in the real world")

    print("What direction would you like to go in?")
    def der(direction):

        if direction == "n":
            souls()

        elif direction == "ne":
            cloth()

        elif direction == "e":
            pens()

        elif direction == "se":
            lava()

        elif direction == "s":
            pit()

        elif direction == "sw":
            hands()

        elif direction == "w":
            bugs()

        elif direction == "nw":
            pit()

        else:
            noder()

            print("What direction would you like to go in?")

            der(raw_input("> "))

    der(raw_input("> "))

def start1():
    print("You are back at the start again!")

    print("Which direction do you want to go in?")

    def der(direction):

        if direction == "n":
            souls()

        elif direction == "ne":
            cloth()

        elif direction == "e":
            pens()

        elif direction == "se":
            lava()

        elif direction == "s":
            pit()

        elif direction == "sw":
            hands()

        elif direction == "w":
            bugs()

        elif direction == "nw":
            pit()

        else:
            noder()
            der(raw_input("> "))

    print("What direction would you like to go in?")

    der(raw_input("> "))

def souls():
    def der(direction):

        if direction == "n":
            wall()

            print("What direction would you like to go in?")

            der(raw_input(">"))

        elif direction == "ne":
            nothing()

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "e":
            cloth()

        elif direction == "se":
            pens()

        elif direction == "s":
            start1()

        elif direction == "sw":
            bugs()

        elif direction == "w":
            nothing()

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "nw":
            sound()

        else:
            noder()

            print("What direction would you like to go in?")

            der(raw_input("> "))

    print("You have entered the room of souls")

    print("Before you there is a sad ghost, what do you do?")

    print("1. Try and sneak past the ghost and into the next room")

    print("2. Go and see what is wrong with the ghost, try and help it")

    choice = raw_input("> ")

    if choice == "1":
        print("The ghost attacks, and you realize it was all a trick to test your morales")

        print("You have two options")

        print("1. Run away from the ghost")

        print("2. Kneel down, and submit to death")

        choice = raw_input("> ")

        if choice == "1":
            print("You ran so far away that you ended back at the begining of the maze!")

            start1()

        elif choice == "2":
            die("The ghost killed you for being a bad person!")

    elif choice == "2":
        print("You go over to help the ghost, and it is made well")

        print("The ghost thanks you for helping and says depending on how you answer the next question he will diecide if he likes you")

        print("True or False, is Gandolf a wizard?")

        print("1. True")

        print("2. False")

        choice = raw_input("> ")

        if choice == "1" or "True" or "true":
            print("That is correct go ahead and make your choice")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif choice == "2" or "False" or "false":
            print("SUFFER MY WRATH!!!!!")

            die("You were kille by a ghost for not knowing your Sc-Fi Fantasy")

        else:
            print("That is not a valid answer, restart the room")

            souls()

    else:
        print("That is not a valid answer, restart the room")

        souls()

def cloth():
    def der(direction):
        if direction == "n":
            nothing()

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "ne":
            print("There is nothing there")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "e":
            tar()

        elif direction == "se":
            reading()

        elif direction == "s":
            pens()

        elif direction == "sw":
            start1()

        elif direction == "w":
            souls()

        elif direction == "nw":
            war()

        else:
            noder()

            print("What direction would you like to go in?")

            der(raw_input("> "))


    print("You have entered into the room of cloth, before you stands the great Sewing Machine")

    print("You realize that the machine is running, and that if you continue to stand on the piece of cloth it will impale you! But when you try and move you see your feet are glued down!\nWhat will you do?")

    print("1. Try and unstick your feet in an effort to get loose")

    print("2. You try and talk to the machine to make a diplomatic bargain")

    choice = raw_input("> ")

    if choice == "1":
        chance = [0, 1]

        result = random.choice(chance)

        print("Alright, there is a 50/50 chance that you will escape, litterally, we will see what happens!")

        if result == 1:
            print("You managed to escape! You run away from the sewing machine, and you are free to choose a direction")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif result == 0:
            print("We are very sorry, but you were not able to escape.")

            die(" You were impaled by a sewing machine, pathetic")

        else:
            print("There is an ERROR")

            cloth()

    elif choice == "2":
        print("The machine stops, and tells you to speak your mind")

        print("What do you do?")

        print("1. Make up a sob story about how you are trying to get back to your long lost love, and you will do anything for them")

        print("2. Tell the truth, that you are a greedy treasure hunter looking to make lots of money, and you don't care what you have to do")

        choice == raw_input("> ")

        if choice == "1":
            print("The sewing machine uses the built in lie detector function to tell you are lying!")

            print("The machine decides to kill you for lying")

            die("You lied to a lie detector")

        elif choice == "2":
            print("The machine understands the greed of humans, and decides to let you go on with your quest")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        else:
            print("That is not a valid answer, restart the room")

            cloth()

    else:
        print("That is not a valid answer, restart the romm")

        cloth()

def pens():
    def der(direction):
        if direction == "n":
            cloth()

        elif direction == "ne":
            tar()

        elif direction == "e":
            reading()

        elif direction == "se":
            print("There is nothing there")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif direction == "s":
            lava()

        elif direction == "sw":
            pit()

        elif direction == "w":
            start1()

        elif direction == "nw":
            souls()

        else:
            noder()

            print("What direction would you like to go in?")

            der(raw_input("> "))

    print("Welcome to the room of pens!")

    print("You are walking to the next door")

    print("......................")

    print("And then a pen comes down from the cieling stabbing you under it")

    print("You are bleeding and will die very soon \nWhat will you do?")

    print("1. Remove the pen from your body, and go as fast as you can to the next door")

    print("2. Know that death is coming, and call on the Pen Godess for help")

    choice = raw_input("> ")

    if choice == "1":
        print("As you remove the pen some ink coomes out the tip, and enters your blood stream, giving you blood posining")

        print("What will you do?")

        print("1. Cut your main artery so that you bleed to death quikly")

        print("2. Call on the Pen Godess's son for help")

        choice = raw_input("> ")

        if choice == "1":
            die("You bleed to death painfully")

        elif choice == "2":
            print("The demigod says that his mother probably would have helped, but you blew it, and he will kill you")

            die("You were killed by a todler demigod")

        else:
            print("That is not a valid answer, restart the room")

            pens()

    elif choice == "2":
        print("The Godess answers you and removes the pen very carefully")

        print("You die, but she revieves you, and says she will let you go on, but after a test")

        print("She asks you what is better, Band or Orchestra")

        print("1. Band \n2. Orchestra")

        choice = raw_input("> ")

        if choice == "1":
            print("I agree with you! You may pass")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif choice == "2":
            print("I do not agree with you, but I suppose that everyone is entitled to their own opnions so I will let you pass, but know I hate you now :)")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        else:
            print("That is not a valid answer, restart the room")

            pens()
    else:
        print("That is not a valid answer, restart the room.")

def hands():
    def der(direction):
        if direction == "n":
            bugs()

        elif direction == "ne":
            start1()

        elif direction == "e":
            pit()

        elif direction == "se":
            numbers()

        elif direction == "s":
            lava()

        elif direction == "sw":
            nothing()

            der(raw_input("> "))

        elif direction == "w":
            nothing()

            der(raw_input("> "))

        elif direction == "nw":
            pit()

        else:
            noder()

            der(raw_input("> "))

    print("Welcome to the Hall of Hands")

    print("After you walk in, you feel somethings touching you, and you look over and see thousands of hands on the wals!")

    print("What will you do?")

    print("1. Run through the room as fast as you possibly can to get to the door you see at the end of the hall")

    print("2. Just go back to the start of the maze")

    choice = raw_input("> ")

    if choice == "1":
        print("There is a 3/5 chance that you will survive, lets see what happnens \n**suspense**")

        chance = [1, 2, 3, 4, 5]

        result = random.choice(chance)

        if result > 3:
            print("Bad luck, and you may think this was intentional, but trust me, it was random draw")

            die("Stupidity and bad descision making")

        elif result < 4:
            print("You made it congrats!")

            print("You make it to the end of the hall and are allowed to move on")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        else:
            print("For some reason there was an ERROR")

            hands()

    elif choice == "2":
        print("It may take longer, but trust me, it was for the better..... maybe")

        start1()

    else:
        print("That is not a valid answer, restart the room")

        hands()

def bugs():
    def der(direction):
        if direction == "n":
            pit()

        elif direction == "ne":
            souls()

        elif direction == "e":
            start1()

        elif direction == "se":
            lava()

        elif direction == "s":
            hands()

        elif direction == "sw":
            nothing()

            der(raw_input("> "))

        elif direction == "w":
            lava()

        elif direction == "nw":
            rodent()

        else:
            noder()

            der(raw_input("> "))

    print("You enter the room of bugs!")

    print("In front of you is a caterpiller. \nIt proceeds to telepathically tell you that you should squash it")

    print("What do you do?")

    print("1. Do what he said and squash it \n2. Follow your instinct, and leave it be")

    choice = raw_input("> ")

    if choice == "1":
        print("The caterpiller is very mad at you and then bites your arm! \nWhat do you do?")

        print("1. Run back to the start of the maze to get medical help \n2. Stab yourself in the heart, but after, ask the caterpiller to revive you")

        choice = raw_input("> ")

        if choice == "1":
            print("It may take a while, but that was probably the right choice")

            start1()

        elif choice == "2":
            print("He understands your quest, and he gives you the rest of your life, and lets you do on with the quest")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        else:
            print("That is not a valid answer, restart the room")

            bugs()

    elif choice == "2":
        print("The bug is happy with your kind heart, and justy needs you to swear an oath before letting you move on")

        print("The Oath is: \nI agree never to kill a bug ever again \nWhat do you do?")

        print("1. Agree to take the oath \n2. Disagree")

        choice = raw_input("> ")

        if choice == "1":
            print("The bug says that is unrealistic, and becomes mad at you")

            die("Killed by a bug becuase you are not realistic")

        elif choice == "2":
            print("The bug tells you that your answer is the more realistic one, and lets you pass")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        else:
            print("That is not a valid answer, restart the room")

            bugs()

    else:
        print("That is not a valid answer, restart the room")

        bugs()

def rodent():
    def der(direction):
        if direction == "n":
            nothing()

            der(raw_input("> "))

        elif direction == "ne":
            sound()

        elif direction == "e":
            lava()

        elif direction == "se":
            bugs()

        elif direction == "s":
            lava()

        elif direction == "sw":
            nothing()

            der(raw_input("> "))

        elif direction == "w":
            nothing()

            der(raw_input("> "))

        elif direction == "nw":
            nothing()

            der(raw_input("> "))

        else:
            noder()

            der(raw_input("> "))

    print("Welcome to the room of rodents \nBefore you stands a giant rat")

    print("The rat immediatly attacks you, and manages to lethally bite you, but in your pain, you are not able to run!")

    print("The rat then transforms into a man, holding two syringes, one the cure, and the other instant death, but he does not tell you which is which")

    print("What would you like to do? \n1. Randomly grab a syringe and inject yourself \n2. Attack the man, and hold both syringes to his neck, threatning to inject both if you do not tell him which is which")

    choice = raw_input("> ")

    if choice == "1":
        chance = [0, 1]

        result = random.choice(chance)

        if result == 0:
            print("You are very lucky, you drew the right syringe, and were able to save yourself! \nYou may move on")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        elif result == 1:
            print("Unfortunatley, you chose the wrong syringe, and you failed to save yourself")

            die("You did not choose the right syringe")

        else:
            print("For some reason there was an ERROR")

            rodent()

    elif choice == "2":
        print("The man just lets you inject him with both, as they do not effect him. For he has immunity")

        print("The man then attacks you, plain and simple")

        die("Killed by an alchmeist with immunity, Bravo")

    else:
        print("That is not a valid answer, restart the room")

def sound():
    def der(direction):
        if direction == "n":
            nothing()

            der(raw_input("> "))

        elif direction == "ne":
            nothing()

            der(raw_input("> "))

        elif direction == "e":
            war()

        elif direction == "se":
            souls()

        elif direction == "s":
            pit()

        elif direction == "sw":
            rodent()

        elif direction == "w":
            nothing()

            der(raw_input("> "))

        elif direction == "nw":
            nothing()

            der(raw_input("> "))

        else:
            noder()

            der(raw_input("> "))

    print("Welcome to the hall of sound! \nBeofore you stands a woman known as \"The Audiophile\" She will judge you based on your answer to one question")

    print("She tells you that you have two choices \n1. Answer the question that she will ask \n2. Run away in fear of losing all the progress you have made")

    choice = raw_input("> ")

    if choice == "1":
        print("Alright then, you are very brave answering this")

        print("The question is, which of these two brands is superior? Beats or Sennheiser?")

        print("1. Beats \n2. Sennheiser")

        choice = raw_input("> ")

        if choice == "1":
            print("You are evil. You like an overpriced company with terrible sound. I hate you. ")

            die("Commit suicide due to realizing your stupdity")

        elif choice == "2":
            print("Very good!!!!!!! I was not expecting this answer, you are clearly informed and wise. \nChoose a direction")

            der(raw_input("> "))

        else:
            print("That is not an option, restart the room")

            sound()

    elif choice == "2":
        print("Unlike the previous rooms, I am more harsh, I do not deem you worthy to continue, as to continue, you must be brave")

        die("Killed by the sound woman due to lack of bravery")

    else:
        print("That is not an option, restart the room")

        sound()

def war():
    def der(direction):
        if direction == "n":
            nothing()

            der(raw_input("> "))

        elif direction == "ne":
            nothing()

            der(raw_input("> "))

        elif direction == "e":
            nothing()

            der(raw_input("> "))

        elif direction == "se":
            cloth()

        elif direction == "s":
            wall()

            der(raw_input("> "))

        elif direction == "sw":
            lava()

        elif direction == "w":
            sound()

        elif direction == "nw":
            nothing()

            der(raw_input("> "))

        else:
            noder()

            der(raw_input("> "))

    print("Welcome to the Hall of War! \nIn this place, Ares, the god of war rules, he is all powerfull!")

    print("He comes to you and asks, \"What is your quest?\"")

    print("How will you answer? \n1. To seek the Holy Grail! \n2. To obtain the ultimate treasure!")

    choice = raw_input(">  ")

    if choice == "1":
        print("Good job, two more questions ensue.")

        print("What is the air-speed velocity of an unladen swallow? \nHow will you answer?")

        print("1. What do you mean? An African or European swallow? \n2. 35.536 kmh")

        choice = raw_input("> ")

        if choice == "1":
            print("Right again! Only one more question. \n Who was the first person to attempt to cross the bridge of death?")

            print("1. King Arthur \n2. Sir Launcelot of Camelot")

            choice = raw_input("> ")

            if choice == "2":
                print("Very good! That is correct. You have passed the test of Ares and may now move on")

                print("What direction do you want to go in?")

                der(raw_input("> "))

            elif choice == "1":
                print("Unfortunaley that is incorrect and I, god of war will have to kill you know")

                die("Lack of Monty-Python knowledge")

            else:
                print("That is not a valid answer, restart the room")

                war()

        elif choice == "2":
            print("I'm very sorry, that is incorrect, I will have to kill you know with my war magic")

            die("Lack of Monty-Python knowledge")

        else:
            print("That is not a valid answer, restart the room")

            war()

    elif choice == "2":
        print("That may be the truth, but it is not the answer that we were looking for. Restart the room")

        war()

    else:
        print("That is not a valid answer, restart the room")

        war()

def numbers():
    def der(direction):
        if direction == "n":
            pit()

        elif direction == "ne":
            lava()

        elif direction == "e":
            electric()

        elif direction == "se":
            nothing()

            der(raw_input("> "))

        elif direction == "s":
            nothing()

            der(raw_input("> "))

        elif direction == "sw":
            nothing()

            der(raw_input("> "))

        elif direction == "w":
            lava()

        elif direction == "nw":
            hands()

        else:
            noder()

            der(raw_input("> "))

    print("This is the room of numbers, before you stands a man named Fibonacci he is an all-knowing being")

    print("He will know ask you a very very basic math question, it is simple, there are three questions, to get to the next one must pass the current one")

    print("What does the Fibonacci Sequence have to do with nature? No searching online!!!")

    print("1. Nothing in nature will ever be a number from the sequence \n2. Everything in nature is from the sequence")

    choice = raw_input("> ")

    if choice == "1":
        print("That is incorrect, I'm very sorry to have to do this")

        die("You were overun with integers, and they smothered you")

    elif choice == "2":
        print("Bravo! That is right, on to the next question")

        print("What is scientific notation?")

        print("1. A way of expressing numbers that are normally too lare to deal with \n2. A way of adding and subtracting numbers to make single numbers")

        choice = raw_input("> ")

        if choice == "1":
            print("Right again! Only one more question, and you can move on!")

            print("What is the proper mathematical term for a division bar? No searching online!")

            print("1. Virgule \n2. Vinculum")

            choice = raw_input("> ")

            if choice == "1":
                print("I'm sorry that is incorrect, we will kill you now.")

                die("Millions of failed test force you into depression, you commit suicide")

            elif choice == "2":
                print("Congratulations, you passed the test, finish your journey")

                print("What direction would you like to go in?")

                der(raw_input("> "))

            else:
                print("That is not a valid answer, restart the room")

                numbers()

        elif choice == "2":
            print("That is not the correct answer.")

            die("Mr. Fibonacci kills you with a nine")

        else:
            print("That is not a valid answer, restart the room")

            numbers()

    else:
        print("Tha is not a valid answer, restart the room")

        numbers()

def electric():
    def der(direction):
        if direction == "n":
            lava()

        elif direction == "ne":
            nothing()

            der(raw_input("> "))

        elif direction == "e":
            nothing()

            der(raw_input("> "))

        elif direction == "se":
            nothing()

            der(raw_input("> "))

        elif direction == "s":
            nothing()

            der(raw_input("> "))

        elif direction == "sw":
            nothing()

            der(raw_input("> "))

        elif direction == "w":
            numbers()

        elif direction == "nw":
            pit()

        else:
            noder()

            der(raw_input("> "))

    print("Welcome to the room of Electricity it is by far the most remore room on the map, and quite desolate")

    print("There are thunderbolts coming from the cieling, you have a 4/7 chance of being hit by one, or you can just jump of the cliff next to you and restart")

    print("1. Brave the thunderbolts \n2. Jump the cliff")

    choice = raw_input("> ")

    if choice == "1":
        chance = [1, 2, 3, 4, 5, 6, 7]

        result = random.choice(chance)

        if result < 5:
            print("You were not able to make it across the field")

            die("Struck by lightning")

        elif result > 4:
            print("What a lucky person! Good job making it across, you are now able to move on to your next direction")

            der(raw_input("> "))

        else:
            print("That is not an option, restart the room")

            electric()

    elif choice == "2":
        print("Sometimes, the easy way is the right way after all")

        start1()

    else:
        print("That is not a valid answer, restart the room")

        electric()

def reading():
    def der(direction):
        if direction == "n":
            tar()

        elif direction == "ne":
            treasure()

        elif direction == "e":
            nothing()

            der(raw_input("> "))

        elif direction == "se":
            nothing()

            der(raw_input("> "))

        elif direction == "s":
            nothing()

            der(raw_input("> "))

        elif direction == "sw":
            lava()

        elif direction == "w":
            pens()

        elif direction == "nw":
            cloth()

        else:
            noder()

            der(raw_input("> "))

    print("Welcome to the room of reading before you stands Frodo Baggins, who has some questions to ask you.")

    print("The first question is, where was the man that wrote about me born? No searching online")

    print("1. England \n2. South Africa")

    choice = raw_input("> ")

    if choice == "1":
        print("You are incorrect I will now attack you with Sting")

        die("Killed by a little man with an elf dagger")

    elif choice == "2":
        print("Very good! That is correct")

        print("The next question is, what do you call it when something is made out to be better than it is in literacy")

        print("1. Euphamism \n2. Hyperbole")

        choice = raw_input("> ")

        if choice == "1":
            print("Wonderful job on those questions, you may move on to the door \nWhat direction would you like to go in?")

            der(raw_input("> "))

        elif choice == "2":
            print("I'm very sorry, that is incorrect")

            die("You are possed by Sarumon and forced of the roof of a building")

        else:
            print("That is not a valid answer, restart the room")

            reading()

    else:
        print("That is not a valid answer, restar the rom")

        reading()

def tar():
    def der(direction):
        if direction == "n":
            nothing()

            der(raw_input("> "))

        elif direction == "ne":
            nothing()

            der(raw_input("> "))

        elif direction == "e":
            wall()

            der(raw_input("> "))

        elif direction == "se":
            nothing()

            der(raw_input("> "))

        elif direction == "s":
            reading()

        elif direction == "sw":
            pens()

        elif direction == "w":
            cloth()

        elif direction == "nw":
            nothing()

            der(raw_input("> "))

        else:
            noder()

            der(raw_input("> "))

    print("Welcome to the hall of tar before you stands a monster that is made up of boiling hot tar")

    print("What will you do?")

    print("1. As the monster runs at you bolt past it to get to the door \n2. Call on the Ice god and have him freeze the whole room")

    choice = raw_input("> ")

    if choice == "1":
        print("You manage to get past the moster, but right before the door you trip and fall into a puddle of tar")

        die("Face melted off by tar")

    elif choice == "2":
        print("The Ice god sees how close you are, and comes to help you. He freezes the room, but also freezes you with it, what will you do?")

        print("1. Call on the Fire godess to help \n2. Just wait in the ice")

        choice = raw_input("> ")

        if choice == "1":
            print("The gods are sick of hearing your voice, so they ignore you")

            die("You get frostbite and hypothermia")

        elif choice == "2":
            print("The Ice god sees your agony, and comes to fix it for you. He melts the ice around you \nYou go to the door")

            print("What direction would you like to go in?")

            der(raw_input("> "))

        else:
            print("That is not a valid answer, restart the room")

            tar()

    else:
        print("That is not a valid answer, restart the room")

        tar()

def treasure():
    print("Congratulations! You have reached the clock room. This is the most challenging room of all, and you are the first to ever attempt it")

    print("A man looking like a clock comes to you and tells you the first question.")

    print("What was the name of the Archduke of Austria-Hungary that was assasinated to start WW1? No internet ")

    print("This time type in the name, single spaced with caps at the begining of each word.")

    choice = raw_input("> ")

    if choice == "Franz Ferdinand":
        print("Amazing! That is the correct answer, I didn't think that you would be able to get it.")

        print("The next question is: \nWhich European country first allowed women to vote?")

        print("Type in the name of the country, with a capital letter at the begining and nothing else, no internet")

        choice = raw_input("> ")

        if choice == "Finland":
            print("Right again, only two more questions!")

            print("Next, \nWhat band did the man that the Sousaphone is named after conduct, type it with single spaces, and no caps, no internet")

            choice = raw_input("> ")

            if choice == "united states marine band" or "us marine band":
                print("Only one more question, and then you can move on!")

                print("What is the programming language Python named after?")

                print("type with capital letters at the begining of each word and single spaced, no internet")

                choice = raw_input("> ")

                if choice == "Monty Python":
                    print("You have done it, you are the first to complete the room of clocks, and I will now reaveal to you the secret")

                    print("The secret is that this is actually the treasure room, and you have claimed the prize, The Jewl of Babylon.")

                    print("%s, your name will go down in history as the name of the person that found the Jewl and passed the tresure room." % name)

                    print("Thank you for playing. I hope you enjoy your victory, farewell!")

                    exit(0)

                else:
                    print("That is either not the correct answer, or the answer is invalid, restart the game")

                    start1()

            else:
                print("That is either not the correct answer, or the answer is invalid, restart the game")

                start1()

        else:
            print("That is either not the correct answer, or the answer is invalid, restart the game")

            start1()

    elif 8200 < choice < 8300:
        print("That is not the correct, but it is very close, so I will not send you to the start, rather back a few rooms.")

        tar()

    else:
        print("That is either not the correct answer, or the answer is invalid, restart the game")

        start1()

def die(why):
    print("You died becuase %s" % why)

    def leave():
        print("Which of the following would you like to do?")

        print("1. Exit the game")

        print("2. Restart the game")

        choice = raw_input("> ")

        if choice == "2":
            start()

        elif choice == "1":
            exit(0)

        else:
            print("That is not a valid answer")

            leave()

    leave()

def lava():
    print("You tripped and fell.")

    die("You fell into lava!")

def wall():
    print("You can not pass because there is a wall, go another way.")

    print("What direction do you want to go?")

def pit():
    print("You slip on a napkin and fall")

    die("When you fell you landed in a botomless pit, where you starve")

def nothing():
    print("There is nothing there, please pick another direction")

def noder():
    print("That is not a direction, try again, remember use lowercase letters without a space, for example, ne")

    print("Which way do you want to go?")

start()
