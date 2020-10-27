#!/usr/bin/python3

import ast
import cv2
import time

from camera_stream import CameraStream
from object_detector import ObjectDetector

config_path = "local.conf"
config_file = open(config_path, "r")
config_dict = ast.literal_eval(config_file.read())

camera_stream = CameraStream(config_dict["camera_stream_path"])
camera_stream.start()

objdet = ObjectDetector(config_dict["detection_classes_path"], config_dict["model_path"])

while(camera_stream.isAlive()):
    ret, last_frame = camera_stream.getLastFrame()

    if(ret):
        cv2.imshow('open_watchman', objdet.detectAndPlot(last_frame, 0.4))
    
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

camera_stream.heyStopItNow()
camera_stream.join()
