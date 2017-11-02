#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import rospy
from message.msg import *

def talker():
    pub = rospy.Publisher('chatter', message, queue_size=10)
    rospy.init_node('Publisher', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        hello_str = message()
        hello_str.first_name = "xin"
        hello_str.last_name = "liu"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass