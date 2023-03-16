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

# class Motion():
#     def __init__(self, AK):
#         self.AK = AK

#     def move()

def middle_stance(): # En garde!
    servo1 = 550  # Gripper: 0-full open, 500-close
    servo2 = 500  # Wrist: 500-horizontal,
    servo3 = 450  # 500: straight out
    servo4 = 1000  # 500: straight out
    servo5 = 750  # 500: straight up
    servo6 = 500  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, 500)
    Board.setBusServoPulse(2, servo2, 500)
    Board.setBusServoPulse(3, servo3, 500)
    Board.setBusServoPulse(4, servo4, 500)
    Board.setBusServoPulse(5, servo5, 500)
    Board.setBusServoPulse(6, servo6, 500)

def high_blow(): #sword raised high
    servo1 = 550  # Gripper: 0-full open, 500-close
    servo2 = 500  # Wrist: 500-horizontal,
    servo3 = 200  # 500: straight out
    servo4 = 500  # 500: straight out
    servo5 = 500  # 500: straight up
    servo6 = 500  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, 500)
    Board.setBusServoPulse(2, servo2, 500)
    Board.setBusServoPulse(3, servo3, 500)
    Board.setBusServoPulse(4, servo4, 500)
    Board.setBusServoPulse(5, servo5, 500)
    Board.setBusServoPulse(6, servo6, 500)

def low_strike(): #sword down low
    servo1 = 550  # Gripper: 0-full open, 500-close
    servo2 = 500  # Wrist: 500-horizontal,
    servo3 = 750  # 500: straight out
    servo4 = 1000  # 500: straight out
    servo5 = 400  # 500: straight up
    servo6 = 500  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, 500)
    Board.setBusServoPulse(2, servo2, 500)
    Board.setBusServoPulse(3, servo3, 500)
    Board.setBusServoPulse(4, servo4, 500)
    Board.setBusServoPulse(5, servo5, 500)
    Board.setBusServoPulse(6, servo6, 500)

def from_the_right(): # sword to the right
    servo1 = 550  # Gripper: 0-full open, 500-close
    servo2 = 300  # Wrist: 500-horizontal,
    servo3 = 450  # 500: straight out
    servo4 = 1000  # 500: straight out
    servo5 = 750  # 500: straight up
    servo6 = 750  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, 500)
    Board.setBusServoPulse(2, servo2, 500)
    Board.setBusServoPulse(3, servo3, 500)
    Board.setBusServoPulse(4, servo4, 500)
    Board.setBusServoPulse(5, servo5, 500)
    Board.setBusServoPulse(6, servo6, 500)

def from_the_left(): # sword to the left
    servo1 = 550  # Gripper: 0-full open, 500-close
    servo2 = 750  # Wrist: 500-horizontal,
    servo3 = 450  # 500: straight out
    servo4 = 1000  # 500: straight out
    servo5 = 750  # 500: straight up
    servo6 = 250  # Base: 500-centered
    Board.setBusServoPulse(1, servo1, 500)
    Board.setBusServoPulse(2, servo2, 500)
    Board.setBusServoPulse(3, servo3, 500)
    Board.setBusServoPulse(4, servo4, 500)
    Board.setBusServoPulse(5, servo5, 500)
    Board.setBusServoPulse(6, servo6, 500)
if __name__ == '__main__':
    arm_kinematics = ArmIK()

    # Board.setBusServoPulse(id, pulse, movetime)
    # driver serial servo rotation to designation position
    # :param id: need to driver servo id
    # :pulse: position
    # :use_time: time required for rotation

