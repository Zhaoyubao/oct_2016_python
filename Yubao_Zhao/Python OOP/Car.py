class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = 0.15 if price > 10000 else 0.12
        self.display_all()
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage
        print "Tax:", self.tax

car1 = Car(2000, "35mph", "Full", "55mpg")
car2 = Car(3000, "45mph", "Kind of Full", "25mpg")
car3 = Car(5000, "40mph", "Empty", "35mpg")
car4 = Car(6000, "45mph", "Not Full", "40mpg")
car5 = Car(12000, "55mph", "Full", "20mpg")
car6 = Car(15000, "65mph", "Empty", "60mpg")
