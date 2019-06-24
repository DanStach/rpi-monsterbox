#!/usr/bin/python
### Sample python code for NeoPixels on Raspberry Pi
### this code is random suggestion for halloween effects from my family, friends, and other examples on the web
### orginal code: https://github.com/DanStach/rpi-ws2811
import time
import board
import neopixel
import random
import math
import serial
import ctypes

class LightWS28XX:

    def __init__(self, pin, pixelNumber, brightness, auto_write, pixelOrder):
        self.pin = pin
        self.pixelNumber = pixelNumber  
        self.brightness = brightness
        self.auto_write = auto_write
        self.pixelOrder = pixelOrder 
        self.pixels = neopixel.NeoPixel(pin, pixelNumber, brightness, auto_write, pixelOrder)

    def HalloweenEyes(red, green, blue, EyeWidth, EyeSpace, Fade, Steps, FadeDelay, EndPause):
        pixels.fill((0,0,0))
        r = 0
        g = 0
        b = 0

        # define eye1 and eye2 location
        StartPoint  = random.randint( 0, num_pixels - (2*EyeWidth) - EyeSpace )
        Start2ndEye = StartPoint + EyeWidth + EyeSpace

        #  set color of eyes for given location
        for i in range(EyeWidth):
            pixels[StartPoint + i] = (red, green, blue)
            pixels[Start2ndEye + i] = (red, green, blue)
        pixels.show()

        # if user wants fading, then fadeout pixel color
        if Fade == True:
            for j in range(Steps, -1, -1):
                r = (j/Steps)*red
                g = (j/Steps)*green
                b = (j/Steps)*blue

                for i in range(EyeWidth):
                    pixels[StartPoint + i] = ((int(r), int(g), int(b)))
                    pixels[Start2ndEye + i] = ((int(r), int(g), int(b)))

                pixels.show()
                time.sleep(FadeDelay)
        
        # Set all pixels to black
        pixels.fill((0,0,0))

        # pause before changing eye location
        time.sleep(EndPause)
