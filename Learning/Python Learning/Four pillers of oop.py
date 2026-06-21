 #SINGLE INHERITENCE
print("------SINGLE INHERITENCE-----")
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")


dog = Dog()
dog.bark()   
dog.sound()   


#Multiple Inheritence
print("------MULTIPLE INHERITENCE-----")
class Father:
    def name(self):
        return "My father's name is MD Durul Hoda" 

class Mother:
    def job(self):
        return "My mother is a hosewife"

class Child(Father,Mother):
    def hobby(self):
        return "My favorite game is criket"  

child = Child()
print(child.name())
print(child.job())
print(child.hobby())

#MULTILEVEL INHERITENCE
print("------MULTILEVEL INHERITENCE-----")
class Son(Child):
    def proffession(self):
        return "Student's"

class Abc(Son):
    def fun(self):
        return "Abc Class" 

abc = Abc()
print(abc.hobby())   

#HIERARCHICAL INHERITENCE
print("------HIERARCHICAL INHERITENCE-------")
class A(Abc):
    def printf(self):
        return "Class A"
class B(Abc):
    def printf(self):
        return "Class B"
a = A()
print(a.fun())
b = B()
print(b.fun()) 
#Hibrid Inheritence
print("------Hibrid Inheritence------")
class Grandfather:
    def legacy(self):
        return "I built a real estate empire."

class Father(Grandfather):
    def profession(self):
        return "I am a Doctor."

class Mother(Grandfather):
    def talent(self):
        return "I am a great musician."

class Son(Father, Mother):
    def hobby(self):
        return "I love coding."

son = Son()

print(son.legacy())
print(son.profession())
print(son.talent())
print(son.hobby())


#POLYMORPHISM
class Rat:
    def make_sound(self):
        return "chick chick!"
    
class Cat:
    def make_sound(self):
        return "Meow!"

#function using polymorphism
def animal_sound(animal):
    return animal.make_sound()

rat = Rat()
cat = Cat()

print(animal_sound(rat))
print(animal_sound(cat))


# METHOD OVERLOADING
class MathOperation:
    def add(self,a,b,c=0):
        return a+b+c
math = MathOperation()
print(math.add(3,4))
print(math.add(2,3,4))


#METHOD OVERRIDING
class Father:
    def show(self):
        return "I am Father"

class Son(Father):
    def show(self):
        return "I am Son"

obj = Son()
print(obj.show())


#ENCAPSULATION
class Bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

obj = Bank(1000)
obj.deposit(500)
print(obj.get_balance())


#ABSTRACTION
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def diagonal(self):
        return "root 2 a"

class Circle(Shape):
    def area(self):
        return "Circle Area Formula"

obj = Circle()
print(obj.area())


#INTERFACE 
# not built in python

from abc import ABC, abstractmethod

# Interface (abstract class with only abstract methods)
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass  # No implementation, acts as an interface


class Dog(Animal):
    def make_sound(self):
        return "Bark!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"
    
# Instantiating subclasses
dog = Dog()
cat = Cat()

print(dog.make_sound())  
print(cat.make_sound())  


#DESIGN PATERN

#SINGLETON PATERN
class Singleton:
    _instance = None  # Class-level variable

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
#FACTORY PATTERN
class Circle:
    def draw(self):
        return "Drawing Circle"


class Square:
    def draw(self):
        return "Drawing Square"


class ShapeFactory:
    
    @staticmethod
    def get_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            return None

shape1 = ShapeFactory.get_shape("circle")
print(shape1.draw()) 


#Builder Pattern
class Burger:
    def __init__(self):
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        return self  # Returning self allows method chaining

    def build(self):
        return f"Burger with {' '.join(self.ingredients)}"


# Using the Builder Pattern
burger = Burger().add_ingredient("Lettuce").add_ingredient("Tomato").add_ingredient("Cheese")

print(burger.build())  # Output: Burger with Lettuce Tomato Cheese
 