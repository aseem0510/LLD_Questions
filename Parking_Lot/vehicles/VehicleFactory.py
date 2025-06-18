from vehicles.CarVehicle import CarVehicle
from vehicles.BikeVehicle import BikeVehicle
from vehicles.Vehicle import Vehicle

class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type: str, license_plate: str) -> Vehicle:
        if vehicle_type.lower() == "car":
            return CarVehicle(license_plate)
        elif vehicle_type.lower() == "bike":
            return BikeVehicle(license_plate)
        return None  # For unsupported vehicle types
