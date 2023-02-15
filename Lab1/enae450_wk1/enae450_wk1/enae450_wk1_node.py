#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class week1_node(Node): 
    def __init__(self):
        super().__init__("week1_node") 
        self.create_timer((1/5.), self.callback)

    def callback(self):
        self.get_logger().info("Hello World!")


def main(args=None):
    rclpy.init(args=args)
    node = week1_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
