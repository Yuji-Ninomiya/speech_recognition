#!/usr/bin/python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String


def callback(str):
    print 'Got callback!'
    rospy.loginfo(str.data)

    input = str.data
    print 'show input data'
    print(input)


def listener():
    rospy.init_node('listener', anonymous=False)
    rospy.Subscriber('/speech', String, callback)
    rospy.spin()

if __name__ == '__main__':

    listener()
    print 'end'

    
