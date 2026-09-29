
#^ Class Relationship:
#& - Aggeegation (has a relatipnship)
#* Example: Resturant has a Menu (one class owns the other class)
#? CODING EXAMPLE:
""" class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def printAddress(self):
        print(f"Address is: {self.address.getCity()}, {self.address.pin}, {self.address.state}")

    def editProfile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.editAddress(new_city, new_pin, new_state)

class Address:
    def __init__(self, city, pin, state):
        self.__city = city
        self.pin = pin
        self.state = state

    def getCity(self):
        return self.__city

    def editAddress(self, new_city, new_pin, new_state):
        self.__city = new_city
        self.pin = new_pin
        self.state = new_state


my_address = Address("Vrindavan", 867456, "Uttar Pradesh")
customer = Customer("Radha Rani", "Female", my_address)

customer.printAddress()

customer.editProfile("Krishna", "Barshana", 675467, "Bihar")
customer.printAddress()
 """

#& - Inheritance

""" class User:
    def __init__(self):
        self.name = "Radha"

    def login(self):
        print("You have been looged in successfully...")


class Student(User):

    def enroll(self):
        print("Student have been enrolled in the course.")

user = User()
student = Student()

print(student.name)
student.login()
student.enroll() """

#^ Parent private variable cannot be inherit
""" class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def show(self):
        print(self.__price)


class SmartPhone(Phone):
    def check(self):
        print(self.__price)


s = SmartPhone(20000, "Apple", 13)
print(s.brand)
s.check() """


# ^ Method Overriding
""" class Phone:
    def __init__(self, price, brand, camera):
        self.price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")


s = SmartPhone(20000, "Apple", 13)
s.buy() """


# ^ Super Keyword
# - It not access the attribute of the parent class
# - It can only access method of parent class in child class
# - It cannot called outside of the class

# ^ Types of Inheritance:

#~ - Single Inheritance
#? ===> Single inheritance is a type of inheritance where one child class inherits attributes and methods from a single parent class.

""" class Animal:
    def eat(self, name):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.sleep()
dog.bark() """

""" class Employee:
    def work(self):
        print("Employee is working")

    def attend_meeting(self):
        print("Employee is attending meeting")


class Developer(Employee):
    def write_code(self):
        print("Developer is writing code")


developer = Developer()

developer.work()
developer.attend_meeting()
developer.write_code() """

# ~ Multilevel Inheritance
#? ==> Multilevel inheritance is a type of inheritance where a class inherits from another derived class, creating a chain of inheritance. For example, if Dog inherits from Animal and Puppy inherits from Dog, then Puppy can access methods from both Dog and Animal.

""" class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Puppy(Dog):
    def play(self):
        print("Puppy is playing")


puppy = Puppy()

puppy.eat()
puppy.bark()
puppy.play() """

""" class Grandparent:
    def __init__(self, family_name):
        self.family_name = family_name

    def show_family(self):
        print(f"Family: {self.family_name}")


class Parent(Grandparent):
    def __init__(self, family_name, parent_name):
        super().__init__(family_name)
        self.parent_name = parent_name

    def show_parent(self):
        print(f"Parent: {self.parent_name}")


class Child(Parent):
    def __init__(self, family_name, parent_name, child_name):
        super().__init__(family_name, parent_name)
        self.child_name = child_name

    def show_child(self):
        print(f"Child: {self.child_name}")


person = Child("Mandal", "Rahul", "Aman")

person.show_family()
person.show_parent()
person.show_child() """

# ~ Hierarchical Inheritance:
#? ==> Hierarchical inheritance is a type of inheritance in which multiple child classes inherit from the same parent class. Each child class can have its own specific attributes and methods while sharing common functionality from the parent class.
"""
        Animal
        /    \
       ↓      ↓
     Dog     Cat
"""

""" class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow() """

#~ Multiple Inheritance
# ? ==> Multiple inheritance is a type of inheritance in which a child class inherits from more than one parent class. Python supports multiple inheritance, and when multiple parent classes contain the same method, Python uses Method Resolution Order, or MRO, to determine which implementation should be used.

    #   Parent A        Parent B
    #       \             /
    #        \           /
    #         ↓         ↓
    #            Child


""" class Father:
    def work(self):
        print("Father is working")


class Mother:
    def cook(self):
        print("Mother is cooking")


class Child(Father, Mother):
    def play(self):
        print("Child is playing")


child = Child()

child.work()
child.cook()
child.play() """

#? ==> 🧠 MRO — Method Resolution Order
# ? - MRO batata hai ki Python kisi method ko search karte waqt classes ko kis order mein check karega.
# ? - Definition: MRO, or Method Resolution Order, defines the order in which Python searches classes for methods and attributes, especially when inheritance involves multiple classes.
#* So search order:

# Child
#  ↓
# Father
#  ↓
# Mother
#  ↓
# object

""" class Father:
    def show(self):
        print("Father")


class Mother:
    def show(self):
        print("Mother")


class Child(Father, Mother):
    pass

child = Child()
child.show()
print(Child.mro())
print(Child.__mro__) """

""" class A:
    def show(self):
        print("A")
        super().show()


class B:
    def show(self):
        print("B")
        super().show()


class C(A, B):
    def show(self):
        print("C")
        super().show()


class D:
    def show(self):
        print("D")


class E(C, D):
    def show(self):
        print("E")
        super().show()


obj = E()
obj.show() """


# ~ Hybrid Inheritance:
#? ==> Hybrid inheritance is a combination of two or more types of inheritance, such as multiple, hierarchical, or multilevel inheritance, within the same class hierarchy. In complex hybrid structures, Python uses MRO to determine the method resolution order.

""" class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


class Cat(Animal):
    def meow(self):
        print("Cat is meowing")


class Pet(Dog, Cat):
    def play(self):
        print("Pet is playing")


pet = Pet()

pet.eat()
pet.bark()
pet.meow()
pet.play() """



