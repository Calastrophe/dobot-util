from util import DobotSocketConnection
from typing import Optional
from constants import *



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
        

class Dashboard(DobotSocketConnection):
    def __init__(self, ip: str):
        super().__init__(ip, DASHBOARD_PORT)
    
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
    
 
    
class Feedback(DobotSocketConnection):
    def __init__(self, ip: str):
        super().__init__(ip, REALTIME_FEEDBACK_PORT)