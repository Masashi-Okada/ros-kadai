#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1) 
rate = rospy.Rate(1)
n = 0
while not rospy.is_shutdown():
    if  n <20:
        n +=1
    elif n >=20:
        n = 0
    pub.publish(n)
    rate.sleep()

