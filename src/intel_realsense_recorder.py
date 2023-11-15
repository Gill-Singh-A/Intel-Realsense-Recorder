#!/usr/bin/env python3

import rospy, cv2
from pathlib import Path
from datetime import date
from cv_bridge import CvBridge
from optparse import OptionParser
from sensor_msgs.msg import Image
from time import strftime, localtime, time

bridge = CvBridge()

folder_name = f"{date.today()} {strftime('%H_%M_%S', localtime())}"
image, image_count = None, 0

def get_arguments(*args):
    parser = OptionParser()
    for arg in args:
        parser.add_option(arg[0], arg[1], dest=arg[2], help=arg[3])
    return parser.parse_args()[0]

def getImage(ros_image):
    global image, image_count
    image = cv2.cvtColor(bridge.imgmsg_to_cv2(ros_image), cv2.COLOR_RGB2BGR)
    image_count += 1
    cv2.imwrite(f"{folder_name}/{date.today()}{strftime('%H%M%S', localtime())}_{image_count}.jpg", image)

def makeFolders():
    cwd = Path.cwd()
    video_folder = cwd / folder_name
    video_folder.mkdir()

if __name__ == "__main__":
    data = get_arguments(('-f', "--folder", "folder", "Name of the Folder for the Camera Feed Frames to be dumped (default=current data and time)"))
    if data.folder:
        folder_name = data.folder
    makeFolders()
    rospy.init_node("intel_realsense_recorder")
    rate = rospy.Rate(10)
    image_subscriber = rospy.Subscriber("/camera/color/image_raw", Image, getImage)
    t0 = time()
    while not rospy.is_shutdown():
        t1 = time()
        print(f"\rFrames = {image_count/(t1-t0):.2f}", end='')
    t2 = time()
    print(f"\nFrames Captured = {image_count}\nTotal Time = {t2-t0:.2f} seconds\nAverage FPS = {image_count/(t2-t0):.2f}")