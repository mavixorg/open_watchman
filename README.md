# open_watchman

## installation
1. Prerequisites: python3, pip, virtualenv

2. Prepare the virtual environment:
```
    virtualenv local_env
    source local_env/bin/activate
```

3. Install requirements (~1.5 GB)
```
    pip install -r requirements.txt
```

Note about size: object_detection_api is an open-source library maintained by Google's researchers, and has many dependencies. Not all of them are truly necessary for this project, so an attempt to clean the dependencies may be made in the future. Currently, here are the requirements that will be installed:

numpy, opencv-python, pillow, six, protobuf, tensorflow-hub, absl-py, tf-slim, opencv-python-headless, httplib2, pyasn1, pyasn1-modules, rsa, cachetools, google-auth, google-auth-httplib2, googleapis-common-protos, pytz, certifi, chardet, idna, urllib3, requests, google-api-core, uritemplate, google-api-python-client, tensorflow-estimator, zipp, importlib-metadata, markdown, werkzeug, grpcio, tensorboard-plugin-wit, oauthlib, requests-oauthlib, google-auth-oauthlib, tensorboard, astunparse, termcolor, gast, google-pasta, keras-preprocessing, h5py, opt-einsum, wrapt, tensorflow, sentencepiece, Cython, typeguard, tensorflow-addons, scipy, pyparsing, python-dateutil, cycler, kiwisolver, matplotlib, gin-config, py-cpuinfo, dm-tree, dill, importlib-resources, tensorflow-metadata, future, promise, tqdm, attrs, tensorflow-datasets, pandas, psutil, text-unidecode, python-slugify, slugify, kaggle, dataclasses, tensorflow-model-optimization, pyyaml, proto-plus, google-cloud-core, pycparser, cffi, google-crc32c, google-resumable-media, google-cloud-bigquery, tf-models-official, pymongo, oauth2client, docopt, hdfs, typing-extensions, avro-python3, pydot, fastavro, pbr, mock, crcmod, pyarrow, apache-beam, pycocotools, lxml, contextlib2, object-detection

4. Download weights for a [pre-trained neural network](http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet50_v1_fpn_640x640_coco17_tpu-8.tar.gz) (~300 MB) and extract them from the archive. Copy the resulting folder (named ssd_resnet50_v1_fpn_640x640_coco17_tpu-8) to the project root directory.

5. Run single image test script and check that it is executed without errors:
```
python single_image_test.py
```

6. Set camera stream source in [main.py - line 8](https://github.com/mavixorg/open_watchman/blob/master/main.py#L8).
It can be equal to:
* an integer camera index (eg 0 for built-in laptop camera);
* video file path (if loading from);
* network stream URL;
* etc. check [OpenCV documentation](https://docs.opencv.org/4.4.0/d8/dfe/classcv_1_1VideoCapture.html#ac4107fb146a762454a8a87715d9b7c96) for more source options options.

7. Run 
```
python main.py
```