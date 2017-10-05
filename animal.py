class animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def displayHealth(self):
        print "Name: " + self.name + " Health: " + str(self.health)
        return self

# #animal instance
# ani1 = animal("Chupacabra", 50)
# ani1.walk().walk().walk().run().run().displayHealth()

class Dog(animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        self.health += 5
        return self

dog1 = Dog("Toby")
dog1.walk().walk().walk().run().run().pet().displayHealth()


class Dragon(animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def displayHealth(self):
        print "This is a dragon"
        super(Dragon, self).displayHealth()

dragon = Dragon('Deathwing')
dragon.fly().displayHealth()
