import logging as log
from enum import IntEnum
from dataclasses import dataclass
from strenum import StrEnum


MOVEMENT_PORT = 30003
REALTIME_FEEDBACK_PORT = 30004
DASHBOARD_PORT = 29999


# There could be more, but not documented in:
# https://github.com/Dobot-Arm/TCP-IP-Protocol/blob/master/README-EN.md
class DobotError(IntEnum):
    FAIL_TO_GET = -1
    COMMAND_ERROR = -10000
    PARAMETER_NUM_ERROR = -20000
    WRONG_PARAM_TYPE = -30000
    FIRST_PARAM_INCORRECT = -30001
    SECOND_PARAM_INCORRECT = -30002
    PARAMETER_RANGE_INCORRECT = -40000
    FIRST_PARAM_RANGE = -40001
    SECOND_PARAM_RANGE = -40002

@dataclass
class IOPort:
    mode: int
    distance: int
    index: int
    status: int

    def __post_init__(self, mode: int, distance: int, index: int, status: int):
        self.mode = self.__clamp(mode, 0, 1)
        self.distance = self.__clamp(distance, 0, 100)
        self.index = self.__clamp(index, 1, 24)
        self.status = self.__clamp(status, 0, 1)
    
    def __clamp(self, val: int, local_min: int, local_max: int) -> int:
        log.info(f"{val} was clamped to the range {local_min}, {local_max}")
        return max(local_min, min(val, local_max))

class RobotMode(IntEnum):
    INIT = 1
    BRAKE_OPEN = 2
    RESERVED = 3
    DISABLED = 4
    ENABLE = 5
    BACKDRIVE = 6
    RUNNING = 7
    RECORDING = 8
    ERROR = 9
    PAUSE = 10
    JOG = 11

class JointSelection(StrEnum):
    J1NEG = "J1-"
    J1POS = "J1+"
    J2NEG = "J2-"
    J2POS = "J2+"
    J3NEG = "J3-"
    J3POS = "J3+"
    J4NEG = "J4-"
    J4POS = "J4+"
    J5NEG = "J5-"
    J5POS = "J5+"


class RobotType(IntEnum):
    CR3 = 3
    CR3L = 31
    CR5 = 5
    CR7 = 7
    CR10 = 10
    CR12 = 12
    CR16 = 16
    MG400 = 1
    M1PRO = 2
    NOVA2 = 101
    NOVA5 = 103
    CR3V2 = 113
    CR5V2 = 115
    CR10V2 = 120