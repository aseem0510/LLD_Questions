from abc import ABC, abstractmethod
from enums import StateType


class ElevatorObserver(ABC):

    @abstractmethod
    def update(self, floor: int, state: StateType):
        pass