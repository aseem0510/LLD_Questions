from parkinglot.ParkingLot import ParkingLot
from parkinglot.ParkingSpot import ParkingSpot
from vehicles.Vehicle import Vehicle
from payment.PaymentService import PaymentService

class ExitGate:
    def __init__(self, parking_lot: ParkingLot, payment_service: PaymentService):
        self.parking_lot = parking_lot
        self.payment_service = payment_service

    def process_exit(self, spot_number: int, hours_stayed: int):
        # Find the spot by number
        spot = self.parking_lot.get_spot_by_number(spot_number)

        if spot is None or not spot.is_occupied():
            print("Invalid or vacant spot!")
            return

        # Get the vehicle in the spot
        vehicle = spot.get_vehicle()
        if vehicle is None:
            print("No vehicle found in the spot!")
            return

        # Calculate the parking fee
        fee = vehicle.calculate_fee(hours_stayed)

        # Process payment
        self.payment_service.process_payment(fee)

        # Vacate the spot after payment
        self.parking_lot.vacate_spot(spot, vehicle)
        print("Spot vacated successfully!")
