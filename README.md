# Real-Time-human-pose-stick-Diagram
Real time human pose with stick diagram, calulate all stick angles, and visualize all angle in the same coorditnate to analyze Human action prediction research
Continute research on Action prediction, after estimate the human pose estimation (Work have done as below). 
This project try to improve the accuracy of joints confidence map (TODO LIST: Use Mask-RCNN)
Caluate all stick angle and visualize them on real-time to reseach on change on stick angle in each actions, 
visualize all stick vectors in the same co0ordinate on real-time to analyze how busy and complicated sticks are. 
NEXT STEP: Human action recognition, High risk behaviour

Thanks for previous works as below:
# Real-Time-Action-Recognition

Real-time pose estimation and action recognition

Openpose weight file is collected from [tf-pose-estimation](https://github.com/ildoonet/tf-pose-estimation), thank for [ildoonet](https://github.com/ildoonet)'s awesome work.

## Old version

Old version detects person using SSD then classify images.

The old version is in [old branch](https://github.com/TianzhongSong/Real-Time-Action-Recognition/tree/old)

## requirements

Using [Anaconda](https://www.anaconda.com/download/) is recommended.

opencv

    pip install opencv-python

tensorflow1.3

    pip install tensorflow-gpu==1.3.0

filterpy

    pip install filterpy

## usage

    python run.py

## results

### pose estimation

[tf-pose-estimation](https://github.com/ildoonet/tf-pose-estimation)

![pose1](https://github.com/TianzhongSong/Real-Time-Action-Recognition/blob/master/files/pose1.gif)

![pose2](https://github.com/TianzhongSong/Real-Time-Action-Recognition/blob/master/files/pose2.gif)

### multi-person tracking

Using [sort](https://github.com/abewley/sort) to track person.

![track1](https://github.com/TianzhongSong/Real-Time-Action-Recognition/blob/master/files/track1.gif)

![track2](https://github.com/TianzhongSong/Real-Time-Action-Recognition/blob/master/files/track2.gif)

### action recognition

![action1](https://github.com/TianzhongSong/Real-Time-Action-Recognition/blob/master/files/action1.gif)

![action2](https://github.com/TianzhongSong/Real-Time-Action-Recognition/blob/master/files/action2.gif)

## reference

[tf-pose-estimation](https://github.com/ildoonet/tf-pose-estimation)

[sort](https://github.com/abewley/sort)
