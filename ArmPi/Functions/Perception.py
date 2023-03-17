#!/usr/bin/python3
# coding=utf8
import sys
sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import numpy as np
import Camera
import threading
from LABConfig import *
from ArmIK.Transform import *
from ArmIK.ArmMoveIK import *
import HiwonderSDK.Board as Board
from CameraCalibration.CalibrationConfig import *
import rossros as rr
import concurrent.futures
import random
import math


def MaxContour( contours):
    """ Find the contour with the largest area
    parameter is list of contours to compare"""
    contour_area_temp = 0
    contour_area_max = 0
    area_max_contour = None

    # iterate over all contours
    for c in contours:
        contour_area_temp = math.fabs(cv2.contourArea(c))  # Calculate area of contour
        if contour_area_temp > contour_area_max:
            contour_area_max = contour_area_temp
            if contour_area_temp > 2500:  # Only when the area > 2500, the contour of the largest area is valid to filter interference
                area_max_contour = c

    return area_max_contour, contour_area_max  # returns largest contour

def Contours(msg):
    print('Thread: Camera Interpreting...')

    task = msg

    frame_lab = filter(task.frame_gb)

    area_max = 0
    areaMaxContour = 0
    if not task.start_pick_up:
        for i in color_range:  # color range comes from LABconfig.py
            if i in task.target_color:
                detect_color = i

                # Perform bitwise operations on original image and mask
                frame_mask = cv2.inRange(frame_lab, color_range[detect_color][0], color_range[detect_color][1])
                # Open Operation
                opened = cv2.morphologyEx(frame_mask, cv2.MORPH_OPEN, np.ones((6, 6), np.uint8))
                # Close Operation
                closed = cv2.morphologyEx(opened, cv2.MORPH_CLOSE, np.ones((6, 6), np.uint8))
                # Find the outline
                contours = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
                # Find the largest contour
                areaMaxContour, area_max = MaxContour(contours)