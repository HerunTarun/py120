# Exercise 1
# Comments show expected output
print(type("Hello"))                # <class 'str'>
print(type(5))                      # <class 'int'>
print(type([1, 2, 3]))              # <class 'list'>

#exercise 2
class Cat:
    pass

# exercise 3
class Cat:
    pass

kitty = Cat()

# exercise 4
class Cat:
    def __init__(self):
        print("I'm a cat!")

kitty = Cat()

# exercise 5
class Cat:
    def __init__(self, name):
        self.name = name
        print(f'Hello! My name is {self.name}!')

kitty = Cat('Sophie')

# exercise 6
class Cat:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()

# exercise 7
class Cat:
    def __init__(self, name):
        self._name = name

    def greet(self):
        print(f"Hello! My name is {self._name}!")

kitty = Cat('Sophie')
kitty.greet()

# exercise 8
class Cat:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    def greet(self):
        print(f"Hello! My name is {self.name}!")
    


kitty = Cat('Sophie')
kitty.greet()

# exercise 9
class Cat:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        self._name = name
        
    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()
kitty.name = 'Luna'
kitty.greet()
# exercise 10
class Person:
    def __init__(self, name='John Doe'):
        self.name = name
        
        
        
        
person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew
