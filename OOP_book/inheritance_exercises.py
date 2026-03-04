# Exercise 1
# A Car and an Engine has a has-a relationship
# A Teacher and a Student has neither relationship
# wrong, while a teacher isn't a student or vice versa, they often have a relationship where they have one another, for example, in a school

# A Flag and a Color has a has-a relationship
# An Apple and an Orange has neither relationship
# A Ship and a Vessel has a is-a relationship
# A Home and a Structure has a is-a relationship
# A Circle and a Shape has a has-a relationship
# wrong, a circle doesn't have a shape, a circle is a shape. 

# Exercise 2
# attempt 1
class Vehicle:
    COUNT = 0
    
    def vehicles():
        return Vehicle.COUNT
    
class Car(Vehicle):
    def __init__(self):
        Vehicle.COUNT += 1
        
class Truck(Vehicle):
    def __init__(self):
        Vehicle.COUNT += 1
        
class Boat(Vehicle):
    def __init__(self):
        Vehicle.COUNT += 1
        
print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8

# better solution
class Vehicle:
    COUNT = 0
    
    def __init__(self):
        Vehicle.COUNT += 1
    
    @classmethod
    def vehicles(cls):
        return Vehicle.COUNT
    
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        
class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        
class Boat(Vehicle):
    def __init__(self):
        super().__init__()
        
print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8

# exercise 3
class MoveMixin:
    def signal_left(self):
        print('Signalling left')
    def signal_right(self):
        print('Signalling right')
    def signal_off(self):
        print('Signal is now off')
        
class Vehicle:
    COUNT = 0
    
    def __init__(self):
        Vehicle.COUNT += 1
    
    @classmethod
    def vehicles(cls):
        return Vehicle.COUNT
    
class Car(MoveMixin, Vehicle):
    def __init__(self):
        super().__init__()
    
class Truck(MoveMixin, Vehicle):
    def __init__(self):
        super().__init__()
        
class Boat(Vehicle):
    def __init__(self):
        super().__init__()



print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8
car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'

# exercise 4
class MoveMixin:
    def signal_left(self):
        print('Signalling left')
    def signal_right(self):
        print('Signalling right')
    def signal_off(self):
        print('Signal is now off')
        
class Vehicle:
    COUNT = 0
    
    def __init__(self):
        Vehicle.COUNT += 1
    
    @classmethod
    def vehicles(cls):
        return Vehicle.COUNT
    
class Car(MoveMixin, Vehicle):
    def __init__(self):
        super().__init__()
    
class Truck(MoveMixin, Vehicle):
    def __init__(self):
        super().__init__()
        
class Boat(Vehicle):
    def __init__(self):
        super().__init__()
        
print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicle.mro())

# exercise 5
class Vehicle:
    
    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg
    
    def max_range_in_miles(self):
        return self.capacity * self.mpg

class Car(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car