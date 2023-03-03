#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class week1_node(Node): 
    def __init__(self):
        super().__init__("week1_node") 
        self.get_logger().info("This is a running node!")

def main(args=None):
    rclpy.init(args=args)
    node = week1_node()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
