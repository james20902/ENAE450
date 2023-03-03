#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64
from example_interfaces.srv import AddTwoInts

class fib(Node): 

    client = None

    def __init__(self):
        super().__init__("fibonacci") 
        self.create_service(AddTwoInts, "add_ints", self.add)
        self.client = self.create_client(AddTwoInts, "add_ints")
    
    
    def add(self, request, response):
        response.sum = request.a + request.b
        return response


def main(args=None):
    previous = 0
    current = 1

    print(0)
    print(1)

    rclpy.init(args=args)

    node = fib()
    request = AddTwoInts.Request()

    for x in range(10):
        request.a = previous
        request.b = current
        
        future = node.client.call_async(request)
        rclpy.spin_until_future_complete(node, future)
        
        previous = current
        current = future.result().sum
        print(current)


    rclpy.shutdown()


if __name__ == "__main__":
    main()
