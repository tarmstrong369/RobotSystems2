#!/usr/bin/python3
# coding=utf8
import sys

sys.path.append('/home/pi/ArmPi/')
import cv2
import time
import Camera
import threading
from LABConfig import *
from ArmIK.Transform import *
from ArmIK.ArmMoveIK import *
import HiwonderSDK.Board as Board
from CameraCalibration.CalibrationConfig import *

def opp_ang(rotation_angle):
    world_X, world_Y = 0, 0
    world_x, world_y = 0, 0
    print(rotation_angle)
    oldservo2_angle = getAngle(world_X, world_Y, rotation_angle)
    servo2_angle=-1*(oldservo2_angle-1000)
    Board.setBusServoPulse(2, servo2_angle, 500)
    time.sleep(0.8)