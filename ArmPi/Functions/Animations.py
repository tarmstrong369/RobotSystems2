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

def middle_stance(T): # En garde!
    servo1 = 510  # Gripper: 0-full open, 500-close
    servo2 = 500  # Wrist: 500-horizontal,
    servo3 = 450  # 500: straight out
    servo4 = 1000  # 500: straight out
    servo5 = 750  # 500: straight up
    servo6 = 500  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, T)
    Board.setBusServoPulse(2, servo2, T)
    Board.setBusServoPulse(3, servo3, T)
    Board.setBusServoPulse(4, servo4, T)
    Board.setBusServoPulse(5, servo5, T)
    Board.setBusServoPulse(6, servo6, T)

def high_blow(T): #sword raised high
    servo1 = 510  # Gripper: 0-full open, 500-close
    servo2 = 500  # Wrist: 500-horizontal,
    servo3 = 200  # 500: straight out
    servo4 = 500  # 500: straight out
    servo5 = 500  # 500: straight up
    servo6 = 500  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, T)
    Board.setBusServoPulse(2, servo2, T)
    Board.setBusServoPulse(3, servo3, T)
    Board.setBusServoPulse(4, servo4, T)
    Board.setBusServoPulse(5, servo5, T)
    Board.setBusServoPulse(6, servo6, T)

def low_strike(T): #sword down low
    servo1 = 510  # Gripper: 0-full open, 500-close
    servo2 = 500  # Wrist: 500-horizontal,
    servo3 = 750  # 500: straight out
    servo4 = 1000  # 500: straight out
    servo5 = 400  # 500: straight up
    servo6 = 500  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, T)
    Board.setBusServoPulse(2, servo2, T)
    Board.setBusServoPulse(3, servo3, T)
    Board.setBusServoPulse(4, servo4, T)
    Board.setBusServoPulse(5, servo5, T)
    Board.setBusServoPulse(6, servo6, T)

def from_the_right(T): # sword to the right
    servo1 = 510  # Gripper: 0-full open, 500-close
    servo2 = 300  # Wrist: 500-horizontal,
    servo3 = 450  # 500: straight out
    servo4 = 1000  # 500: straight out
    servo5 = 750  # 500: straight up
    servo6 = 750  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, T)
    Board.setBusServoPulse(2, servo2, T)
    Board.setBusServoPulse(3, servo3, T)
    Board.setBusServoPulse(4, servo4, T)
    Board.setBusServoPulse(5, servo5, T)
    Board.setBusServoPulse(6, servo6, T)

def from_the_left(T): # sword to the left
    servo1 = 510  # Gripper: 0-full open, 500-close
    servo2 = 750  # Wrist: 500-horizontal,
    servo3 = 450  # 500: straight out
    servo4 = 1000  # 500: straight out
    servo5 = 750  # 500: straight up
    servo6 = 250  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, T)
    Board.setBusServoPulse(2, servo2, T)
    Board.setBusServoPulse(3, servo3, T)
    Board.setBusServoPulse(4, servo4, T)
    Board.setBusServoPulse(5, servo5, T)
    Board.setBusServoPulse(6, servo6, T)
if __name__ == '__main__':
    arm_kinematics = ArmIK()
    t=1000
    s=1.5
    middle_stance(t)
    time.sleep(s)
    high_blow(t)
    time.sleep(s)
    low_strike(t)
    time.sleep(s)
    from_the_right(t)
    time.sleep(s)
    from_the_left(t)

