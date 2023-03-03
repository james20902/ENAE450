#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from example_interfaces.srv import SetBool

class subscriber_test(Node): 
    counter = 0
    message = None

    def __init__(self):
        super().__init__("number_counter") 
        self.subscriber = self.create_subscription(
            Int64, "number", self.update_count, 10)
        self.publisher = self.create_publisher(
            Int64, "number_count", 10)
        self.message = Int64()
        self.create_service(SetBool, "reset_counter", self.reset_count)
    
    def update_count(self, data):
        self.get_logger().info(str(self.counter))
        self.counter += data.data
        self.message.data = self.counter
        self.publisher.publish(self.message) 
    
    def reset_count(self, request, response):
        if request.data:
            self.get_logger().info("reset request received")
            self.counter = 0
        response.success = True
        response.message = "poggers"
        return response


def main(args=None):
    rclpy.init(args=args)

    node = subscriber_test()

    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
