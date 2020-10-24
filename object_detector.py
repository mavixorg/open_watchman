#!/usr/bin/python3

import os
import ast
import numpy as np
import tensorflow as tf

from object_detection.utils import visualization_utils

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
        detections = self._detect(tf.convert_to_tensor(np.expand_dims(input_image, axis=0), dtype=tf.uint8))
        
        output_image = input_image.copy()
        
        visualization_utils.visualize_boxes_and_labels_on_image_array(
            output_image,
            detections['detection_boxes'][0].numpy(),
            detections['detection_classes'][0].numpy().astype(np.uint32),
            detections['detection_scores'][0].numpy(),
            self.category_index,
            use_normalized_coordinates=True,
            min_score_thresh=score_threshold)
        
        return output_image