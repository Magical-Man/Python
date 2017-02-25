from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print("This is what happens!")
        exit(1)

class Thing(Scene):
    def enter(self):
        print("Here are things")

        def fight(type):
            if type == 1:
                print("1")

            elif type == 2:
                print("2")

            elif type == 3:
                print("3")

            else:
                print("x")

        fight(randint(0, 2))



x = Thing()

x.enter()
