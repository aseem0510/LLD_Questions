from payment_strategy import PaymentStrategy

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: int):
        print(f"₹{amount} paid via Credit Card")
        return True