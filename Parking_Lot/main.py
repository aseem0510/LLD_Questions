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
    print("3. Get parking status by vehicle type")
    print("4. Exit the system")
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
    # Initialize parking lot with multiple floors
    num_floors = int(input("Enter number of floors: "))
    floors = []

    for i in range(num_floors):
        print(f"\nConfigure Floor {i + 1}")
        car_spots = int(input(f"Enter number of car spots for Floor {i + 1}: "))
        bike_spots = int(input(f"Enter number of bike spots for Floor {i + 1}: "))
        floor = ParkingFloor(floor_number=i + 1, num_of_car_spots=car_spots, num_of_bike_spots=bike_spots)
        floors.append(floor)

    parking_lot = ParkingLot(floors=floors) 
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
            vehicle_type = input("Enter vehicle type (car/bike): ").strip().lower()
            for floor in parking_lot.get_floors():
                print(f"\nStatus for Floor {floor.floor_number}:")
                floor.get_status(vehicle_type)
        elif choice == 4:
            print("Thank you for using the Parking Lot System!")
            break
        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()
