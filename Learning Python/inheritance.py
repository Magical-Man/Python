# There are different three different kinds of inheritance

# The first type is where actions on the child imply an action on the parent

# The next is where actions on the child override the action on the parent

# The third is where actions on the child alter the action of the parent

#This first type is implicit inheritace where you defing a function in the paretn but not in the child

class Parent(object):
    def pr(self, name):
        print(name)

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.pr("a")
son.pr("s")

# The next type is very similar and we jsut redefine the funciton in the child class
# Which effectivly overrides whatever is made in parent class

# The next type is alter before or after so when you overide before or after the parent class runs
# You use some super() wizardry

class Parent1(object):

    def altered(self):
        print("PARENT altered()")

class Child1(Parent1):

    def altered(self):
        print("CHILD, BEOFRE PARENT altered()")
        super (Child1, self).altered()
        print("CHILD AFTER altered()")

dd = Parent1()
sn = Child1()

dd.altered()
sn.altered()
