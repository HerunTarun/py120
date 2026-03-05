# exercise 1
class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994

car1 = Car(2006)
print(car1.year)              # 2006
# exercise 2
class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year):
        super().__init__(year)
        self.start_engine()
        
    def start_engine(self):
        print('Ready to go!')

# Comments show expected output
truck1 = Truck(1994)          # Ready to go!
print(truck1.year)            # 1994

# exercise 3
class Vehicle:
    def __init__(self, year):
        self._year = year
        

    @property
    def year(self):
        return self._year

class Truck(Vehicle):
    def __init__(self, year, bed_type):
        super().__init__(year)
        self._bed_type = bed_type
    
    @property
    def bed_type(self):
        return self._bed_type

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994, 'Short')
print(truck1.year)            # 1994
print(truck1.bed_type)        # Short

car1 = Car(2006)
print(car1.year)              # 2006
print(car1.bed_type)
# AttributeError: 'Car' object has no attribute 'bed_type'

# exercise 4
class Vehicle:
    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def start_engine(self, speed):
        return f'{super().start_engine()} Drive {speed}, please!'

# Comments show expected output
truck1 = Truck()
print(truck1.start_engine('fast'))
# Ready to go! Drive fast, please!

truck2 = Truck()
print(truck1.start_engine('slow'))
# Ready to go! Drive slow, please!

# exercise 5
class WalkingMixin:
    def walk(self):
        print("Let's go for a walk")

class Cat(WalkingMixin):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

# Comments show expected output
kitty = Cat('Sophie')
kitty.greet()       # Hello! My name is Sophie!
kitty.walk()        # Let's go for a walk!

# exercise 6
class TowingMixin():
    def tow(self):
        print('I can tow a trailer!')

class Truck(TowingMixin):
    pass

class Car:
    pass

# Comments show expected output
truck1 = Truck()
truck1.tow()        # I can tow a trailer!

car1 = Car()
car1.tow()
# AttributeError: 'Car' object has no attribute 'tow'

# exercise 7
class TowingMixin:
    def tow(self):
        return 'I can tow a trailer!'

class Vehicle:
    def __init__(self, year):
        self._year = year
    
    @property
    def year(self):
        return self._year

class Truck(TowingMixin, Vehicle):
    pass

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994)
print(truck1.year)            # 1994
print(truck1.tow())           # I can tow a trailer!

car1 = Car(2006)
print(car1.year)              # 2006


# exercise 8
class Animal:
    def __init__(self, color):
        self._color = color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.get_color())

# MRO - Cat -> Animal -> Object
# While Animal has color as a instance variable, there is no getter for it, so MRO will search the object superclass

# exercise 9
class Animal:
    pass

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat()
cat1.color

# MRO - Cat -> Animal -> object
# exercise 10

class FlyingMixin:
    def fly(self):
        return "I'm flying!"

class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(FlyingMixin, Animal):
    pass

bird1 = Bird('Red')
print(bird1.color)

# MRO - Bird -> FlyingMixin -> Animal
# MRO will stop at Animal because it will find the getter color(self) in the Animal class and return "Red"