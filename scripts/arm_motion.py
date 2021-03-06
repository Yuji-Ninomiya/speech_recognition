#!/usr/bin/env python

import serial
import time
import numpy as np
import math as m

import time

import rospy
#from sensor_msgs.msg import JointState
#from std_msgs.msg import String


interval = 2.0

def init_arm(board):

    board.write("#0 P1500 T2000\r")
    board.write("#1 P1720 T2000\r")
    board.write("#2 P660 T2000\r")
    board.write("#3 P2200 T2000\r")
    board.write("#4 P800 T2000\r")

    ok = 1

    return ok

def move_to_grasp():

    #move to object
    ssc32.write("#0 P1500 T1000\r")
    ssc32.write("#1 P1000 T1000\r")
    ssc32.write("#2 P800 T1000\r")
    ssc32.write("#3 P2200 T1000\r")
    ssc32.write("#4 P800 T1000\r")

    print "Successed 'move to grasp'"
    time.sleep(interval)

def grasp():

    #catching
    ssc32.write("#0 P1500 T1000\r")
    ssc32.write("#1 P1000 T1000\r")
    ssc32.write("#2 P800 T1000\r")
    ssc32.write("#3 P2200 T1000\r")
    ssc32.write("#4 P1500 T1000\r")

    print "Successed 'grasp'"
    time.sleep(interval)

def turn_back_ini():

    #return to initial position

    ssc32.write("#0 P1500 T1500\r")
    ssc32.write("#1 P1720 T1500\r")
    ssc32.write("#2 P660 T1500\r")
    ssc32.write("#3 P2200 T1500\r")
    ssc32.write("#4 P1500 T1500\r")

    print "'return to initial position'"
    time.sleep(interval)

def turn_right():

    #turn right

    ssc32.write("#0 P1800 T1000\r")
    ssc32.write("#1 P1720 T1000\r")
    ssc32.write("#2 P660 T1000\r")
    ssc32.write("#3 P2200 T1000\r")
    ssc32.write("#4 P1500 T1000\r")

    print "'turn right"
    time.sleep(interval)

def turn_left():

    #turn left

    ssc32.write("#0 P1200 T1000\r")
    ssc32.write("#1 P1720 T1000\r")
    ssc32.write("#2 P660 T1000\r")
    ssc32.write("#3 P2200 T1000\r")
    ssc32.write("#4 P1500 T1000\r")

    print "'turn left"
    time.sleep(interval)

def move_to_put():

    #move to put space
    ssc32.write("#0 P1200 T1000\r")
    ssc32.write("#1 P800 T1000\r")
    ssc32.write("#2 P1200 T1000\r")
    ssc32.write("#3 P2200 T1000\r")
    ssc32.write("#4 P1500 T1000\r")

    print "'move to put'"
    time.sleep(interval)

def put():

    #put the object
    ssc32.write("#0 P1200 T1000\r")
    ssc32.write("#1 P800 T1000\r")
    ssc32.write("#2 P1200 T1000\r")
    ssc32.write("#3 P2200 T1000\r")
    ssc32.write("#4 P800 T1000\r")

    print "'put'"
    time.sleep(interval)


if __name__ == '__main__':

    ssc32 = serial.Serial('/dev/rfcomm0', 115200);

    print "connected. press '0 + Enter' to move the arm: "
    init_bottun = raw_input('>>>  ')

    if init_bottun == '0':

        init_arm(ssc32)

        print "Ok"
        time.sleep(1.5)


        print "input motion number."
        print "1: move to grasp, 2: grasp, 3: turn right, 4: turn left,"
        print "5: move to put, 6: put, 7: return to initial position"

        for i in range(7):

            mode_serect = raw_input('Input command >>>  ')

            if mode_serect == '1':
                move_to_grasp()

            elif mode_serect == '2':
                grasp()

            elif mode_serect == '3':
                turn_right()

            elif mode_serect == '4':
                turn_left()

            elif mode_serect == '5':
                move_to_put()

            elif mode_serect == '6':
                put()

            elif mode_serect == '7':
                turn_back_ini()

     else:
        print "Operation canceled"

    ssc32.close()
