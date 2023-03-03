#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool

def main(args=None):
    rclpy.init(args=args)

    node = Node("number_resetter")
    cli = node.create_client(SetBool, "reset_counter")

    while not cli.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('service not available, waiting again...')
    
    request = SetBool.Request()
    request.data = True
    
    future = cli.call_async(request)
    rclpy.spin_until_future_complete(node, future)
    
    node.get_logger().info('request sent, dying')
    rclpy.shutdown()

if __name__ == "__main__":
    main()