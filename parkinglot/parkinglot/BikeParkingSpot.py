from parkinglot.ParkingSpot import ParkingSpot
from vehicles.Vehicle import Vehicle

class BikeParkingSpot(ParkingSpot):
    def __init__(self, spot_number: int):
        super().__init__(spot_number, "Bike")

    def can_park_vehicle(self, vehicle: Vehicle) -> bool:
        return vehicle.get_vehicle_type().lower() == "bike"
