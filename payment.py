from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using PayPal. Payment Successful!")

class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount:.2f} using Credit Card. Payment Successful!")