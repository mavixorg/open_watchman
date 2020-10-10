#!/usr/bin/python3

import cv2
import numpy as np

from object_detector import ObjectDetector

objdet = ObjectDetector("coco_classes.txt", "ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/")

input_image = cv2.imread("boats_test.jpg")
cv2.imwrite("local_output.jpg", objdet.detectAndPlot(input_image))