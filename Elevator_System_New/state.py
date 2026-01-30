from abc import ABC, abstractmethod
from enums import StateType


class State(ABC):
    def __init__(self, elevator):
        self.elevator = elevator

    @abstractmethod
    def move_up(self):
        pass

    @abstractmethod
    def move_down(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def get_type(self) -> StateType:
        pass


class IdleState(State):
    def move_up(self):
        from state import MovingUpState
        self.elevator.set_state(MovingUpState(self.elevator))

    def move_down(self):
        from state import MovingDownState
        self.elevator.set_state(MovingDownState(self.elevator))

    def stop(self):
        pass

    def get_type(self):
        return StateType.IDLE


class MovingUpState(State):
    def move_up(self):
        pass

    def move_down(self):
        from state import MovingDownState
        self.elevator.set_state(MovingDownState(self.elevator))

    def stop(self):
        from state import IdleState
        self.elevator.set_state(IdleState(self.elevator))

    def get_type(self):
        return StateType.MOVING_UP


class MovingDownState(State):
    def move_up(self):
        from state import MovingUpState
        self.elevator.set_state(MovingUpState(self.elevator))

    def move_down(self):
        pass

    def stop(self):
        from state import IdleState
        self.elevator.set_state(IdleState(self.elevator))

    def get_type(self):
        return StateType.MOVING_DOWN