# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from AMSpi import AMSpi
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

# For BOARD pin numbering use AMSpi(True) otherwise BCM is used
with AMSpi(True) as amspi:

i=GPIO.input(3)	#Right IR sensor
k=GPIO.input(16)	#Left IR sensor
j=GPIO.input(12)	#Switch

# Set PINs for controlling shift register (GPIO numbering)
amspi.set_74HC595_pins(40, 38, 36)
# Set PINs for controlling all 4 motors (GPIO numbering)
amspi.set_L293D_pins(29, 31, 33, 35)

while j==1:
    print "Robot Active"

    if i==0:
        print "Obstacle detected on Right",i	#back up
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
        time.sleep(2)
        amspi.run_dc_motors([amspi.DC_Motor_1], clockwise=False)
        time.sleep(2)
        amspi.run_dc_motors([amspi.DC_Motor_2])
        time.sleep(2)
    elif k==0:
        print "Obstacle detected on Left",k	#back up
        amspi.run_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
        time.sleep(2)
        amspi.run_dc_motors([amspi.DC_Motor_1])
        time.sleep(2)
        amspi.run_dc_motors([amspi.DC_Motor_2], clockwise=False)
        time.sleep(2)
    elif i==1 and k==1:
        print "No obstacles detected"	#go forward
        amspi.run_dc_motors([amspi.DC_Motor_1], clockwise=False)
        amspi.run_dc_motors([amspi.DC_Motor_2], clockwise=False)
        time.sleep(2)
    elif j=0:
        print "Robot is off"
        amspi.stop_dc_motors([amspi.DC_Motor_1, amspi.DC_Motor_2])
        GPIO.cleanup()