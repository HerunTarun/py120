# exercise 1
class Banner:
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        return '| ' + (' ' * len(self.message)) + ' |'

    def _horizontal_rule(self):
        return '+-' + ('-' * len(self.message)) + '-+'

    def _message_line(self):
        return f"| {self.message} |"
    
    
    # Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

# further exploration
class Banner:
    def __init__(self, message, width=None):
        self.message = message
        if self._is_valid_width(width):
            self.width = width
            
    def _is_valid_width(self, width):
        if not isinstance(width, int):
            return False
        elif width < 0:
            return False
        return True
            
    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        if self.width is None:
            return '| ' + (' ' * len(self.message)) + ' |'
        return '| ' + (' ' * self.width) + ' |'

    def _horizontal_rule(self):
        if self.width is None:
            return '+-' + ('-' * len(self.message)) + '-+'
        return '+-' + ('-' * self.width) + '-+'

    def _message_line(self):
        if self.width is None:
            return f"| {self.message} |"
        return self._formatted_message()
    
    def _formatted_message(self):
        return "\n".join(['| ' + self.message[i:i + self.width] + ' |' 
                          for i in range(0, len(self.message), self.width)])
    
    # Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('To boldly go where no one has gone before.', 6)
print(banner)

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

# exercise 2
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @property
    def height(self):
        return self._height
    
    @property
    def area(self):
        return self.width * self.height
        
        
rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True

# exercise 3
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height
    
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
        
square = Square(5)
print(square.area == 25)      # True

# exercise 4
class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self._color = color
    
    @property
    def color(self):
        return self._color
    
    @property
    def info(self):
        return f'My cat {self.name} is {self.age} and has {self.color} fur.'

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)

# exercise 5
class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")

class Cat(Animal):
    legs = 4
    species = 'cat'
    
    def __init__(self, name, age, status):
        super().__init__(name, age, self.legs, self.species, status)
    
    def introduce(self):
        return f'{super().introduce()} Meow meow!'


class Dog(Animal):
    legs = 4
    species = 'dog'
    
    def __init__(self, name, age, status, owner):
        super().__init__(name, age, self.legs, self.species, status)
        self.owner = owner
        
    def introduce(self):
        return f'{super().introduce()} Woof! Woof!'
    
    def greet_owner(self):
        return f'Hi {self.owner}! Woof! Woof!'
        
cat = Cat("Pepe", 4, "happy")
expected = ("Hello, my name is Pepe and I am 4 years old "
            "and happy. Meow meow!")
print(cat.introduce() == expected)      # True

dog = Dog("Bobo", 9, "hungry", "Daddy")
expected = ("Hello, my name is Bobo and I am 9 years old "
            "and hungry. Woof! Woof!")
print(dog.introduce() == expected)                  # True
print(dog.greet_owner() == "Hi Daddy! Woof! Woof!") # True

# exercise 6
class Shelter:
    def __init__(self):
        self.adoptions = {}
    
    def adopt(self, adopter, animal):
        self.adoptions.setdefault(adopter.name, []).append(animal)
        adopter.add_pet(animal)
        
    
    def print_adoptions(self):
        for adopter, pets in self.adoptions.items():
            print(f'{adopter} has adopted the following pets:')
            for pet in pets:
                print(f'a {pet.species} named {pet.name}')
            print()

class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name
    
    @property
    def species(self):
        return self._species
    
    @property
    def name(self):
        return self._name
    
class Owner:
       
    def __init__(self, name):
        self._name = name
        self._pets = []
        
    @property
    def name(self):
        return self._name
    
    def number_of_pets(self):
        return len(self._pets)
    
    def add_pet(self, pet):
        self._pets.append(pet)
    
cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
# futher exploration
class Shelter:
    def __init__(self):
        self.available = []
        self.adoptions = {}
    
    @property
    def number_of_available_pets(self):
        return len(self.available)
    
    def intake(self, animal):
        self.available.append(animal)
    
    def adopt(self, adopter, animal):
        self.adoptions.setdefault(adopter, []).append(animal)
        adopter.add_pet(animal)
        
    def print_available(self):
        print(f'The Animal Shelter has the following unadopted pets:')
        for pet in self.available:
            print(pet.pet_info())
        print()
            
    def print_adoptions(self):
        for adopter, pets in self.adoptions.items():
            print(f'{adopter.name} has adopted the following pets:')
            for pet in pets:
                print(pet.pet_info())
            print()

class Pet:
    def __init__(self, species, name):
        self._species = species
        self._name = name
    
    @property
    def species(self):
        return self._species
    
    @property
    def name(self):
        return self._name
    
    def pet_info(self):
        return f'a {self.species} named {self.name}'
    
class Owner:
       
    def __init__(self, name):
        self._name = name
        self._pets = []
        
    @property
    def name(self):
        return self._name
    
    def number_of_pets(self):
        return len(self._pets)
    
    def add_pet(self, pet):
        self._pets.append(pet)
    
cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.intake(darwin)
shelter.intake(kennedy)
shelter.intake(sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_available()
shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")
print(f"The Animal Shelter has {shelter.number_of_available_pets} unadopted pets.")

# exercise 7
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info(self):
        return f"{self.make} {self.model}"    
        
class Car(Vehicle):
    def get_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def get_wheels(self):
        return 2

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def get_wheels(self):
        return 6
    
# further exploration
class Vehicle:
    def __init__(self, make, model, wheels):
        self.make = make
        self.model = model
        self.wheels = wheels
    
    def info(self):
        return f"{self.make} {self.model}"    
    
    def get_wheels(self):
        return self.wheels     

class Car(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 4)

class Motorcycle(Vehicle):
    def __init__(self, make, model):
        super().__init__(make, model, 2)

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model, 6)
        self.payload = payload
# exercise 8
class MoveMixin:
    def walk(self):
        return f'{self.name} {self.gait()} forward'

class Person(MoveMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(MoveMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(MoveMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
    
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

# exercise 9
class WalkMixin:
    def titled(self):
        try:
            self.title
        except AttributeError:
            return f'{self.name}'
        else:
            return f'{self.title} {self.name}'
    def walk(self):
        return f'{self.titled()} {self.gait()} forward'

class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

class Noble(WalkMixin):
    def __init__(self, name, title):
        self._name = name
        self._title = title
    
    @property
    def name(self):
        return self._name
    
    @property
    def title(self):
        return self._title
    
    def gait(self):
        return 'struts'
    
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"
byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

# better version
class WalkMixin:
    def walk(self):
        return f'{self} {self.gait()} forward'

class Person(WalkMixin):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def gait(self):
        return "strolls"

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def gait(self):
        return "runs"

class Noble(WalkMixin):
    def __init__(self, name, title):
        self._name = name
        self._title = title
    
    def __str__(self):
        return f'{self._title} {self._name}'
    @property
    def name(self):
        return self._name
    
    @property
    def title(self):
        return self._title
    
    def gait(self):
        return 'struts'
    
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"
byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

# exercise 10
class House:
    def __init__(self, price):
        self.price = price
    
    def __lt__(self, other):
        if isinstance(other, House):
            return self.price < other.price
    
    def __gt__(self, other):
        if isinstance(other, House):
            return self.price > other.price
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

home1 = House(100000)
home2 = House(150000)
if home1 < home2:
    print("Home 1 is cheaper")
if home2 > home1:
    print("Home 2 is more expensive")

# exercise 11
class Wallet:
    def __init__(self, money):
        self.money = money
        
    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, money):
        self._money = money
    
    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        amount = self.money + other.money
        return Wallet(amount)
    
wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.money)       # True

# exercise 12
class Wallet:
    def __init__(self, money):
        self.money = money
        
    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, money):
        self._money = money
    
    def __add__(self, other):
        if not isinstance(other, Wallet):
            return NotImplemented
        amount = self.money + other.money
        return Wallet(amount)
    
    def __str__(self):
        return f'Wallet with ${self.money}'
    
wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)       # True

# exercise 13
class Transform:
    def __init__(self, text):
        self.text = text
    
    @classmethod    
    def lowercase(cls, string):
        return string.lower()
    
    
    def uppercase(self):
        return self.text.upper()
    
my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz