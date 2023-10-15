#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_turtle():
    rospy.init_node('turtle_square_publisher', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)  # 1Hz

    while not rospy.is_shutdown():
        # Mova a tartaruga para a frente
        move_forward(pub)
        rospy.sleep(2)  # Espere por 2 segundos

        # Pare a tartaruga
        stop_turtle(pub)
        rospy.sleep(1)  # Espere por 1 segundo

        # Gire a tartaruga
        turn_turtle(pub)
        rospy.sleep(2)  # Espere por 2 segundos

        # Pare a tartaruga
        stop_turtle(pub)
        rospy.sleep(1)  # Espere por 1 segundo

def move_forward(pub):
    twist = Twist()
    twist.linear.x = 3.0
    pub.publish(twist)

def stop_turtle(pub):
    twist = Twist()
    pub.publish(twist)

def turn_turtle(pub):
    twist = Twist()
    twist.angular.z = 1.56
    pub.publish(twist)

if __name__ == '__main__':
    try:
        move_turtle()
    except rospy.ROSInterruptException:
        pass

