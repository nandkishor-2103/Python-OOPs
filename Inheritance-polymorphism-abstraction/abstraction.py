
#^ ==================== ABSTRACTION =========================
#? ==> Abstraction hides implementation details and exposes only the essential functionality to the user.
#~ 1. Abstract method always contain atleast one abstract method
#~ 2. We never make object of abstract class

#* EXAMPLES:
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class UPI(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid using UPI")

class CreditCard(Payment):

    def pay(self, amount):
        print(f"₹{amount} paid using Credit Card")

upi = UPI()
upi.pay(500)

creditCard = CreditCard()
creditCard.pay(400)
