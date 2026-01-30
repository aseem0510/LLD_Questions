from payment_strategy import PaymentStrategy

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy

    def process(self, amount: int):
        return self.strategy.pay(amount)