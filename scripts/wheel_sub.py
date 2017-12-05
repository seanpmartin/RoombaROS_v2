#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray
from pycreate2 import Create2
import time

def callback(data):
    v_left = data.data[0]
    v_right = data.data[1]
    bot.drive_direct(v_left,v_right)
    v=[v_left,v_right]
    rospy.loginfo(data.data)
    rospy.loginfo(v)
    time.sleep(0.01)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("nav_msg", Int32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    port = '/dev/ttyUSB0'
    baud = {
        'default': 115200,
        'alt': 19200
    }
    bot = Create2(port=port, baud=baud['default'])
    listener()
