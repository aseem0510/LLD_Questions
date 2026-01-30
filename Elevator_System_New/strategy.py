from abc import ABC, abstractmethod
from enums import Direction, StateType


class ElevatorSelectionStrategy(ABC):

    @abstractmethod
    def select_elevator(self, floor, direction, elevators):
        pass


class NearestElevatorStrategy(ElevatorSelectionStrategy):

    def select_elevator(self, floor, direction, elevators):
        if not elevators:
            return None

        best = None
        min_distance = float("inf")

        for elevator in elevators:
            distance = abs(elevator.current_floor - floor)
            state = elevator.state.get_type()

            if state == StateType.IDLE and distance < min_distance:
                best = elevator
                min_distance = distance
            elif direction == Direction.UP and state == StateType.MOVING_UP:
                if elevator.current_floor <= floor and distance < min_distance:
                    best = elevator
                    min_distance = distance
            elif direction == Direction.DOWN and state == StateType.MOVING_DOWN:
                if elevator.current_floor >= floor and distance < min_distance:
                    best = elevator
                    min_distance = distance

        return best