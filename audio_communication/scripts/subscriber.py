#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import rospy
from message.msg import *

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "First name is: %s", data.first_name)
    rospy.loginfo(rospy.get_caller_id() + "Last name is: %s", data.last_name)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('Subscriber', anonymous=True)

    rospy.Subscriber("chatter", message, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()