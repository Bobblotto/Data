

class Vehicle():
    def __init__(self, name, year, speed, speedunits):
        self.name = name
        self.year = year
        self.__speed = speed # __ is privatisation
        self.speedunits = speedunits 
    
    def km2m(self):
        if self.speedunits == "km":
            self.speedunits = "m"
            self.__speed *= 1.6
    
    def m2km(self):
        if self.speedunits == "m":
            self.speedunits = "km"
            self.__speed /= 1.6

    def get_speed(self):
        return self.__speed # returns a useable value from the function

    def set_speed(self, newspeed):
        self.__speed = newspeed

class Car(Vehicle):
    def __init__(self, name, year, speed, speedunits, mileage):
        Vehicle.__init__(self, name, year, speed, speedunits)
        self.mileage = mileage

car = Car("Ford Mustang GT", 2024, 155, "m", 25)

print(car.get_speed())
car.set_speed(100)
print(car.get_speed())