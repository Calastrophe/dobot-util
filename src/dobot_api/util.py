import socket
from typing import Optional, Tuple
from constants import DobotError

class DobotSocketConnection:
    def __init__(self, ip: str, port: int):
        self.socket = socket.socket()
        self.socket.connect((ip, port))

    "Sends a desired command over the socket connection"
    def send_command(self, cmd: str):
        encoded_cmd = cmd.encode("utf-8")
        self.socket.send(encoded_cmd)

    # This is a quick and easy solution, but may not cover all ErrorIDs.
    def await_reply(self) -> Tuple[Optional[DobotError], str]:
        data = self.socket.recv(1024)
        response: str = str(data, encoding="utf-8")
        split_response = response.split(",")
        errorID: int = int(split_response[0].strip())
        return_value: str = split_response[1].strip()
        if errorID == 0:
            return (None, return_value)
        else:
            # It will panic here if errorID is not impl'd
            return (DobotError(errorID), return_value)

        


     