from manager import ElevatorManager
from elevator import Elevator
from panel import OuterPanel
from enums import Direction


def main():
    print("Starting Elevator System Simulation")
    print("==================================")

    manager = ElevatorManager()

    e1 = Elevator(1, manager)
    e2 = Elevator(2, manager)

    manager.add_elevator(e1)
    manager.add_elevator(e2)

    p1 = OuterPanel(1, manager)
    p2 = OuterPanel(2, manager)
    p3 = OuterPanel(3, manager)

    manager.add_panel(p1)
    manager.add_panel(p2)
    manager.add_panel(p3)

    print("\nSimulating Requests\n===================")
    p3.request_elevator(Direction.DOWN)
    p1.request_elevator(Direction.UP)
    p2.request_elevator(Direction.UP)


if __name__ == "__main__":
    main()