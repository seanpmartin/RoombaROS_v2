#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import Int32MultiArray
#from __future__ import print_function
from pycreate2 import Create2
import time

def rangestate():

    port = '/dev/ttyUSB0'
    baud = {
        'default': 115200,
        'alt': 19200
    }
    bot = Create2(port=port, baud=baud['default'])
    bot.start()
    bot.full()
    pub = rospy.Publisher('sensor_msg', Int32MultiArray, queue_size=10)
    rospy.init_node('rangestate', anonymous=True)
    rate = rospy.Rate(1) # 10hz
    while not rospy.is_shutdown():
        sensor = bot.get_sensors()
	x = sensor[35]
	y = (int(x[0]),int(x[1]),int(x[2]),int(x[3]),int(x[4]),int(x[5]),)
	z = Int32MultiArray(data=y)
        #print(type(sensor.light_bumper))
        #state = "Sensors: %s" %str(sensor.light_bumper)
	#rospy.loginfo(z)
       	pub.publish(z)
	rate.sleep()

if __name__ == '__main__':
    try:
        rangestate()

    except rospy.ROSInterruptException:
        pass
