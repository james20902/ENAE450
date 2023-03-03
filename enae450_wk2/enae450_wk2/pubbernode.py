#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64


class publisher_test(Node): 
    message = None

    def __init__(self):
        super().__init__("number_publisher") 
        self.publisher = self.create_publisher(Int64, "number", 10)
        self.create_timer(1, self.publish)
        self.message = Int64()

    def publish(self):
        self.get_logger().info("published data")
        self.message.data = 449
        self.publisher.publish(self.message)

def main(args=None):
    rclpy.init(args=args)
    node = publisher_test()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
