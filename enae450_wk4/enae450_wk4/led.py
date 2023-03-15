#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from custom_interfaces.msg import LedPanelState
from custom_interfaces.srv import SetLedState
    
class LedPanel(Node):
    led_states = []
    message = LedPanelState()

    def __init__(self):
        super().__init__("led_panel")
        self.publisher = self.create_publisher(LedPanelState,
                                               "led_panel_state",
                                               10)
        self.declare_parameter("led_states", [0, 0, 1])
        self.led_states = self.get_parameter("led_states").value
        # regularly refresh the state, should only
        # be updated in 1 second intervals as per
        # battery updates
        self.create_timer(1, self.publish_state)
        self.create_service(SetLedState, "set_led", self.led_manager)

    def publish_state(self):
        self.message.states = self.led_states
        self.publisher.publish(self.message)

    def led_manager(self, request, response):
        try:
            # update led
            self.led_states[request.index] = int(request.state)
            
            response.success = True
            response.message = "changed successfully"
            self.get_logger().info("led state changed!")
        except(IndexError):
            # in case the led we want to change dont work
            response.success = False
            response.message = "led not found"
        print(self.led_states)
        return response


def main(args=None):
    rclpy.init(args=args)

    led = LedPanel()

    rclpy.spin(led)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
