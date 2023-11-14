'''
The code (directly below) exhibits polymorphic behavior by using objects of different classes interchangeably through a common interface method, process_payment. 
However, in the (next) example (from line 33), polymorphism is shown in the more traditional sense where subclasses inherit and then override a method from a common superclass.
'''

class CreditCardPayment():
    def process_payment(self):
        print("Processing credit card payment")

class PaypalPayment():
    def process_payment(self):
        print("Processing PayPal payment")

class BankTransferPayment():
    def process_payment(self):
        print("Processing bank transfer payment")

# Usage
payments = [CreditCardPayment(), PaypalPayment(), BankTransferPayment()]
for payment in payments:
    payment.process_payment()





'''
In the traditional sense of polymorphism, we use inheritance where a subclass overrides a method from its superclass. 
Here, the superclass `Payment` provides a common interface for all payment types. Each subclass then provides its own 
specific implementation of the `process_payment` method. By doing so, we can use objects of the subclasses interchangeably, 
and when we call `process_payment`, the correct subclass method is invoked.
'''
class Payment:
    def process_payment(self, amount):
        raise NotImplementedError("Subclass must implement abstract method")

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing credit card payment for £{amount}")

class PaypalPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing PayPal payment for £{amount}")

class BankTransferPayment(Payment):
    def process_payment(self, amount):
        print(f"Processing bank transfer payment for £{amount}")

# Usage
payments = [
    CreditCardPayment(), 
    PaypalPayment(), 
    BankTransferPayment()
]

for payment in payments:
    payment.process_payment(100)  # Passing the payment amount as an argument






'''
The code demonstrates polymorphism by using the shared method 'change_direction' as a common interface across different classes.

Composition is used here because Vehicle contains an object of Wheels or Tracks, demonstrating a "has-a" relationship rather than "is-a".  "Vehicle has a controller, which is either Wheels or Tracks".
'''

import time

class Tracks:
    def change_direction(self, left, on):
        print("tracks: ", left, on)

class Wheels:
    def change_direction(self, left, on):
        print("wheels: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.change_direction(left, True)
        time.sleep(0.25)
        self.controller.change_direction(left, False)


wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
tracked.turn(False)

# Note to self: 
# Remember the 'True' argument on the second last line is received by 'left' (not 'True') on the first line after the turn method definition:
# Meaning the 'left' and 'on' Wheels.change_direction paramaters first receive ('True', 'True').