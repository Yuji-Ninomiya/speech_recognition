#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String



def callback(str):
    rospy.loginfo(std)


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('/speech', String, callback)
    rospy.spin()

if __name__ == '__main__':

    listener()
    
