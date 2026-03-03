# exercise 1
class Car:
    ACCELERATION = 5
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError('model must be a string')

        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError('year must be an integer')

        if year < 0:
            raise ValueError('year must be above zero')

        self._year = year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('color must be a string')

        self._color = color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed < 0:
            raise ValueError('speed must be above zero!')
        self._speed = speed

    def start_engine(self):
        print(f'engine has been turned on!')

    def accelerate(self):
        self.speed += Car.ACCELERATION
        print(f'car speed is now {self.speed}!')

    def decelerate(self):     
        self.speed = max(0, self.speed - Car.ACCELERATION)
        print(f'car speed is now {self.speed}!')

    def stop_engine(self):
        self.speed = 0
        print(f'engine has been turned off!')


ford = Car('Ford', 1962, 'yellow')
print(ford.model)
print(ford.year)
print(ford.color)
print(ford.speed)
ford.start_engine()
ford.accelerate()
ford.accelerate()
ford.decelerate()
ford.stop_engine()
print(ford.speed)


# exercise 2
class Car:
    ACCELERATION = 5
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.speed = 0

    def model(self):
        return self._model

    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('color must be a string')

        self._color = color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed < 0:
            raise ValueError('speed must be above zero!')
        self._speed = speed

    def start_engine(self):
        print(f'engine has been turned on!')

    def accelerate(self):
        self.speed += Car.ACCELERATION
        print(f'car speed is now {self.speed}!')

    def decelerate(self):     
        self.speed = max(0, self.speed - Car.ACCELERATION)
        print(f'car speed is now {self.speed}!')

    def stop_engine(self):
        self.speed = 0
        print(f'engine has been turned off!')


ford = Car('Ford', 1962, 'yellow')
print(ford.model)
print(ford.year)
print(ford.color)
ford.color = 'green'
print(ford.color)
print(ford.speed)
ford.start_engine()
ford.accelerate()
ford.accelerate()
ford.decelerate()
ford.stop_engine()
print(ford.speed)


# exercise 3
class Car:
    ACCELERATION = 5
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self.speed = 0

    def model(self):
        return self._model

    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed < 0:
            raise ValueError('speed must be above zero!')
        self._speed = speed
        
    def paint(self, color):
        if not isinstance(color, str):
            raise TypeError('color has to be a string')
        
        self._color = color
        print(f'The car is now {self.color}!')
        
    def start_engine(self):
        print(f'engine has been turned on!')

    def accelerate(self):
        self.speed += Car.ACCELERATION
        print(f'car speed is now {self.speed}!')

    def decelerate(self):     
        self.speed = max(0, self.speed - Car.ACCELERATION)
        print(f'car speed is now {self.speed}!')

    def stop_engine(self):
        self.speed = 0
        print(f'engine has been turned off!')
        
ford = Car('Ford', 1932, 'yellow')
print(ford.color)
ford.paint('green')
print(ford.color)

# exercise 4
class Car:
    ACCELERATION = 5
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self._color = color
        self.speed = 0

    def model(self):
        return self._model

    def year(self):
        return self._year

    @property
    def color(self):
        return self._color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed < 0:
            raise ValueError('speed must be above zero!')
        self._speed = speed
        
    @classmethod
    def mileage(cls, distance, fuel):
        print(distance / fuel)
        
    def paint(self, color):
        if not isinstance(color, str):
            raise TypeError('color has to be a string')
        
        self._color = color
        print(f'The car is now {self.color}!')
        
    def start_engine(self):
        print(f'engine has been turned on!')

    def accelerate(self):
        self.speed += Car.ACCELERATION
        print(f'car speed is now {self.speed}!')

    def decelerate(self):     
        self.speed = max(0, self.speed - Car.ACCELERATION)
        print(f'car speed is now {self.speed}!')

    def stop_engine(self):
        self.speed = 0
        print(f'engine has been turned off!')
        
ford = Car('Ford', 1962, 'yellow')        
ford.start_engine()
ford.accelerate()
ford.accelerate()
ford.decelerate()
ford.stop_engine()
Car.mileage(12, 2)

# exercise 5
class Person:
    def __init__(self, first, last):
        if self.is_valid_first(first):
            self._first = first
        if self.is_valid_last(last):
            self._last = last
        
    @property
    def name(self):
        return f'{self._first.title()} {self._last.title()}'
    
    @name.setter
    def name(self, name):
        first, last = name
        if self.is_valid_first(first):
            self._first = first
        if self.is_valid_last(last):
            self._last = last
   
    def is_valid_first(cls, name):
        if not isinstance(name, str):
            raise TypeError('first name must be a string')
        elif not name.isalpha():
            raise ValueError('first name must be alphabetic only')
        return True

    def is_valid_last(self, name):
        if not isinstance(name, str):
            raise TypeError('last name must be a string')
        elif not name.isalpha():
            raise ValueError('last name must be alphabetic only')
        return True

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
# actor.name = ('', 'Diesel')
# # ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
# character = Person('Da5id', 'Meier')
# # ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.

# exercise 6
class Car:
    ACCELERATION = 5
    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if not isinstance(model, str):
            raise TypeError('model must be a string')

        self._model = model

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError('year must be an integer')

        if year < 0:
            raise ValueError('year must be above zero')

        self._year = year

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('color must be a string')

        self._color = color

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if speed < 0:
            raise ValueError('speed must be above zero!')
        self._speed = speed
    
    @staticmethod
    def start_engine():
        print(f'engine has been turned on!')

    def accelerate(self):
        self.speed += Car.ACCELERATION
        print(f'car speed is now {self.speed}!')

    def decelerate(self):     
        self.speed = max(0, self.speed - Car.ACCELERATION)
        print(f'car speed is now {self.speed}!')

    def stop_engine(self):
        self.speed = 0
        print(f'engine has been turned off!')


ford = Car('Ford', 1962, 'yellow')
print(ford.model)
print(ford.year)
print(ford.color)
print(ford.speed)
ford.start_engine()
ford.accelerate()
ford.accelerate()
ford.decelerate()
ford.stop_engine()
print(ford.speed)

# no, you shouldn't change it to a static method even though you can, simply because the ability to start the engine would depend on the car's state, such as fuel.