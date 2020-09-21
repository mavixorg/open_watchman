#!/usr/bin/python3

import cv2
import threading

class CameraStream (threading.Thread):
    def __init__(self, stream_address):
        threading.Thread.__init__(self)
        self._stream_address = stream_address
        self._frame_available = False
        self._frame_lock = threading.Lock()
        self._last_frame = 0
        self._stop_requested = False

    def run(self):
        print("starting camera stream")
        input_capture = cv2.VideoCapture(self._stream_address)
        
        while(not self._stop_requested):
            if(not input_capture.isOpened()):
                print("camera stream not opened. Terminating")
                break
            ret, new_frame = input_capture.read()
            if(ret):
                self._frame_lock.acquire()
                self._last_frame = new_frame.copy()
                self._frame_available = True
                self._frame_lock.release()

        print("ending camera stream")
        input_capture.release()

    def getLastFrame(self):
        last_frame = 0
        self._frame_lock.acquire()
        frame_available = self._frame_available
        if(frame_available):
            last_frame = self._last_frame.copy()
        self._frame_lock.release()
        return (frame_available, last_frame)

    def heyStopItNow(self):
        self._stop_requested = True
