#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def move_square():
    # Inicializa o nó
    rospy.init_node('move_square_turtle', anonymous=True)

    # Inicializa o publisher para enviar comandos de movimento
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    # Define a velocidade linear (3 unidades por segundo)
    vel_msg.linear.x = 3.0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0

    # Gire a tartaruga em 90 graus (1,57 radianos)
    vel_msg.angular.z = 1.57

    # Tempo para a tartaruga se mover em linha reta (1 segundo)
    move_time = 1.0

    # Tempo para a tartaruga girar 90 graus
    rotate_time = 1.57

    for _ in range(4):  # Repita 4 vezes para formar o quadrado
        # Move para a frente
        start_time = rospy.Time.now()
        while (rospy.Time.now() - start_time).to_sec() < move_time:
            velocity_publisher.publish(vel_msg)
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

        # Gire 90 graus
        start_time = rospy.Time.now()
        while (rospy.Time.now() - start_time).to_sec() < rotate_time:
            velocity_publisher.publish(vel_msg)
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

    # Encerra o nó do ROS
    rospy.spin()

if __name__ == '__main__':
    try:
        move_square()
    except rospy.ROSInterruptException:
        pass
