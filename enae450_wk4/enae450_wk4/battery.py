#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from custom_interfaces.srv import SetLedState

class Battery(Node): 
    
    battery_discharging = True
    battery_state = 1.
    
    state_request = SetLedState.Request()
    state_request.index = 0

    def __init__(self):
        super().__init__("battery") 
        self.create_timer(1, self.handle_logic)
        self.client = self.create_client(SetLedState, "set_led")
    
    def handle_logic(self):
        
        # we run this every second
        # so increment/decrement depending on which
        # way we're going
        if self.battery_discharging:
            self.battery_state -= (1/4.)
        else:
            self.battery_state += (1/6.)

        print(self.battery_state)

        # because precision
        if self.battery_state <= .01:
            # empty
            self.battery_state = 0
            self.battery_discharging = False
            # send request to power on
            self.state_request.state = True
            self.client.call_async(self.state_request)
            self.get_logger().info("client requests on!")

        if self.battery_state >= .99:
            # full
            self.battery_state = 1
            self.battery_discharging = True
            # send request to power off
            self.state_request.state = False
            self.client.call_async(self.state_request)
            self.get_logger().info("client requests off!")

def main(args=None):
    rclpy.init(args=args)

    bat = Battery()

    rclpy.spin(bat)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
