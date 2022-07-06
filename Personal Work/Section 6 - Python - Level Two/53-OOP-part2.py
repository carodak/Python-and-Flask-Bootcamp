class Circle():

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * self.pi

    def circumference(self):
        return 2 * self.pi * self.radius

my_circle = Circle(10)
print(my_circle.radius)
print(my_circle.area())
print(my_circle.circumference())

class Animal():
    def __init__(self, fur):
        print('Animal Created!')
        self.fur = fur

    def report(self):
        print('Animal')

    def eat(self):
        print('Eating')

class Dog(Animal):
    def __init__(self, fur):
        Animal.__init__(self, fur) #Upon creating an instance of Dog, create an instance of the Animal class
        print('Dog Created!')
    def report(self):
        print('I am a dog')

#a = Animal()
#a.eat()
#a.report()
d = Dog('Fuzzy White')
d.eat()
d.report()
print(d.fur)
