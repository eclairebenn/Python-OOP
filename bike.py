# pylint: disable=print-statement
class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        if self.miles < 0:
            self.miles = 0
        print "Bike price: {} dollars. Bike Max Speed : {}. Bike total miles : {} miles.".format(self.price, self.max_speed, self.miles)
        #return self (dont need this but maybe should have?)

    def ride(self):
        print "Riding . . ."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing . . ."
        self.miles -= 5
        return self

bike1 = Bike(600, "25mph")
bike2 = Bike(400, "10mph")
bike3 = Bike(1300, "50mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()
