#!/usr/bin/python3

import cv2
import time

from camera_stream import CameraStream

camera_stream = CameraStream('rtsp://192.168.1.119/user=admin_password=_channel=1_stream=0.sdp')

camera_stream.start()
time.sleep(2)

while(camera_stream.isAlive()):
    ret, last_frame = camera_stream.getLastFrame()

    if(ret):
        height, width = last_frame.shape[:2]
        resized_frame = cv2.resize(last_frame,(int(width/2), int(height/2)), interpolation = cv2.INTER_CUBIC)
        
        cv2.imshow('open_watchman', resized_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

camera_stream.heyStopItNow()
camera_stream.join()
