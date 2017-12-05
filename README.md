# RoombaROS_v2
Project 4 Submission. Sean Martin, Alex Soussan, Brahima Fanny

This project consists of a ROS package which communicates with
a iRobot Create2 Roomba over a serial port USB connection from a Raspberry Pi3.

A publisher publishs the 6 IR range sensors (0=no object, 1=object)
and a subscriber takes these values and writes a corresponding left
and right wheel velocity value to the Roomba.

A node for navigation was added to RoombaROS_v2 to assign each motor a specific velocity when any configuration of the sensors are obstructed.

Thanks to the MomsFriendlyRobotCompany for their pycreate2 Python 
library, whose functions are used to drive the Roomba's sensors.
```
https://github.com/MomsFriendlyRobotCompany/pycreate2
```

## Intro
Things needed before starting:

iRobot Create 2:
http://www.irobot.com/About-iRobot/STEM/Create-2.aspx

Raspberry Pi 3:
https://www.amazon.com/CanaKit-Raspberry-Complete-Starter-Kit/dp/B01C6Q2GSY

=> flash fresh image of Ubuntu 16.04 LTS

ROS Kinetic:
http://wiki.ros.org/Installation/UbuntuARM

**Also visit http://wiki.ros.org for all things ROS related - like setting up packages and workspace**

Pycreate2 Python Package: 
https://pypi.python.org/pypi/pycreate2

## ROS
To download the package to Raspberry Pi 3, follow the below command line
steps. This will initialize a workspace called irobot
for Roomba ROS packages
```
### **Initialize Workspace**
mkdir ~/irobot/src
cd ~/irobot/src
catkin_init_workspace
cd ..
catkin_make

### **Create Package**
cd ~/irobot/src
git clone https://github.com/spm1200/RoombaROS_v2
cd ~/irobot
rosdep update
rosdep install --from-paths src -i -y
catkin_make
source ./devel/setup.bash
```

To ensure the USB connection will work on the Pi
run the below command
```
sudo usermod -a -G dialout $USER
```

To run the ROS package, three terminal windows are needed.
Run the commands shown for each 3 below.

Terminal 1 [run roscore]:
```
export ROS_MASTER_URI=http://[pi_ip_address]:11311
export ROS_IP=[pi_ip_address]
roscore
```

Terminal 2 [IR publisher]:
```
export ROS_MASTER_URI=http://[pi_ip_address]:11311
export ROS_IP=[pi_ip_address]
source devel/setup.bash
rosrun RoombaROS_v2  IR_pub.py
```
Terminal 3 [navigator pub/sub]:
```
export ROS_MASTER_URI=http://[pi_ip_address]:11311
export ROS_IP=[pi_ip_address]
source devel/setup.bash
rosrun RoombaROS_v2  navigator.py
```
Terminal 4 [wheel subscriber]:
```
export ROS_MASTER_URI=http://[pi_ip_address]:11311
export ROS_IP=[pi_ip_address]
source devel/setup.bash
rosrun RoombaROS_v2  wheel_sub.py
```


The flowchart below represents each ROS node and messages.

![ros nav](https://github.com/asoussan/markdown_images/blob/master/ros%20diagram.png)
