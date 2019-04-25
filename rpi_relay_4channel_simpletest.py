# Simple test for JBtek 4 Channel DC 5V Relay Module on Raspberry Pi
import time
import serial
import RPi.GPIO as GPIO

# Setup GPIO
GPIO.setmode(GPIO.BMC)
GPIO.setwarning(False)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)


# test relay1 on/off
print("relay1 on")
GPIO.output(6,GPIO.HIGH)
time.sleep(3)
print("relay1 off")
GPIO.output(6,GPIO.LOW)
time.sleep(3)

# test relay2 on/off
print("relay2 on")
GPIO.output(13,GPIO.HIGH)
time.sleep(3)
print("relay2 off")
GPIO.output(13,GPIO.LOW)
time.sleep(3)

# test relay3 on/off
print("relay3 on")
GPIO.output(19,GPIO.HIGH)
time.sleep(3)
print("relay3 off")
GPIO.output(19,GPIO.LOW)
time.sleep(3)

# test relay4 on/off
print("relay4 on")
GPIO.output(26,GPIO.HIGH)
time.sleep(3)
print("relay4 off")
GPIO.output(26,GPIO.LOW)
time.sleep(3)