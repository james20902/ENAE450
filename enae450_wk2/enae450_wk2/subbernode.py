#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64

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
    
    def update_count(self, data):
        self.get_logger().info(str(self.counter))
        self.counter += data.data
        self.message.data = self.counter
        self.publisher.publish(self.message)


def main(args=None):
    rclpy.init(args=args)
    node = subscriber_test()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
