#! /usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from tf_transformations import euler_from_quaternion
from math import atan2
from collections import deque
MAX_DIFF = 0.1
goals = [(0.3, 2.0),
         (0.8, 5.0),
         (0.4, 0.0),
         ]


class Fila(list):
    def __init__(self, fila):
        super().__init__(item for item in fila)

    def enqueue(self, x):
        super().append(x)

    def dequeue(self):
        return super().pop(0)


fila = Fila([])


class TurtleController(Node):
    def __init__(self, fila):
        super().__init__('subscriber_node')
        self.x, self.y, self.theta = 0.0, 0.0, 0.0
        self.point = 0
        self.point_list = fila

        self.publisher = self.create_publisher(
            msg_type=Twist,
            topic='/cmd_vel',
            qos_profile=10)

        self.subscription = self.create_subscription(
            msg_type=Odometry,
            topic='/odom',
            callback=self.get_position,
            qos_profile=4)

        self.timer = self.create_timer(
            timer_period_sec=0.02,
            callback=self.Segue_ponto)

    def get_position(self, msg):
        self.x = msg.pose.pose.position.x
        self.y = msg.pose.pose.position.y
        rot = msg.pose.pose.orientation
        _, _, self.theta = euler_from_quaternion([rot.x, rot.y, rot.z, rot.w])
        self.get_logger().info(f"x={self.x:3f}, y={self.y:3f}")

    def Segue_ponto(self):
        ponto = Point()
        ponto.x = self.point_list[self.point][0]
        ponto.y = self.point_list[self.point][1]

        inc_x = ponto.x - self.x
        inc_y = ponto.y - self.y
        angulo_ponto = atan2(inc_y, inc_x)

        speed = Twist()

        if (abs(inc_x) < MAX_DIFF and abs(inc_y) < MAX_DIFF):
            fila.dequeue()
            print(fila)
            if fila == []:
                speed.linear.x = 0.0
                exit()

        if abs(angulo_ponto - self.theta) > MAX_DIFF:
            speed.linear.x = 0.0
            speed.angular.z = 0.3 if (
                angulo_ponto - self.theta) > 0.0 else -0.3
        else:
            speed.linear.x = 0.5
            speed.angular.z = 0.0
        self.publisher.publish(speed)


def main(args=None):

    rclpy.init(args=args)
    for goal in goals:
        fila.enqueue(goal)
        print(fila)
    subscriber_node = TurtleController(fila)
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
