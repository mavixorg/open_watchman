# open_watchman

## installation
1. Prerequisites: python3, pip, virtualenv

2. Prepare the virtual environment:
```
    virtualenv local_env
    source local_env/bin/activate
```

3. Install requirements (~1.1 GB)
```
    pip install -r requirements.txt
```

requirements.txt includes the latest tensorflow library, which has many dependencies, hence the size. Following is a full list of dependencies that will be installed:

numpy, opencv-python, six, grpcio, google-pasta, astunparse, pyasn1, pyasn1-modules, rsa, cachetools, google-auth, chardet, certifi, idna, urllib3, requests, oauthlib, requests-oauthlib, google-auth-oauthlib, absl-py, protobuf, tensorboard-plugin-wit, werkzeug, zipp, importlib-metadata, markdown, tensorboard, h5py, keras-preprocessing, tensorflow-estimator, opt-einsum, gast, wrapt, termcolor, tensorflow

4. Download weights for a [pre-trained neural network](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz) (~300 MB) and extract them from the archive. Copy the resulting folder (named ssd_resnet50_v1_fpn_640x640_coco17_tpu-8) to the project root directory.

5. Run single image test script and check that it is executed without errors:
```
python single_image_test.py
```
The image with detected boats will be saved in a file "local_output.jpg". Check it out!

6. Set camera stream source in [main.py - line 8](https://github.com/mavixorg/open_watchman/blob/master/main.py#L8).
It can be equal to:
* an integer camera index (eg 0 for built-in laptop camera);
* video file path (if loading from);
* network stream URL;
* etc. check [OpenCV documentation](https://docs.opencv.org/4.4.0/d8/dfe/classcv_1_1VideoCapture.html#ac4107fb146a762454a8a87715d9b7c96) for more source options.

7. Run 
```
python main.py
```