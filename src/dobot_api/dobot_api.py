import logging as log
from typing import Optional
from util import *
from constants import *


# TODO: The outer dashboard classes will implement all shared functionality, but the CR version will have additional methods.
# TODO: A neater way of sharing methods across models.


# We leave it upon the caller of the API to see if they care about the errors.
# There should be no error handling inside of this API.
# This is just a faithful translation and communication layer.


class Dobot:
    def __init__(self, ip: str, is_cr: bool = False, logging: bool = False, log_name: str = "output.log", log_level = log.DEBUG):
        if logging:
            log.basicConfig(filename=log_name, level=log_level)
        self.movement = Movement(ip)
        self.feedback = Feedback(ip)
        self.dashboard = Dashboard(ip)


class Movement(DobotSocketConnection):
    def __init__(self, ip: str):
        super().__init__(ip, MOVEMENT_PORT)

    # MovJ
    def move_joint(
        self, x: float, y: float, z: float, rx: float, ry: float, rz: float
    ) -> Optional[DobotError]:
        error_id, ret_val = self.send_command(
            "MovJ({:f}, {:f}, {:f}, {:f}, {:f}, {:f})".format(x, y, z, rx, ry, rz)
        )
        return error_id

    # MovL
    def move_linear(
        self, x: float, y: float, z: float, rx: float, ry: float, rz: float
    ) -> Optional[DobotError]:
        error_id, ret_val = self.send_command(
            "MovL({:f}, {:f}, {:f}, {:f}, {:f}, {:f})".format(x, y, z, rx, ry, rz)
        )
        return error_id

    # MoveJog
    def move_jog(self, joint: JointSelection) -> Optional[DobotError]:
        error_id, ret_val = self.send_command("MovJog({})".format(joint))
        return error_id


class Dashboard(DobotSocketConnection):
    def __init__(self, ip: str):
        super().__init__(ip, DASHBOARD_PORT)

    def turn_on(self) -> Optional[DobotError]:
        error_id, ret_val = self.send_command("PowerOn()")
        return error_id

    def enable(self) -> Optional[DobotError]:
        error_id, ret_val = self.send_command("EnableRobot()")
        return error_id

    def disable(self) -> Optional[DobotError]:
        error_id, ret_val = self.send_command("DisableRobot()")
        return error_id

    def reset(self) -> Optional[DobotError]:
        error_id, ret_val = self.send_command("ResetRobot()")
        return error_id

    def clear_errors(self) -> Optional[DobotError]:
        error_id, ret_val = self.send_command("ClearError()")
        return error_id

    def emergency_stop(self) -> Optional[DobotError]:
        error_id, ret_val = self.send_command("EmergencyStop()")
        return error_id

    def robot_mode(self) -> DobotError | RobotMode:
        error_id, ret_val = self.send_command("RobotMode()")
        if error_id:
            return error_id
        else:
            # TODO: Handle this if error'd
            return RobotMode(int(ret_val))
    
    def set_linear_accel(self, rate: int) -> Optional[DobotError]:
        rate = clamp(rate, 1, 100)
        error_id, ret_val = self.send_command("AccL({:d})".format(rate))
        return error_id

    def set_joint_accel(self, rate: int) -> Optional[DobotError]:
        rate = clamp(rate, 1, 100)
        error_id, ret_val = self.send_command("AccJ({:d})".format(rate))
        return error_id
    
    def set_linear_velocity(self, rate: int) -> Optional[DobotError]:
        rate = clamp(rate, 1, 100)
        error_id, ret_val = self.send_command("SpeedL({:d})".format(rate))
        return error_id

    def set_joint_velocity(self, rate: int) -> Optional[DobotError]:
        rate = clamp(rate, 1, 100)
        error_id, ret_val = self.send_command("SpeedJ({:d})".format(rate))
        return error_id

    def set_speedfactor(self, ratio: int) -> Optional[DobotError]:
        ratio = clamp(ratio, 1, 100)
        error_id, ret_val = self.send_command("SpeedFactor({:d})".format(ratio))
        return error_id

    def set_user(self, index: int) -> Optional[DobotError]:
        index = clamp(index, 0, 9)
        error_id, ret_val = self.send_command("User({:d})".format(index))
        return error_id

    def set_tool(self, index: int) -> Optional[DobotError]:
        index = clamp(index, 0, 9)
        error_id, ret_val = self.send_command("Tool({:d})".format(index))
        return error_id
    
   
class Feedback(DobotSocketConnection):
    def __init__(self, ip: str):
        super().__init__(ip, REALTIME_FEEDBACK_PORT)
