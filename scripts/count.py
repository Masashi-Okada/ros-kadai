#!/usr/bin/env python3
#BSD 3-Clause License
#*Copyright(c) 2022 Ryuichi Ueda & Masashi Okada.All right reserved.

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

