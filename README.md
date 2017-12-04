# RoombaROS_v2 ECE 422
Project 4 Submission. Sean Martin, Brahima Fanny, Alex Soussan

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

The following hardware is used: An iRobot Create2

A Raspberry Pi3 w/ Unbuntu 16.04 and ROS Kinetic installed.

To download to a Raspberry Pi follow the below command line
steps. This will initialize a workspace called irobot
for Roomba ROS packages
```
mkdir ~/irobot/src
cd ~/irobot/src
catkin_init_workspace
cd ..
catkin_make

cd ~/irobot/src
git clone https://github.com/spm1200/RoombaROS_v1
cd ~/irobot
rosdep update
rosdep install --from-paths src -i -y
catkin_make
source ./develop/setup.bash
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

Terminal 2 [run publisher]:
```
export ROS_MASTER_URI=http://[pi_ip_address]:11311
export ROS_IP=[pi_ip_address]
source develop/setup.bash
rosrun RoombaROS_v1  rangestate.py
```

Terminal 3 [run subscriber]:
```
export ROS_MASTER_URI=http://[pi_ip_address]:11311
export ROS_IP=[pi_ip_address]
source develop/setup.bash
rosrun RoombaROS_v1  listener.py
```

From here, the 6IR sensor states and 
wheel velocities will be displayed.

![ros nav](https://github.com/asoussan/markdown_images/blob/master/ros%20diagram.png)
