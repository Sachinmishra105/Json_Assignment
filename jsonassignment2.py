# create a class named "Dog". it should have a constructor which accepts its name,age and coat colour.

class Dog:
    def Breed(self,name,age,colour):
        self.name = name
        self.age = age
        self.colour = colour

    def description(self):
        print(self.name + " is a dog breed and its age is " + self.age)

    def info(self):
        print("coat colour of dog is :",self.colour)
        return ""

class JackRussellTerrier(Dog):
    def country(self):
        print("British breed")
        return ""

class Bulldog(JackRussellTerrier):
    def behavior(self):
        print("Friendly but dignified")
        return ""    

x = Bulldog()
x.name = "Pug"
x.colour = "Brown"
x.age = "5 years"
print(x.name)
print(x.colour)
print(x.age)
print(x.info())
print(x.behavior())
print(x.description())
print(x.country())






