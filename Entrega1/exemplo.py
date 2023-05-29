#!/usr/bin/env python3
import rclpy

from rclpy.node import Node
from geometry_msgs.msg import Twist


class TurtleController(Node):
    def __init__(self):
        super().__init__('turtle_controller')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 100)
        self.timer_ = self.create_timer(1, self.move_turtle)
        self.twist_msg_ = Twist()
        self.count = 0

    def move_turtle(self):
        print(self.count)
        self.count += 1 
        if self.count < 17:
            self.twist_msg_.linear.x = 1.2
            self.twist_msg_.angular.z = 0.5
        if  self.count >=17 and self.count<19:
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = 0.7
        if self.count >= 19 and self.count <=20:
            self.twist_msg_.angular.z = 0.0 
            self.twist_msg_.linear.x = 1.0
        if self.count > 20 and self.count < 26:
            self.twist_msg_.linear.x = 0.0
            self.twist_msg_.angular.z = 0.9 
        if self.count >=26 and self.count <=45:
            self.twist_msg_.linear.x = 0.3
            self.twist_msg_.angular.z = 0.5 
        if self.count > 45 and self.count <= 50:
            self.twist_msg_.angular.z = 0.9 
            self.twist_msg_.linear.x = 0.0 

        if self.count > 50 and self.count <=51:
            self.twist_msg_.angular.z = 0.0 
            self.twist_msg_.linear.x = 1.0 
        if self.count > 52: 
            self.twist_msg_.angular.z = 0.0 
            self.twist_msg_.linear.x = 0.0 



        self.publisher_.publish(self.twist_msg_)


def main(args=None):
    rclpy.init()
    turtle_controller = TurtleController()
    rclpy.spin(turtle_controller)
    turtle_controller.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
