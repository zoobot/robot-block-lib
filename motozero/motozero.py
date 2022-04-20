import rospy, smbus2, logging,time 
from core.utils import *
# import RPi.GPIO as GPIO
from gpiozero import Motor, OutputDevice
from time import sleep

FORWARD = 1 # Full speed forward
FORWARD_HALF = 0.5 # Half speed forward
BACKWARD = -1 # Full speed backward
BACKWARD_HALF = -0.5 # Half speed backward
STOP = 0 # Stop

# # Define GPIO pins
# MOTOR1A = 24
# MOTOR1B = 27
# MOTOR1_ENABLE = 5
# MOTOR2A = 17
# MOTOR2B = 6
# MOTOR2_ENABLE = 22
# MOTOR3A = 12
# MOTOR3B = 23
# MOTOR3_ENABLE = 16
# MOTOR4A = 25
# MOTOR4B = 13
# MOTOR4_ENABLE = 18

class motozero():
     
    def __init__(self, pins):
        self.init_pins(pins)

        '''
             try:
         
            logg(__name__, "INFO", "Motors successfullly initialised")
        except Exception as e:
            logg(__name__, "ERROR", "Exception initialisitng Motozero Motor Driver {}".format(e))
        
        '''

    def init_pins(self, pins):
        self.motor1 = Motor(pins['motor1a'], pins['motor1b'])
        self.motor1_enable = OutputDevice(pins['motor1_enable'], initial_value=1)

        self.motor2 = Motor(pins['motor2a'], pins['motor2b'])
        self.motor2_enable = OutputDevice(pins['motor2_enable'], initial_value=1)

        self.motor3 = Motor(pins['motor3a'], pins['motor3b'])
        self.motor3_enable = OutputDevice(pins['motor3_enable'], initial_value=1)

        self.motor4 = Motor(pins['motor4a'], pins['motor4b'])
        self.motor4_enable = OutputDevice(pins['motor4_enable'], initial_value=1)

    def circle(self):
        # Turn the motor on
        self.motor1.value = FORWARD
        self.motor3.value = BACKWARD
        self.motor4.value = BACKWARD
        print('circle: ', self.motor1.value, self.motor2.value, self.motor3.value, self.motor4.value)

    def forward(self):
        # Turn the self.motor on
        self.motor1.forward()
        self.motor2.forward()
        self.motor3.forward()
        self.motor4.forward()
        print('forward: ', self.motor1.value, self.motor2.value, self.motor3.value, self.motor4.value)

    def back(self):
        self.motor1.reverse()
        self.motor2.reverse()
        self.motor3.reverse()
        self.motor4.reverse()
        print('back:', self.motor1.value, self.motor2.value, self.motor3.value, self.motor4.value)

    def right(self):
        self.motor1.value = FORWARD
        self.motor2.value = FORWARD
        self.motor3.value = FORWARD_HALF
        self.motor4.value = FORWARD_HALF
        print('right: ', self.motor1.value, self.motor2.value, self.motor3.value, self.motor4.value)

    def left(self):
        self.motor1.value = FORWARD_HALF
        self.motor2.value = FORWARD_HALF
        self.motor3.value = FORWARD
        self.motor4.value = FORWARD
        print('left: ', self.motor1.value, self.motor2.value, self.motor3.value, self.motor4.value)

    def stop(self):
        # Stop the self.motor by 'turning off' the _ENABLE GPIO pin
        self.motor1.stop()
        self.motor2.stop()
        self.motor3.stop()
        self.motor4.stop()
        print('stop: ', self.motor1.value, self.motor2.value, self.motor3.value, self.motor4.value)

    # def disconnect(self):
    #     GPIO.cleanup()
    #     print('disconnect: ', self.motor1.value, self.motor2.value, self.motor3.value, self.motor4.value)

    def update(self, msg):
        # self.circle(self)
        print('update circle it: self, msg', self, msg)