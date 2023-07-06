from util import DobotSocketConnection
from typing import Optional
from constants import *


# TODO: The outer dashboard classes will implement all shared functionality, but the CR version will have additional methods.
# TODO: A neater way of sharing methods across models.


# We leave it upon the caller of the API to see if they care about the errors.
# There should be no error handling inside of this API.
# This is just a faithful translation and communication layer.

class Dobot:
    def __init__(self, ip: str):
        self.movement = Movement(ip)
        self.feedback = Feedback(ip)
        self.dashboard = Dashboard(ip)


class Movement(DobotSocketConnection):
    def __init__(self, ip: str):
        super().__init__(ip, MOVEMENT_PORT)

    # MovJ
    def move_joint(self, x: float, y: float, z: float, rx: float, ry: float, rz: float) -> Optional[DobotError]:
        self.send_command("MovJ({:f}, {:f}, {:f}, {:f}, {:f}, {:f})".format(x, y, z, rx, ry, rz))
        error_id, ret_val = self.await_reply()
        return error_id
    
    # MovL
    def move_linear(self, x: float, y: float, z: float, rx: float, ry: float, rz: float) -> Optional[DobotError]:
        self.send_command("MovL({:f}, {:f}, {:f}, {:f}, {:f}, {:f})".format(x, y, z, rx, ry, rz))
        error_id, ret_val = self.await_reply()
        return error_id

    # MoveJog
    def move_jog(self, joint: JointSelection) -> Optional[DobotError]:
        self.send_command("MovJog({})".format(joint))
        error_id, ret_val = self.await_reply()
        return error_id



class Dashboard(DobotSocketConnection):
    def __init__(self, ip: str):
        super().__init__(ip, DASHBOARD_PORT)

    def turn_on(self) -> Optional[DobotError]:
        self.send_command("PowerOn()")
        error_id, ret_val = self.await_reply()
        return error_id
  
    def enable(self) -> Optional[DobotError]:
        self.send_command("EnableRobot()")
        error_id, ret_val = self.await_reply()
        return error_id
 
    def disable(self) -> Optional[DobotError]:
        self.send_command("DisableRobot()")
        error_id, ret_val = self.await_reply()
        return error_id
    
    def reset(self) -> Optional[DobotError]:
        self.send_command("ResetRobot()")
        error_id, ret_val = self.await_reply()
        return error_id

    def clear_errors(self) -> Optional[DobotError]:
        self.send_command("ClearError()")
        error_id, ret_val = self.await_reply()
        return error_id

    def robot_mode(self) -> DobotError | RobotMode:
        self.send_command("RobotMode()")
        error_id, ret_val = self.await_reply()
        if error_id:
            return error_id
        else:
            # TODO: Handle this if error'd
            return RobotMode(int(ret_val))
    
 
    
class Feedback(DobotSocketConnection):
    def __init__(self, ip: str):
        super().__init__(ip, REALTIME_FEEDBACK_PORT)