#!/usr/bin/python3

import ast
import os
import time

import cv2
import numpy as np
import tensorflow as tf

class ObjectDetector:
    
    def __init__(self, categories_path, model_dir):
        
        self.category_index = self._load_category_index(categories_path)

        # Initializaing object detection tf.function
        self._detect = tf.saved_model.load(os.path.join(model_dir, "saved_model"))

    def _load_category_index(self, path):
        f = open(path, "r")
        classes_dict = ast.literal_eval(f.read())
        category_index = {}
        for class_id, class_name in classes_dict.items():
            category_index[class_id] = {'id': class_id, 'name': class_name}
        return category_index

    def detectAndPlot(self, input_image, score_threshold=0.52):
        """
        input_image: numpy array of uint8 with shape [img_height, img_width, 3]
        (img_height and img_width can be arbitrary).
        Note, however, that input_image will be resized to 640x640 by detector.
        """
        start_time = time.time()
        detections = self._detect(tf.convert_to_tensor(np.expand_dims(input_image, axis=0), dtype=tf.uint8))
        
        output_image = input_image.copy()
        h, w = output_image.shape[:2]

        bboxes = detections['detection_boxes'][0].numpy()
        classes = detections['detection_classes'][0].numpy().astype(np.uint32)
        scores = detections['detection_scores'][0].numpy()

        for detection_id in range(len(scores)):
            if(scores[detection_id] < score_threshold):
                continue

            bbox = bboxes[detection_id]
            bbox_px = [int(x) for x in [bbox[0]*h, bbox[1]*w, bbox[2]*h, bbox[3]*w]]
            cv2.rectangle(output_image, (bbox_px[1], bbox_px[0]), (bbox_px[3], bbox_px[2]), (0, 255, 0), 3)

            class_id = classes[detection_id]
            class_name = self.category_index[class_id]["name"]

            annotation = class_name + " " + str(int(scores[detection_id]*100.0)) + "%"
            cv2.putText(output_image, annotation,
                (bbox_px[1], bbox_px[0]+10), 
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (255, 0, 0), 2, cv2.LINE_AA)
        
        elapsed_time = time.time() - start_time
        cv2.putText(output_image, str(elapsed_time)[:5] + " s/frame",
            (20, 20), 
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7, (0, 255, 0), 2, cv2.LINE_AA)

        return output_image