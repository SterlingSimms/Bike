class Bike(object):
    def __init__(self, price, max_speed, miles):
        self.miles = 0
        self.price = price
        self.max_speed = max_speed
    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self
    def ride(self):
        self.miles += 10
        print "Riding"
        return self
    def reverse(self):
        print "reversing"
        while self.miles > 0:
            self.miles -= 5
        return self


bike1 = Bike(50, 100, 0)
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(20, 20, 0)
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(200, 100, 0)
bike3.reverse().reverse().reverse().displayInfo()



