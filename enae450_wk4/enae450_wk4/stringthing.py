#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StringPublisher(Node):

    def __init__(self):
        super().__init__("string_thing")
        self.declare_parameter("name", "James")
        self.declare_parameter("book", "The Art of War")
        self.publisher = self.create_publisher(String, "introduction", 10)
        self.publisher.publish(
            self.get_string(self.get_parameter("name").value,
                            self.get_parameter("book").value)
        )
        self.get_logger().info("publishing string!")

    
    def get_string(self, name, book):
        msg = String()
        msg.data = "Hi, my name is {} and my favorite book is {}."
        msg.data = msg.data.format(name, book)
        print(msg.data)
        return msg

def main(args=None):
    rclpy.init(args=args)

    stringpub = StringPublisher()

    rclpy.shutdown()


if __name__ == "__main__":
    main()
