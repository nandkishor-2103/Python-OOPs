
#^ ================ ENCAPSULATION ====================
#? ==> Encapsulation is the process of bundling data and methods inside a class and controlling direct access to the data.
# OR
# ? ==> Encapsulation involves bundling data (attributes) and the methods that operate on that data into a single unit (a class) while restricting direct access to some of the object's components

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(5000)

account.deposit(1000)
account.withdraw(2000)

print(account.get_balance())



#^ ============ STATIC =============
#? ==> A static method is a method defined inside a class that does not depend on instance or class state and therefore does not require self or cls.

class User:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def is_valid_email(email):
        return "@" in email


user = User("Rahul")

print(user.is_valid_email("rahul@gmail.com"))
print(User.is_valid_email("rahul@gmail.com"))

#^ ==================== SUPER ======================
#? ==> super() is used to access the next class in the inheritance hierarchy according to Python's MRO, commonly to call parent methods or constructors.
#? ==> Method Overriding mein super() useful hota hai
class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no


student = Student("Rahul", 101)

print(student.name)
print(student.roll_no)
