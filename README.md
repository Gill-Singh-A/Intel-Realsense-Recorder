# Intel Realsense Recorder
Recording Camera Feed using Intel Realsense Camera

## Requirements
Language Used = Python3<br />
Modules/Packages used:
* rospy
* cv2
* pathlib
* cv_bridge
* optparse
* sensor_msgs
* time

### intel_realsense_recorder.py
It is the python program located in the *src* folder that records the Camera Feed. <br />
It takes the frames from the Camera and saves them in the folder with the name depending upon the command line arguments provided by the user and in the format **{Current_Date_and_Time}_{Frame_Index}.jpg**. <br />
It takes the following command line arguments:
* '-f', "--folder" : Name of the Folder for the Camera Feed Frames to be dumped (default=current data and time)