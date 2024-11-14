

class Car():
    def __init__(self, name, year, mileage, mileageunits):
        self.name = name
        self.year = year
        self.mileage = mileage
        self.mileageunits = mileageunits 
    
    def km2m(self):
        if self.mileageunits == "km/l":
            self.mileageunits = "m/l"
            self.mileage *= 1.6
    
    def m2km(self):
        if self.mileageunits == "m/l":
            self.mileageunits = "km/l"
            self.mileage /= 1.6

car = Car("Ford Mustang GT", 2024, 25, "m/l")

print(car.name)
print(car.year)
print(car.mileage, car.mileageunits)

car.m2km()

print(car.mileage, car.mileageunits)