class product(object):
    def __init__(self, price, item_name, weight, brand, cost, status):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"


    def displayInfo(self):
        print "Price: $" + str(self.price)
        print "Item Name: " + self.item_name
        print "Weight: " + str(self.weight) + "lbs"
        print "Brand: " + self.brand
        print "Cost: $" + str(self.cost)
        print "Status: " + self.status
        return self


    def sell(self):
        self.status = "sold"
        return self


    def addTax(self, tax):
        self.price += tax
        return self


    def makeReturn(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "return in box":
            self.status = "for sale"
        elif reason == "opened":
            self.status = "used"
            self.price = self.price - (self.price * .2)
        return self


item1 = product(10, "bat", 2, "Louisville", 5, "new")
item1.makeReturn("return in box").displayInfo()
