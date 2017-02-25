from sys import exit

#So we import the exit() command from the system
def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = raw_input("> ")

    if choice.isdigit() == True:
        how_much = int(choice)
        #SO here we are saying if the number contains a 1 or 0, then make the var how_much and move on
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")

#Here we make the gold_room() funciton, and we say how it will run

def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True

#So with this one, we make it so that if you taunt twice you die, because in the above we make bear_moved true.

        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

def cthulhu_room():
    print("Here you see the great evil Cthlhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "Good Job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
#Then here, we declare what the begining of the program is.

start()

#Here we first call the program