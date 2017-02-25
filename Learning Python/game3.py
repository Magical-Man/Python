from sys import exit
from random import randint

# import some stuff to do with exiting the app and randomizing things!

class Scene(object):
    def enter(self):
        print("This scene is not yet configured subclass and implment enter()")
        exit(1)

    # right now all of this is pretty experimental and we are going to try and create combat
class Engine(object):    #the whole engine plass is essentially what is running the game
    def __init__(self, scene_map):
        self.scene_map = scene_map

    # here we are making the initilize function and we are saying taht self.scene_map is equal to the scene_map attribute
    def play(self):       #this is the function that we will execute in order to start the game at the bottom
        current_scene = self.scene_map.opening_scene()  # we say the current_scene att. is equal to the open scene of the map
        last_scene = self.scene_map.next_scene('rescue')   # we identify what the last scene is as where we resuce

        while current_scene != last_scene:   # the loop that repeats to advance scenes
        # says while the current is not the last
            next_scene_name = current_scene.enter()    # the next_scene_name is the enter func of the class
            current_scene = self.scene_map.next_scene(next_scene_name)   # constantly changes the current scene to update it to whatever the scene 'is'

class Death(Scene):
    quips = [
    "You died. You suck at this.",
    "Wow. My puppy can do better than that.",
    "Don't make me create an easy mode!",
    "I really thought someone of your age would be better at this.",
    "And I thought I was bad at videogames!"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) -1)])
        exit(1)

    # the death scene that qeues when you die.

class Open(Scene):
    def enter(self):
        print("If you are ready to play the game type 'yes', if not, type 'no'")
        action = raw_input("> ")

        if action == "yes":
            print("""
You are on the second ever journey to Mars made by man, when suddenly, you look
out of the spaceship window, and you see that part of your ship has been hit by an astroid!
the ship is crashing, and you will need to go and find the emergency video that was given to
you for this situation. You know that it is in this room, but you are going to have to find it.
Hurry!""")

            return 'window'

        elif action == "no":
            print("Alright then, bye!")
            exit(0)

        else:
            print("That is not a valid answer!")
            return 'open'



class Window(Scene):
    def enter(self):
        def fight(type):
            if type == 1:
                print(""""
Suddenly, the computer displays a boxes for a code, and this text,
'Guess the three digit code. The first number is an even number one to four, and the
last digit is the third positive prime number. The middle digit is a positive integer less than five.
After the third attempt, the drive will be wiped.' Type in the number when you are ready""")

                code = "4%d5" % randint(1, 5)
                guess = raw_input("[code]> ")
                guesses = 0

                while guess != code and guesses < 3:
                    print("BZZZDDDDD!")
                    guesses += 1
                    guess = raw_input("[code]> ")

                if guess == code:
                    print("""
You got past the system! The screen blinks on and off for a few seconds, but then
the desktop comes up, you go and you click on the flash drive and see a vdieo file, you
click on it and the file opens.""")

                    return 'video'

                else:
                    print("The drive is wiped, the ship crashes and everyone dies")

                    return 'death'

            elif type == 2:
                print("""
Sudenly, the computer displays the following, 'Solve the following math
problem for x, you will have three chances, after the third attempt, the drive
 will be wiped. / is divide and * is multiply. Here is the problem,
y = 2x - 5 and 4y + 8x = 15
If the answer is a fraction type it with no spaces and use / as the fraction bar.
Type in the number that you want to pick.""")

                math_ans = "35/16"
                math_guess = raw_input("[math]> ")
                guesses = 0

                while math_guess != math_ans and guesses < 3:
                    print("BZZZZDDD")
                    guesses += 1
                    math_guess = raw_input("[math]> ")

                if math_guess == math_ans:
                    print("""
You got past the system! The screen blinks on and off for a few seconds, but then
the desktop comes up, you go and you click on the flash drive and see a vdieo file, you
click on it and the file opens.""")

                    return 'video'

                else:
                    print("The drive is wiped, the ship crashes and everyone dies")

                    return 'death'

            elif type == 3:
                print("""
Suddenly, the computer displays the following, 'Answer the trivia question,
after the third attempt, the drive will be wiped. Here is the question,
What is the name of the scale used to measure the spicy hear of peppers?'
Answer the question with no capital letters and with a single space between each word
if applicable""")

                answer = "scoville scale"
                guess = raw_input("[answer]> ")
                guesses = 0

                while guess != answer and guesses < 3:
                    print("BBBBZZZDD")
                    guesses += 1
                    guess = raw_input("[answer]> ")

                if answer == guess:
                    print("""
You got past the system! The screen blinks on and off for a few seconds, but then
the desktop comes up, you go and you click on the flash drive and see a vdieo file, you
click on it and the file opens.""")

                    return 'video'

                else:
                    print("The drive is wiped, the ship crashes and everyone dies")

                    return 'death'
            else:
                print("ERROR")
                exit(1)

        def choice():
            print("What would you like to do?")
            action = raw_input("> ")

            if action == "look":
                print("""
You look around the room frantically. You see that there is a computer, television,
bed, nightstand, and on the nightstand, a flashdrive.""")

            elif action == "use":
                print("What would you like to use?")
                action = raw_input("> ")

                if action == "flashdrive":
                    print("""
You take the falshdrive off of the nightstand and you go over to the computer
to plug it in. You plug it in, and the computer starts flashing bright red! It looks
as if the computer has been hacked by someone! Your first thought is that it is coming
from Earth, but you will think about it more later. First, you will have to acess the drive.""")

                    return fight(randint(1, 3))

                elif action == "computer":
                    print("You go over to the computer, and play minesweeper for a little while, but then")
                    print("realize you've got to get back to work!")

                    return choice()

                elif action == "television":
                    print("You try to play the Xbox, but the graphics are too bad for your eyes, \#pcmasterrace")

                    return choice()

                else:
                    print("You cannot interact with that item!")

                    return choice()

            elif action == "speak":
                print("You say to yourself, 'I've got to hurry up and watch the video so I make it off the ship!'")
                return choice()

            else:
                print("That is not a valid answer!")

                return choice()


        print("Remember, you need to go as fast as you can, the crew is depending on you!")

        choice()

class Video(Scene):
    def enter(self):  # we may not need any of this becuase the video may not actually do anything after?
        print("What are you going to do?")
        action = raw_input("> ")


        if action == "look":
            pass

        elif action == "use":
            pass

        elif action == "speak":
            pass

        else:
            pass

class Gear(Scene):
    def enter(self):
        print("What are you going to do?")
        action = raw_input("> ")

        if action == "look":
            pass

        elif action == "use":
            pass

        elif action == "speak":
            pass

        else:
            pass

class Team(Scene):
    def enter(self):
        print("What are you going to do?")
        action = raw_input("> ")

        if action == "look":
            pass

        elif action == "use":
            pass

        elif action == "speak":
            pass

        else:
            pass

class Crash(Scene):
    def enter(self):
        print("What are you going to do ?")
        action = raw_input("> ")

        if action == "look":
            pass

        elif action == "use":
            pass

        elif action == "speak":
            pass

class Comm(Scene):
    def enter(self):
        print("What are you going to do?")
        action = raw_input("> ")

        if action == "look":
            pass

        elif action == "use":
            pass

        elif action == "speak":
            pass

        else:
            pass

class Rescue(Scene):
    def enter(self): # remeber to return 'rescue' after the scene
        pass

class Map(object):
    scenes = {
    'death' : Death(),
    'window' : Window(),
    'video' : Video(),
    'gear' : Gear(),
    'team' : Team(),
    'crash' : Crash(),
    'communication' : Comm(),
    'rescue' : Rescue(),
    'open' : Open(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('open')
a_game = Engine(a_map)
a_game.play()
