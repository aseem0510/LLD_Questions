from gates.EntranceGate import EntranceGate
from gates.ExitGate import ExitGate
from parkinglot.ParkingFloor import ParkingFloor
from parkinglot.ParkingLot import ParkingLot
from payment.PaymentService import PaymentService


def show_menu():
    print("\n******************************************************")
    print("Please choose an option from below:")
    print("1. Park a vehicle")
    print("2. Vacate a vehicle spot")
    print("3. Exit the system")
    print("******************************************************")


def get_user_choice():
    try:
        return int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return -1


def park_vehicle(entrance_gate: EntranceGate):
    entrance_gate.process_entrance()


def vacate_spot(exit_gate: ExitGate):
    try:
        spot_number = int(input("Enter the spot number to vacate: "))
        hours_stayed = int(input("Enter the number of hours the vehicle stayed: "))
        exit_gate.process_exit(spot_number, hours_stayed)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def main():
    # Initialize the parking lot with one floor and 2 car spots and 2 bike spots
    floor = ParkingFloor(floor_number=1, num_of_car_spots=2, num_of_bike_spots=2)
    parking_lot = ParkingLot(floors=[floor])

    # Initialize services
    payment_service = PaymentService()

    # Initialize gates
    entrance_gate = EntranceGate(parking_lot)
    exit_gate = ExitGate(parking_lot, payment_service)

    # Welcome message
    print("\n=========================================")
    print("   Welcome to the Parking Lot System!    ")
    print("=========================================")

    # Main loop
    while True:
        show_menu()
        choice = get_user_choice()

        if choice == 1:
            park_vehicle(entrance_gate)
        elif choice == 2:
            vacate_spot(exit_gate)
        elif choice == 3:
            print("Thank you for using the Parking Lot System!")
            break
        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()
