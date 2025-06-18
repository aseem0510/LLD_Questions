from vehicles.Vehicle import Vehicle

class CarVehicle(Vehicle):
    RATE = 10.0  # $10 per hour for cars

    def __init__(self, license_plate: str):
        super().__init__(license_plate, "Car")

    def calculate_fee(self, hours_stayed: int) -> float:
        return hours_stayed * self.RATE
