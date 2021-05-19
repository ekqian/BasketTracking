# BasketTracking

![](resources/logo_large.png "Logo")

Tactics and statistics in professional basketball teams are widespread. This operation can be optimized and speed up by
an automatic computer vision system. We aim at developing such system capable of action tracking and understanding in
basketball games using computer vision approaches and ideas alongside deep learning models such as Detectron2. Our
system tracks player trajectories from videos and rectifies them to a standard basketball court, showing also the player
who owns the ball.

## Table of Contents

* [Demo](#demo)
* [Dependencies](#dependencies)
* [Usage](#usage)

### Demo

<p align='center'>
  <img src="resources/demo.gif" width="80%"/>
</p>

### Dependencies

* [Python](https://www.python.org/)
* [OpenCV](https://opencv.org/)
* [Detectron2](https://github.com/facebookresearch/detectron2)
* [Pytorch-Cuda](https://pytorch.org/)
* [Numpy](https://numpy.org/)
* [Matplotlib](https://matplotlib.org/)

### Usage

The system can be executed from the ```main.py```.

* ```main.py```: Initializes classes and loads or rectifies the needed images
* ```video_handler.py```: Manages the frame reading procedure from the input video.
* ```rectify_court.py```: Produces homographies, rectified images, panoramas.
* ```ball_detect_track.py```: Detects and tracks the ball
* ```player_detection.py```: Detects and tracks the players
* ```player.py```: Contains the class ```Player```.
* ```tools```: Helper functions.
* ```resources```: Contains template images, input video.
