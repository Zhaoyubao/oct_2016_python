from Animal import Animal

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        print "Petting..."
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        print "Flying..."
        self.health -= 10
        return self
    def displayHealth(self):
        print "This is a dragon!"
        super(Dragon, self).displayHealth()
dog = Dog("Puppy")
dog.walk().walk().walk().run().run().pet().displayHealth()

dragon = Dragon("dragon")
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
