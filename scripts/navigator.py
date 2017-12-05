#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32MultiArray

def publish_wheel(data):
    pub = rospy.Publisher('nav_msg', Int32MultiArray, queue_size=10)
    rate = rospy.Rate(1) # 10hz
    top = 200 #0 to 500
    #control logic below
    #
    rospy.loginfo("I receive %s", data.data)
    left = 0
    right = 0
    if (data.data[0]==1):
        # need to turn right
        left=-0.2*top
        right=0.4*top
    elif (data.data[1]==1):
        # need to turn left
        left=-0.4*top
        right=0.6*top
    elif (data.data[3]==1):
        # need to turn left
        left=-0.4*top
        right=0.4*top
    elif (data.data[4]==1):
        # need to turn left
        left=0.4*top
        right=-0.4*top
    elif (data.data[5]==1):
        # need to turn left
        left=0.4*top
        right=-0.2*top
    else:
        left=0.2*top
        right=0.2*top

    speeds = [left,right]
    rospy.loginfo(speeds)
    z = Int32MultiArray(data=speeds)
    pub.publish(z)
    rate.sleep()

#define the subscriber
#
def navigation():
    rospy.init_node('navigator')
    rospy.Subscriber('sensor_msg', Int32MultiArray, publish_wheel)
    rospy.spin()

if __name__=='__main__':
    navigation()

