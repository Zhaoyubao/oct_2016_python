class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        print "Bike's Price:", self.price
        print "Bike's Maximum Speed:", self.max_speed
        if self.miles < 0:
            self.miles = -self.miles
        print "Bike's Total Miles: %d miles"%self.miles
    def ride(self):
        print "Riding..."
        self.miles += 10
    def reverse(self):
        print "Reversing..."
        self.miles -= 5

bike1 = Bike(200, "25mph")
bike2 = Bike(300, "30mph")
bike3 = Bike(400, "35mph")
for i in range(3):
    bike1.ride()
    bike3.reverse()
bike1.reverse()
for i in range(2):
    bike2.ride()
    bike2.reverse()
bike1.displayinfo()
bike2.displayinfo()
bike3.displayinfo()
