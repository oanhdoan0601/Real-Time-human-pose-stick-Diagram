#--------------------------------------------------------------------#
# Date                                          : 10/20/2019         #
# Angle calculation, stick vector visualization : OD                 #
# Status                                         :reasearch purpose  #
#--------------------------------------------------------------------#

import threading
import time
import math
import cv2
from VideoGet import VideoGet
import multiprocessing as mp

# Behavior Detection Libraries
import settings
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from pose.estimator2 import TfPoseEstimator
from pose.networks import get_graph_path
from utils.sort import Sort
from utils.actions import actionPredictor
from utils.joint_preprocess import *
import sys


import os, signal
pid = os.getpid()
print("\n")
print("PID : ", pid)
print("\n")

cv2.namedWindow("Behavior_detection", cv2.WINDOW_NORMAL)
#select the appropriate Source
source = 0

# Start the dedicated thread for video grabbing.
video_getter = VideoGet(source).start()
#cap = cv2.VideoCapture("trimmed_assault.mp4")

global poseEstimator
poseEstimator = TfPoseEstimator(get_graph_path('mobilenet_thin'), target_size=(432, 368))

while True:
    frame = video_getter.frame
    #ret, frame = cap.read()
    frame = cv2.resize(frame, (settings.winWidth, settings.winHeight))
    humans = poseEstimator.inference(frame)
    frame = TfPoseEstimator.draw_humans(frame, humans, imgcopy=False) # Humans are plotted on the frame.
    cv2.imshow("Behavior_detection", frame)
        
    #cv2.waitKey(1)
    if cv2.waitKey(10)==ord('q'):
        video_getter.stop()
        break
        
#Destroy all windows while exiting
cv2.destroyAllWindows()
os.kill(pid, signal.SIGKILL)
    
    
    
