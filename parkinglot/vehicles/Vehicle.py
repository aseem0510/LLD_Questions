from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: str):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    def get_vehicle_type(self) -> str:
        return self.vehicle_type

    def get_license_plate(self) -> str:
        return self.license_plate

    @abstractmethod
    def calculate_fee(self, hours_stayed: int) -> float:
        pass
