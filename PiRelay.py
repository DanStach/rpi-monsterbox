#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Relay:


    def __init__(self, relaypin, relayname):
        self.pin = relaypin
        self.name = relayname
        GPIO.setup(self.pin,GPIO.OUT)
        GPIO.output(self.pin, GPIO.LOW) #set relay to on by default

    def __exit__(self):
        GPIO.cleanup()

    def on(self):
        print(self.name + " - ON")
        GPIO.output(self.pin,GPIO.LOW)

    def off(self):
        print(self.name + " - OFF")
        GPIO.output(self.pin,GPIO.HIGH)

    def onDelayOff(self, timeSec):
        print(self.name + " - ON")
        GPIO.output(self.pin,GPIO.LOW)
        time.sleep(timeSec)
        print(self.name + " - Off")
        GPIO.output(self.pin,GPIO.HIGH)

    def offDelayOn(self, timeSec):
        print(self.name + " - Off")
        GPIO.output(self.pin,GPIO.HIGH)
        time.sleep(timeSec)
        print(self.name + " - ON")
        GPIO.output(self.pin,GPIO.LOW)
        time.sleep(timeSec)

