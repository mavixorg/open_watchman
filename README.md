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

4. Download weights for a [pre-trained neural network](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_640x640_coco17_tpu-8.tar.gz) (~20 MB) and extract them from the archive.

5. Create a file "local.conf" in the project root directory and copy contents of "sample.config" to it.

6. Update the value of "model_path" in local.conf to the path where neural network weights were extracted.

7. Run single image test script and check that it is executed without errors:
```
python single_image_test.py
```
The image with detected boats will be saved in a file "local_output.jpg". Check it out!

8. Update the value of "camera_stream_path" in local.conf.
It can be equal to:
* an integer camera index (eg 0 for built-in laptop camera);
* video file path (if loading from);
* network stream URL;
* etc. check [OpenCV documentation](https://docs.opencv.org/4.4.0/d8/dfe/classcv_1_1VideoCapture.html#ac4107fb146a762454a8a87715d9b7c96) for more source options.

9. Run 
```
python main.py
```