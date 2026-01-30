from strategy import NearestElevatorStrategy


class ElevatorManager:
    def __init__(self):
        self.elevators = []
        self.observers = []
        self.strategy = NearestElevatorStrategy()
        print("Elevator Manager created")

    def add_elevator(self, elevator):
        self.elevators.append(elevator)

    def add_panel(self, panel):
        self.observers.append(panel)

    def add_request(self, floor, direction):
        print(f"Request received for floor {floor}")
        elevator = self.strategy.select_elevator(floor, direction, self.elevators)
        if elevator:
            elevator.add_to_queue(floor)

    def notify(self, floor, state):
        for obs in self.observers:
            obs.update(floor, state)