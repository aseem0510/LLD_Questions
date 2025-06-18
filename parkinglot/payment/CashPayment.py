from payment.PaymentStrategy import PaymentStrategy


class CashPayment(PaymentStrategy):
    def process_payment(self, amount: float):
        print(f"Processing cash payment of ${amount}")
        # Logic for cash payment processing
