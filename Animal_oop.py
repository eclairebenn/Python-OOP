# pylint: disable=print-statement
class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def walk(self):
        self.health -= 1
        return self
    
    def run(self):
        self.health -= 5
        return self
    
    def display_health(self):
        print "Current health of {} is: {}".format(self.name, self.health)
        return self

animal1 = Animal('turkey', 300)
#animal1.walk().walk().walk().run().run().display_health() #Testing animal object

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name, 150)
        #self.health = 150 
    def pet(self):
        self.health += 5
        return self
    
dog1 = Dog('doggy')
dog1.walk().run().pet().display_health() #Testing dog object

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name, 170)
        #self.health = 170

    def fly(self):
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon!"
        return self

drag1 = Dragon('draggy')
drag1.fly().walk().run().display_health() #Testing Dragon Object

animal2 = Animal('piggy', 400)
animal2.walk().run().display_health()
