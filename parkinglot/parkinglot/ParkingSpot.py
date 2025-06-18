from abc import ABC, abstractmethod
from vehicles.Vehicle import Vehicle


class ParkingSpot(ABC):
    def __init__(self, spot_number: int, spot_type: str):
        self.spot_number = spot_number
        self.spot_type = spot_type
        self._is_occupied = False
        self._vehicle = None

    def is_occupied(self) -> bool:
        return self._is_occupied

    @abstractmethod
    def can_park_vehicle(self, vehicle: Vehicle) -> bool:
        pass

    def park_vehicle(self, vehicle: Vehicle):
        if self._is_occupied:
            raise Exception("Spot is already occupied.")
        if not self.can_park_vehicle(vehicle):
            raise Exception(f"This spot is not suitable for a {vehicle.get_vehicle_type()}")
        self._vehicle = vehicle
        self._is_occupied = True

    def vacate(self):
        if not self._is_occupied:
            raise Exception("Spot is already vacant.")
        self._vehicle = None
        self._is_occupied = False

    def get_spot_number(self) -> int:
        return self.spot_number

    def get_vehicle(self) -> Vehicle:
        return self._vehicle

    def get_spot_type(self) -> str:
        return self.spot_type

    def __str__(self):
        return f"ParkingSpot(spot_number={self.spot_number}, is_occupied={self._is_occupied}, vehicle={self._vehicle.get_license_plate() if self._vehicle else 'None'})"
