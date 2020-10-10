#!/usr/bin/python3

import os

import numpy as np
import tensorflow as tf

from object_detection.builders import model_builder
from object_detection.utils import config_util

class ObjectDetector:
    
    def __init__(self, model_dir, checkpoint_id=0):
        
        # Loading pipeline config
        model_config_file = os.path.join(model_dir, 'pipeline.config')
        checkpoint_path = os.path.join(model_dir, 'checkpoint/ckpt-' + str(checkpoint_id))
        pipeline_config = config_util.get_configs_from_pipeline_file(model_config_file)

        # Building detection model
        self._detection_model = model_builder.build(
            model_config=pipeline_config['model'], is_training=False)

        # Restoring checkpoint
        ckpt = tf.compat.v2.train.Checkpoint(
            model=self._detection_model)
        ckpt.restore(checkpoint_path).expect_partial()

        # Initializaing object detection tf.function
        self._detect = self._getDetectionFunction()

    def _getDetectionFunction(self):
        @tf.function
        def detectFn(input_tensor):
            """
            input_tensor: A [1, height, width, 3] Tensor of type tf.float32.
            Returns a dict containing 3 Tensors: `detection_boxes`, `detection_classes`, and `detection_scores`.
            """
            preprocessed_image, shapes = self._detection_model.preprocess(input_tensor)
            prediction_dict = self._detection_model.predict(preprocessed_image, shapes)
            return self._detection_model.postprocess(prediction_dict, shapes)
        return detectFn

    def getDetectionsFromImage(self, input_image):
        """
        input_image: numpy array of uint8 with shape [img_height, img_width, 3]
        (img_height and img_width can be arbitrary).
        Note, however, that input_image will be resized to 640x640 by detector.
        """
        return self._detect(tf.convert_to_tensor(np.expand_dims(input_image, axis=0), dtype=tf.float32))