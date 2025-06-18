from vehicles.Vehicle import Vehicle

class BikeVehicle(Vehicle):
    RATE = 5.0  # $5 per hour for bikes

    def __init__(self, license_plate: str):
        super().__init__(license_plate, "Bike")

    def calculate_fee(self, hours_stayed: int) -> float:
        return hours_stayed * self.RATE
