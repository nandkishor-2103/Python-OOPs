
#! =================================
#!           POLYMORPHISM
#! =================================
#? ===> the ability of a single function, method, or operator to behave differently depending on the context or the type of object it is working with

# It have three concept that are:
#* - Method Overriding
#* - Method Overloading
#* - Operator Overloading

#^ ================== METHOD OVERRIDING ===================
#? Method overriding means redefining a parent class method inside a child class to provide specialized behavior.
""" class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


animals = [Dog(), Cat()]

for animal in animals:
    animal.speak() """

#^ ================== METHOD OVERLOADING ===================
# Q1. What is method overloading?

#? Method overloading refers to defining the same method name with different parameter combinations to support different ways of calling the method.
#* Python does not support traditional method overloading like Java or C++. If we define multiple methods with the same name in a class, the latest definition replaces the previous one. However, we can achieve similar behavior using default arguments, *args, **kwargs, or explicit argument handling.

#~ 1️⃣ Default Arguments
""" class Calculator:

    def add(self, a, b = 0, c = 0):
        return a + b + c


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(10)) """

#~ 2️⃣ *args Se Flexible Arguments
""" class Calculator:

    def add(self, *args):
        return sum(args)


calc = Calculator()

print(calc.add(10, 20))
print(calc.add(10, 20, 30))
print(calc.add(1, 2, 3, 4, 5,)) """


""" class LLMService:

    def generate(self, prompt, temperature=0.7, max_tokens=500):
        print("Prompt:", prompt)
        print("Temperature:", temperature)
        print("Max tokens:", max_tokens)


llm = LLMService()

llm.generate("Explain Python")

llm.generate(
    "Explain Python",
    temperature=0.2
)

llm.generate(
    "Explain Python",
    temperature=0.5,
    max_tokens=1000
) """

#^ ================== OPERATOR OVERLOADING ===================
#? ===> Operator overloading is the ability to define how Python operators behave for user-defined objects by implementing special methods such as __add__(), __sub__(), and __eq__().

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y
        )

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(10, 20)
p2 = Point(10, 15)

p3 = p1 + p2

print(p3)
