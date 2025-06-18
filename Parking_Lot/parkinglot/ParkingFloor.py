from parkinglot.CarParkingSpot import CarParkingSpot
from parkinglot.BikeParkingSpot import BikeParkingSpot
from parkinglot.ParkingSpot import ParkingSpot
from typing import List, Optional


class ParkingFloor:
    _global_spot_id = 1  # Class-level counter to ensure unique spot numbers

    def __init__(self, floor_number: int, num_of_car_spots: int, num_of_bike_spots: int):
        self.floor_number = floor_number
        self.spots: List[ParkingSpot] = []

        for _ in range(num_of_car_spots):
            self.spots.append(CarParkingSpot(ParkingFloor._global_spot_id))
            ParkingFloor._global_spot_id += 1

        for _ in range(num_of_bike_spots):
            self.spots.append(BikeParkingSpot(ParkingFloor._global_spot_id))
            ParkingFloor._global_spot_id += 1

    def find_available_spot(self, vehicle_type: str) -> Optional[ParkingSpot]:
        for spot in self.spots:
            if not spot.is_occupied() and spot.get_spot_type().lower() == vehicle_type.lower():
                return spot
        return None
    
    def get_status(self, vehicle_type: str) -> str:
        for spot in self.spots:
            if spot.get_spot_type().lower() == vehicle_type.lower():
                status = "Available" if not spot.is_occupied() else "Occupied"
                print(f"Spot {spot.get_spot_number()} ({spot.get_spot_type()}): {status}")


    def get_parking_spots(self) -> List[ParkingSpot]:
        return self.spots
