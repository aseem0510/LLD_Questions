from payment.PaymentStrategy import PaymentStrategy


class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount: float):
        print(f"Processing credit card payment of ${amount}")
        # Logic for credit card payment processing
