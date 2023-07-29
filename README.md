## Ergonomic and type-hinted Python API for Dobot Products

A work-in-progress API, but with the goal of becoming the standard communication layer with Dobot Product's TCP-IP Protocol. 

The majority of the Dobot TCP-IP methods are renamed to adhere to snakecase formatting and increase readability.

Unique to this API, each method could potentially return an error, this allows for you to determine how errors should be handled in your implementation.

## How to use this API?

To use the API, just simply download the PyPi package through `pip install dobot-util`.

After installing the package, you can import the `Dobot` class and the `DobotError` type.

Its important to note that you need to switch your Dobot Robot into TCP-IP Development Mode in Remote Control settings otherwise it won't connect.

Once this is all configured, you can provide the IP of the robot on your local network and easily start a connection and issue commands from each component.

There are three components - Dashboard, Movement, and Feedback. Each of them have their own responsibility and their name explains their role well-enough.

For actual examples of the API being used in code, check the examples directory.