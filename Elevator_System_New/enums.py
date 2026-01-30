from enum import Enum, auto


class Direction(Enum):
    UP = auto()
    DOWN = auto()


class StateType(Enum):
    IDLE = auto()
    MOVING_UP = auto()
    MOVING_DOWN = auto()