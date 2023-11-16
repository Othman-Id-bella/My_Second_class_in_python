class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color


    def brake(self):
        print("the car name",self.make," his color ",self.color," his model",self.model,"display of the year",self.year)

car1 = Car("Toyota", "Camry", 2022, "Blue")
car2 = Car("Honda", "Accord", 2023, "Red")

car1.brake()
car2.brake()

