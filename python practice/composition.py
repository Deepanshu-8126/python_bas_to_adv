#Composition -- one class can use object of another class
# agar has a relationship agar engine nahi hey tho car ka kuch nahi chalegi has a realtionship
# Engine class
"""class Engine:
    def start(self):
        print("Engine started")


# Car class
class Car:
    def __init__(self):
        self.engine = Engine()  # Engine object created

    def drive(self):
        print("Car is ready to drive")
        self.engine.start()


# Usage
print("=== Creating Car object ===")
car = Car()
print("\n=== Calling drive method ===")
car.drive()"""

"""class Battery:
    def __init__(self,capacity):
        self.capacity=capacity
    def show_capacity(self):
        print(f"Battery capacity is : {self.capacity}")
class Mobile:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
        self.battery=Battery(5000) #battery ka object use kiya
    def mobile_info(self):
        print(f"Mobile{self.brand},{self.model}")
        self.battery.capacity() # battery object call
mobile=Mobile("Samsung","Realme")
mobile.mobile_info()"""

"""class Engine:
    def __init__(self,horsepower,engine_type):
        self.horsepower=horsepower
        self.engine_type=engine_type
class Car:
    def __init__(self,brand,engine):
        self.brand=brand
        self.engine=Engine()
    def car_info(self):
        print(f"Brand name :{self.brand} and egine :{self.engine}")
c1 = Car("Bmw","gsx")
c2=Car("toyota","fede")
c1.car_info()
"""

