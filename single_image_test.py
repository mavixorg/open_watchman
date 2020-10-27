#!/usr/bin/python3

import ast
import cv2
import numpy as np

from object_detector import ObjectDetector

config_path = "local.conf"
config_file = open(config_path, "r")
config_dict = ast.literal_eval(config_file.read())

objdet = ObjectDetector(config_dict["detection_classes_path"], config_dict["model_path"])

input_image = cv2.imread("boats_test.jpg")
cv2.imwrite("local_output.jpg", objdet.detectAndPlot(input_image))