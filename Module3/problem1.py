#!/usr/bin/python
from __future__ import print_function

from __future__ import division

import queue
import signal
import threading
from math import *
from statistics import mean
import time
import gopigo3 
import easygopigo3 as easy

import picamera

import numpy as np

import matplotlib.pyplot as plt
from PIL import Image

from curtsies import Input
from di_sensors import inertial_measurement_unit
from easygopigo3 import *

import csv
import random

gp = EasyGoPiGo3()
gpg_motor = EasyGoPiGo3()

distance = gp.init_distance_sensor()

def loop():
    i = 0
    while(i < 50):
        if(int(format(distance.read_mm())) >= 250):
            gp.drive_cm(1)
            i+=1
            r = 90
        else:
            gp.turn_degrees(180)
            gp.drive_cm(i)
            r = -90
            gp.turn_degrees(r)
            i = 0
            
GPG = gopigo3.GoPiGo3() # Create an instance of the GoPiGo3 class. GPG will be the GoPiGo3 object.

try:
    GPG.offset_motor_encoder(GPG.MOTOR_LEFT, GPG.get_motor_encoder(GPG.MOTOR_LEFT))
    GPG.offset_motor_encoder(GPG.MOTOR_RIGHT, GPG.get_motor_encoder(GPG.MOTOR_RIGHT))
    for i in range(0, 361):
        GPG.set_motor_position(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, i)
        time.sleep(0.01)
    while True:
        for i in range(-360, 361):
            GPG.set_motor_position(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, -i)
            time.sleep(0.01)
        
        for i in range(-360, 361):
            GPG.set_motor_position(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, i)
            time.sleep(0.01)
            
except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    GPG.reset_all()
    
    
my_servo_portSERVO1 = gp.init_servo('SERVO1')            
my_servo_portSERVO2 = gp.init_servo('SERVO2')            
my_servo_portSERVO1.rotate_servo(90)
my_servo_portSERVO2.rotate_servo(90)
loop()