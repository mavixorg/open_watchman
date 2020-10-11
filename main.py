#!/usr/bin/python3

import cv2
import time

from camera_stream import CameraStream
from object_detector import ObjectDetector

#camera_stream = CameraStream('rtsp://192.168.1.119/user=admin_password=_channel=1_stream=0.sdp')
camera_stream = CameraStream(0)
camera_stream.start()

objdet = ObjectDetector("coco_classes.txt", "ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/")

while(camera_stream.isAlive()):
    ret, last_frame = camera_stream.getLastFrame()

    if(ret):
        cv2.imshow('open_watchman', objdet.detectAndPlot(last_frame, 0.4))

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

camera_stream.heyStopItNow()
camera_stream.join()
