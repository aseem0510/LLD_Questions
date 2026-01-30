from payment_strategy import PaymentStrategy

class UPIPayment(PaymentStrategy):
    def pay(self, amount: int):
        print(f"₹{amount} paid via UPI")
        return True