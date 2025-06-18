from Vehicle import Vehicle

class OtherVehicle(Vehicle):
    RATE = 15.0  # $15 per hour for other vehicles

    def __init__(self, license_plate: str):
        super().__init__(license_plate, "Other")

    def calculate_fee(self, hours_stayed: int) -> float:
        return hours_stayed * self.RATE
