#!/usr/bin/python3

import numpy as np

from object_detector import ObjectDetector

objdet = ObjectDetector("ssd_resnet50_v1_fpn_640x640_coco17_tpu-8/")

input_image = np.zeros((640, 640, 3))
detections = objdet.getDetectionsFromImage(input_image)
print(detections)