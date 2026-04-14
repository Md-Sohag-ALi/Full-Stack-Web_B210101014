import math
class Car:
    def __init__(self,mk,mdl,yr,pr):       #magic function /dunder
        print("Initializing a car")
        self.make = mk
        self.model = mdl
        self.year = yr
        self.price = pr
    
    def __str__(self):                     #magic function /dunder
        return f"{self.make} {self.model} {self.year} {self.price}"

    def Update_price(self , newprice):
        self.price = newprice


car1 = Car("Subaru","forester",2014,10000)
car2 = Car("Toyota","Camry",2020,30000)
print(car1)
car1.Update_price(9000)
print(car1)
print(car2) 

#Another Class
class Fraction:
    def __init__(self,nu,dnu):
        self.numerator = nu
        if dnu == 0:
            raise ValueError("Denumerator Can't be 0")
        self.dnumerator = dnu

    def __str__(self):
        return f"{self.numerator}/{self.dnumerator}" 

    def simplify(self):
        g = math.gcd(self.numerator , self.dnumerator)   
        self.numerator //=g
        self.dnumerator //=g
    def __add__(self, f):
         n = math.lcm(self.dnumerator,f.dnumerator)
         d = self.numerator *(n // self.dnumerator) \
              + f.numerator *(n // f.dnumerator)
         return Fraction(d,n)
               

fraction1 = Fraction(1,5)
""" print(fraction1)  
fraction1.simplify()
print(fraction1)   """
fraction2 = Fraction(4,10)
fraction3 = fraction1 + fraction2
print(fraction3)
fraction3.simplify()
print(fraction3)

#Class method and Static Method
class Example:
    class_variable = "I belong to the class"

    @staticmethod
    def static_method():
        #print(class_variable) --> u can't access
        return "Inside a static Method"
    @classmethod
    def class_method(cls):
        return f"I can access {cls.class_variable}"
print(Example.class_method())  
print(Example.static_method())  
