# exercise 1
class Car:
    def __init__(self, name):
        self.name = name
        print(f'I am a {name}!')
        
car1 = Car('Volvo')
car2 = Car('Toyota')

# exercise 2
class Foo:
    def __init__(self, name):
        self.name = name

        

foo_object = Foo('Garrick')
type_name_1 = type(foo_object).__name__
type_name_2 = foo_object.__class__.__name__
print(f'I am a {type_name_1} object')
print(f'I am a {type_name_2} object')

