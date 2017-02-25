class Parent(object): # Here we just define a class...

    # We delcare a bunch of functions that print() stuff
    def override(self):
        print("PARENT overrid()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent): # Here we are defining another class under the influence of Parent()

    def override(self): # We define a function we already have in the parent and it becomes overriden
        print("CHILD override()")

    # We don't call an implicit() one becuase the Child naturally inherits it

    def altered(self): # We override a function
        print("CHILD, BEFORE PARENT, altered()") # Print something
        super(Child, self).altered() # Print the original Parent() version of the function
        print("CHILD, AFTER PARENT, altered()") # Print another thing after

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
