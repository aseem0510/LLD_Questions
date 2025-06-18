from payment.Payment import Payment
from payment.CreditCardPayment import CreditCardPayment
from payment.CashPayment import CashPayment
from payment.UPIPayment import UPIPayment


class PaymentService:
    def __init__(self, input_function=input):
        self.input = input_function  # Allow dependency injection for easier testing

    def process_payment(self, fee: float):
        self.choose_payment_method(fee)

    def choose_payment_method(self, fee: float):
        print(f"Total fee: {fee}")
        print("Choose payment method:")
        print("1. Credit Card")
        print("2. Cash")
        print("3. UPI")

        try:
            choice = int(self.input("Enter choice: "))
        except ValueError:
            print("Invalid input! Defaulting to Cash payment.")
            choice = 2

        if choice == 1:
            payment = Payment(fee, CreditCardPayment())
        elif choice == 2:
            payment = Payment(fee, CashPayment())
        elif choice == 3:
            payment = Payment(fee, UPIPayment())
        else:
            print("Invalid choice! Defaulting to Cash payment.")
            payment = Payment(fee, CashPayment())

        payment.process_payment()
