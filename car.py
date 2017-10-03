class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 15
        else:
            self.tax = 12
        self.displayAll()


    def displayAll(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed)
        print "Fuel: " + self.fuel
        print "Mileage: " + str(self.mileage)

        print "Tax: " + str(self.tax) + "%"


#1
car1 = car(20000, 60, 'Full', 2500)

#2
car2 = car(50000, 90, 'Not Full', 500)
#3
car3 = car(9800, 55, 'Not Full', 60000)
#4
car4 = car(5000, 60, 'Full', 5500)
#5
car3 = car(98000, 105, ' Full', 6000)
#6
car3 = car(1000, 45, 'Not Full', 80000)
