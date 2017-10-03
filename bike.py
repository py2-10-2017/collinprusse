class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "The price is $" + str(self.price)
        print "The max speed is " + str(self.max_speed) + " M.P.H."
        print "Total miles: " + str(self.miles)
        return self

    def ride(self):
        print "Riding"
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing"
        if self.miles >= 5:
            self.miles -= 5
        return self


#First instance
bike1 = Bike(105.75, 15)
bike1.ride().ride().ride().reverse().displayInfo()


#Second instance

bike2 = Bike(499.99, 50)
bike2.ride().ride().reverse().reverse().displayInfo()


#Third instance
bike3 = Bike(199.99, 25)
bike3.reverse().reverse().reverse().displayInfo()
