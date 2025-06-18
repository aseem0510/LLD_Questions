from payment.PaymentStrategy import PaymentStrategy


class Payment:
    def __init__(self, amount: float, payment_strategy: PaymentStrategy):
        self.amount = amount
        self.payment_strategy = payment_strategy

    def process_payment(self):
        if self.amount > 0:
            self.payment_strategy.process_payment(self.amount)  # Delegate to strategy
        else:
            print("Invalid payment amount.")
