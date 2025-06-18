from payment.PaymentStrategy import PaymentStrategy


class UPIPayment(PaymentStrategy):
    def process_payment(self, amount: float):
        print(f"Processing UPI payment of ${amount}")
        # Logic for UPI payment processing
