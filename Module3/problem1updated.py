import easygopigo3 as easy
import time
from easygopigo3 import *
sensor_readings = None

gpg = easy.EasyGoPiGo3()
gp = EasyGoPiGo3()
my_distance_sensor = gp.init_distance_sensor()

time.sleep(0.1)


# start
my_servo_portSERVO1 = gp.init_servo('SERVO1')            
my_servo_portSERVO2 = gp.init_servo('SERVO2')            
my_servo_portSERVO1.rotate_servo(90)
my_servo_portSERVO2.rotate_servo(180)
i = 0
while(i > 0):
    if(my_distance_sensor.read_mm() <= 250):
        gpg.offset_motor_encoder(gpg.MOTOR_LEFT, gpg.get_motor_encoder(gpg.MOTOR_LEFT))
        gpg.offset_motor_encoder(gpg.MOTOR_RIGHT, gpg.get_motor_encoder(gpg.MOTOR_RIGHT))
        i+=1
        r = 90
    else:
        gp.turn_degrees(180)
        gp.drive_cm(i)
        r = -90
        gp.turn_degrees(r)
        i = 0
while(distance.read_mm() >= 250):
    gpg.turn_degrees(-1*180, blocking=True)
gpg.drive_cm(50, blocking=True)
gpg.turn_degrees(-1*90, blocking=True)

gpg.offset_motor_encoder(gpg.MOTOR_LEFT, gpg.get_motor_encoder(gpg.MOTOR_LEFT))
gpg.offset_motor_encoder(gpg.MOTOR_RIGHT, gpg.get_motor_encoder(gpg.MOTOR_RIGHT))
my_distance_sensor = gpg.init_distance_sensor()
file =open("problem1_pathtrace.csv","a+")
file.write((  "Index : {:i},Current distance : {:i} mm, Motor Encoder L: {:i}, Motor Encoder R: {:i} \r\n".format(count+1,my_distance_sensor.read_mm(),gpg.get_motor_encoder(gpg.MOTOR_RIGHT),gpg.get_motor_encoder(gpg.MOTOR_LEFT),  )))
