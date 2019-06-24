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
       
      
        # gather a list of mp3 files in the folder
        mp3_files = [ f for f in listdir(self.folderpath) if f[-4:] == self.extension ]
        if not len(mp3_files) > 0:
            print("Sound init: No audio files found!")
        self.mp3_files = mp3_files   

    ### colorAll2Color(c1, c2) allows two alternating colors to be shown
    def colorAll2Color(c1, c2):
        for i in range(num_pixels):
            if(i % 2 == 0): # even
                pixels[i] = c1
            else: # odd   
                pixels[i] = c2
        pixels.show()

    ### wheel(pos) will convert value 0 to 255 to get a color value.
    def wheel(pos):
        # Input a value 0 to 255 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 255:
            r = g = b = 0
        elif pos < 85:
            r = int(pos * 3)
            g = int(255 - pos*3)
            b = 0
        elif pos < 170:
            pos -= 85
            r = int(255 - pos*3)
            g = 0
            b = int(pos*3)
        else:
            pos -= 170
            r = 0
            g = int(pos*3)
            b = int(255 - pos*3)
        return (r, g, b) if ORDER == neopixel.RGB or ORDER == neopixel.GRB else (r, g, b, 0)

    def brightnessRGB(red, green, blue, bright):
        r = (bright/256.0)*red
        g = (bright/256.0)*green
        b = (bright/256.0)*blue
        return (int(r), int(g), int(b))

    def FadeInOut(red, green, blue, delay):
        r = 0
        g = 0
        b = 0
        
        for k in range(256):
            r = (k/256.0)*red
            g = (k/256.0)*green
            b = (k/256.0)*blue
            pixels.fill((int(r), int(g), int(b)))
            pixels.show()
            time.sleep(delay)
        
        for k in range(256, -1, -1):
            r = (k/256.0)*red
            g = (k/256.0)*green
            b = (k/256.0)*blue
            pixels.fill((int(r), int(g), int(b)))
            pixels.show()
            time.sleep(delay)
            
            
    def fadeToBlack(ledNo, fadeValue):
        #ctypes.c_uint32 oldColor = 0x00000000UL
        #ctypes.c_uint8 r = 0
        #ctypes.c_uint8 g = 0
        #ctypes.c_uint8 b = 0

        oldColor = pixels[ledNo]
    #    r = (oldColor & 0x00ff0000) >> 16
    #    g = (oldColor & 0x0000ff00) >> 8
    #    b = (oldColor & 0x000000ff)
        #print(oldColor)
    #    r = oldColor >> 16
    #    g = (oldColor >> 8) & 0xff
    #    b = oldColor & 0xff
        r = oldColor[0]
        g = oldColor[1]
        b = oldColor[2]

        if (r<=10):
            r = 0
        else:
            r = r - ( r * fadeValue / 256 )

        if (g<=10):
            g = 0
        else:
            g = g - ( g * fadeValue / 256 )

        if (b<=10):
            b = 0
        else:
            b = b - ( b * fadeValue / 256 )

        pixels[ledNo] = ( int(r), int(g), int(b) )



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
