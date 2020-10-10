# open_watchman

## installation
1. Prerequisites: python3, pip, virtualenv

2. Prepare the virtual environment:
```
    virtualenv local_env
    source local_env/bin/activate
    pip install -r requirements.txt
```

3. Set camera stream source in [main.py - line 8](https://github.com/mavixorg/open_watchman/blob/master/main.py#L8).
It can be equal to:
* an integer camera index (eg 0 for built-in laptop camera);
* video file path (if loading from);
* network stream URL;
* etc. check [OpenCV documentation](https://docs.opencv.org/4.4.0/d8/dfe/classcv_1_1VideoCapture.html#ac4107fb146a762454a8a87715d9b7c96) for more source options options.

4. Run 
```
python main.py
```