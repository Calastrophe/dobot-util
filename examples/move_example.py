from dobot_util import Dobot, DobotError

if __name__ == "__main__":
    # Provide the IP of the Dobot Robot, determine if you want to log or not - read other default arguments and determine what you want to change.
    robot = Dobot("192.168.1.6", logging = True)
    
    # Attempt to turn on the robot with the needed command, could fail - but we assume it works.
    robot.dashboard.enable()

    # This is a joint to joint move, so you provide the joint values you want to move to.
    # The amount of joints needed to pass depends on the robot model type.
    # For the case of an M1 Pro, it would need to be four floats.
    result = robot.movement.joint_to_joint_move([0.0, 0.0, 0.0, 0.0])

    # Any command provided through the API could potentially fail and return an error.
    # It is important to handle ALL cases, so handle errors - either through a function which takes an error and panics, or does something based on the error.
    if result:
        # There is an error, handle it.
        pass
    
    # If you've got this far, you didn't encounter an error or handled it.

    # This API subscribes to the idea that the USER should handle exceptions and not force their hand by raising exceptions, but it comes with the price of simple code being verbose and needing an error handling function.
    # In the future, there will be in-built handler functions on DobotError types to panic or raise exceptions easily, if wanted explicitly.


