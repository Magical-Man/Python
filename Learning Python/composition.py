class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit():
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER, altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER, altered()")

son = Child()
son.implicit()
son.override()
son.altered()

# We don't use the name Parent() cause it's not is-a it is has-a where child has-a other
