# exercise 1
class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'
    
teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!
roger = Bulldog()
print(roger.sleep())
print(roger.speak())
# exercise 2
class Pet:
    def sleep(self):
        return 'sleeping!'

    def run(self):
        return 'running!'

    def jump(self):
        return 'jumping!'
class Cat(Pet):
    def speak(self):
        return 'meow'

class Dog(Cat):
    def speak(self):
        return 'bark!'
    
    def fetch(self):
        return 'fetching!'
    
class Bulldog(Dog):
    def sleep(self):
        return 'snoring!'

carl = Dog()
print(carl.run())
print(carl.fetch())

ruby = Cat()
print(ruby.speak())
print(ruby.jump())
print(ruby.fetch())
   
# exercise 3
# Pet
#     Dog
#         Bulldog
#     Cat

# # exercise 4
# The method resolution order is the order in which Python traverses the class hierarchy in order to find the method being called upon. It is important because it determines which method will be called on for the object calling the method