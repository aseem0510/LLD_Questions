from parkinglot.ParkingSpot import ParkingSpot
from parkinglot.ParkingFloor import ParkingFloor
from vehicles.Vehicle import Vehicle
from typing import List, Optional

class ParkingLot:
    def __init__(self, floors: List[ParkingFloor]):
        self.floors = floors

    def find_available_spot(self, vehicle_type: str) -> Optional[ParkingSpot]:
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle_type)
            if spot:
                return spot
        return None

    def park_vehicle(self, vehicle: Vehicle) -> Optional[ParkingSpot]:
        spot = self.find_available_spot(vehicle.get_vehicle_type())
        if spot:
            spot.park_vehicle(vehicle)
            print(f"Vehicle parked successfully in spot: {spot.get_spot_number()}")
            return spot
        print(f"No parking spots available for {vehicle.get_vehicle_type()}!")
        return None

    def vacate_spot(self, spot: ParkingSpot, vehicle: Vehicle):
        if spot and spot.is_occupied() and spot.get_vehicle() == vehicle:
            spot.vacate()
            print(f"{vehicle.get_vehicle_type()} vacated the spot: {spot.get_spot_number()}")
        else:
            print("Invalid operation! Either the spot is already vacant or the vehicle does not match.")

    def get_spot_by_number(self, spot_number: int) -> Optional[ParkingSpot]:
        for floor in self.floors:
            for spot in floor.get_parking_spots():
                if spot.get_spot_number() == spot_number:
                    return spot
        return None

    def get_floors(self) -> List[ParkingFloor]:
        return self.floors
