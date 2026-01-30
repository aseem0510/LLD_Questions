from observer import ElevatorObserver


class OuterPanel(ElevatorObserver):
    def __init__(self, floor, manager):
        self.floor = floor
        self.manager = manager
        print(f"Panel created at floor {floor}")

    def request_elevator(self, direction):
        print(f"Panel at floor {self.floor} requesting elevator")
        self.manager.add_request(self.floor, direction)

    def update(self, floor, state):
        print(f"Panel {self.floor} update: Elevator at floor {floor} ({state.name})")