# pylint: disable=print-statement
class Car(object):   
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        
        self.display_all()
     
    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Tax: {}".format(self.tax)
        return self

#6 Random Instances
car1 = Car(1000, "35mph", "Full", "15mpg")
car2 = Car(2000, "50mph", "Not Full", "105mpg")
car3 = Car(10293, "23mph", "Half Full", "30mpg")
car4 = Car(7093, "70mph", "Quarter Full", "90mpg")
car5 = Car(20093, "100mph", "Three Quarters Full", "12mpg")
car6 = Car(6093, "50mph", "Full", "50mpg")
