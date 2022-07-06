#almost everything is an object in python
#defined inside a class
#mylist = [1,2,3]
#mylist.append(4)
#print(type(mylist))
#print(type(12))
#print(type(23.5))

class Sample():
    pass

x = Sample()
print(type(x))

class Dog():

    # CLASS OBJECT ATTRIBUTES
    # Shared amoung all instances
    species = 'mammal'

    def __init__(self, breed, name): #self refers to the instance
        self.breed = breed
        self.name = name

x = Dog('Huskie', 'Sam')
new_dog = Dog('Golden', 'Cindy')

print(x.breed)
print(x.name)
print(x.species)
print(new_dog.species)
