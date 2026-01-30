from collections import deque
from state import IdleState
from enums import StateType


class Elevator:
    def __init__(self, elevator_id, manager):
        self.id = elevator_id
        self.current_floor = 1
        self.manager = manager
        self.state = IdleState(self)
        self.floor_queue = deque()

        print(f"Elevator {self.id} created at floor {self.current_floor}")

    def set_state(self, new_state):
        self.state = new_state
        print(f"Elevator {self.id} changed state to {self.state.get_type().name}")

        # # 🔔 Notify observers via manager
        # self.manager.notify(self.current_floor, self.state.get_type())

    def add_to_queue(self, floor):
        self.floor_queue.append(floor)
        print(f"Elevator {self.id} received request for floor {floor}")
        self.process_queue()

    def process_queue(self):
        if not self.floor_queue:
            return

        target = self.floor_queue[0]

        if target > self.current_floor:
            self.state.move_up()
            self._move(target)
        elif target < self.current_floor:
            self.state.move_down()
            self._move(target)

    def _move(self, target_floor):
        while self.current_floor != target_floor:
            self.current_floor += 1 if target_floor > self.current_floor else -1
            print(f"Elevator {self.id} at floor {self.current_floor}")

            # # 🔔 Notify on every floor change
            # self.manager.notify(self.current_floor, self.state.get_type())

        self.floor_queue.popleft()
        self.state.stop()