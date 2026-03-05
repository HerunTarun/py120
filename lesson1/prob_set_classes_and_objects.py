# exercise 1
class Person:
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

bob = Person('bob')
print(bob.name)           # bob
bob.name = 'Robert'
print(bob.name)           # Robert

# exercise 2
class Person:
    def __init__(self, name):
        names = name.split()
        self._first_name = names[0]
        self._last_name = ''
        if len(names) > 1:
            self._last_name = names[-1]
    
    @property
    def name(self):
        if not self._last_name:
            return self._first_name
        return f'{self._first_name} {self._last_name}'
    
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError('Name must be a string')
   
        self._first_name = first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError('Name must be a string')
        
        self._last_name = last_name
        
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith
# exercise 3
class Person:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        if not self._last_name:
            return self._first_name
        return f'{self._first_name} {self._last_name}'
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        names = name.split()
        self._first_name = names[0]
        self._last_name = ''
        if len(names) > 1:
            self._last_name = names[-1]
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError('Name must be a string')
   
        self._first_name = first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError('Name must be a string')
        
        self._last_name = last_name
        
bob = Person('Robert')
print(bob.name)             # Robert
print(bob.first_name)       # Robert
print(repr(bob.last_name))  # ''
bob.last_name = 'Smith'
print(bob.name)             # Robert Smith

bob.name = 'Prince'
print(bob.first_name)       # Prince
print(repr(bob.last_name))  # ''

bob.name = 'John Adams'
print(bob.first_name)       # John
print(bob.last_name)        # Adams
# exercise 4
        
bob = Person('Robert Smith')
rob = Person('Robert Smith')
print(bob.name == rob.name)

# exercise 5
bob = Person('Robert Smith')
print(f"The person's name is: {bob}")
# I think it prints "The person's name is Person object at memory address

# exercise 6 
class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name    
    
    @property
    def name(self):
        if not self._last_name:
            return self._first_name
        return f'{self._first_name} {self._last_name}'
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name must be a string')
        names = name.split()
        self._first_name = names[0]
        self._last_name = ''
        if len(names) > 1:
            self._last_name = names[-1]
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str):
            raise TypeError('Name must be a string')
   
        self._first_name = first_name
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str):
            raise TypeError('Name must be a string')
        
        self._last_name = last_name

bob = Person('Robert Smith')
print(f"The person's name is: {bob}")
# I think this will print 'The person's name is Robert Smith'
