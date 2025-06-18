class FeeCalculator:
    @staticmethod
    def calculate_fee(hours_stayed: int, vehicle):
        return vehicle.calculate_fee(hours_stayed)  # Delegates to vehicle's method
