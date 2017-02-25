#Animal is-a object
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        #self is-a name
        self.name = name

#Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        #self has-a name
        self.name = name

#Person is-a object
class Person(object):

    def __init__(self, name):
        #self has-a name
        self.name = name

        #Peron has-a pet
        self.pet = None

#Employee is-a Person
class Employee(Person):

    def __init__(self, name, slalary):
        #What is this magic?
        super(Employee, self).__init__(name)

        #Self has-a slalary
        self.slalary = slalary

#Fish is-a object
class Fish(object):
    pass

#Salmon is-a Fish
class Salmon(Fish):
    pass

#Halibut is a Fish
class Halibut(Fish):
    pass

#Rover is-a Dog
rover = Dog("Rover")

#Satan is a Cat
satan = Cat("Satan")

#Mary is a Person
mary = Person("Mary")

#mary has-a pet
mary.pet = satan

#Frank is-a Employee
frank = Employee("Frank", 120000)

#Frank has-a pet
frank.pet = rover

#Flipper is a Fish
flipper = Fish()

#Crouse is-a Salmon
crouse = Salmon()

#Harry is-a Halibut
harry = Halibut()

john = Person("John")


#This is a has-many
john.pet = [satan, rover]
