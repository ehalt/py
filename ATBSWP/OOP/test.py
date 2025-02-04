# class Dog:
#     species = 'Canis familiaris'
#     # constructor 
#     def __init__(self, name, age) :
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         return f"{self.name} says woof!"
    

# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 5)

# print(dog1.name)
# print(dog2.age)
# print(dog1.bark())
# print(dog2.species)










'''
        Class and static methods 
'''


# class MathOperations:
#     @classmethod
#     def multiply(cls, a, b):
#         return a * b
    

#     @staticmethod
#     def add(a, b) : 
#         return a + b

# print(MathOperations.multiply(3, 4))
# print(MathOperations.add(5, 3))











'''
        inheritance
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"
    
class Cat(Animal):
    def speak (self):
        return f"{self.name} says meaw!!"
    


cat = Cat("Whiskers")
print(cat.speak())

