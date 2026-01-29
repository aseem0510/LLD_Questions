from vehicles.VehicleFactory import VehicleFactory
from parkinglot.ParkingLot import ParkingLot

class EntranceGate:
    def __init__(self, parking_lot: ParkingLot):
        self.parking_lot = parking_lot

    def process_entrance(self):
        license_plate = input("Enter the vehicle license plate: ")
        vehicle_type = input("Enter the vehicle type (Car or Bike): ")

        vehicle = VehicleFactory.create_vehicle(vehicle_type, license_plate)
        if vehicle is None:
            print("Invalid vehicle type! Only Car and Bike are allowed.")
            return

        # spot = self.parking_lot.park_vehicle(vehicle)
        # if spot:
        #     print(f"Vehicle parked successfully in spot: {spot.get_spot_number()}")
        # else:
        #     print("No available spots for the vehicle type.")
        self.parking_lot.park_vehicle(vehicle)
