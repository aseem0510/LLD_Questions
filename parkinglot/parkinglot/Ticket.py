from datetime import datetime
from parkinglot.ParkingSpot import ParkingSpot
from vehicles.Vehicle import Vehicle


class Ticket:
    def __init__(self, parking_spot: ParkingSpot, vehicle: Vehicle):
        self.parking_spot = parking_spot
        self.vehicle = vehicle
        self.start_time = datetime.now()  # Set current time as the start time
