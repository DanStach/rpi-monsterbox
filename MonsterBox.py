# The goal of the monster box is to turn a motor (via relay), 
#  play scary sounds, and flash lights

# RPI3B pin out layout
#
# NeoPixel
#  - Pin04 (5v)
#  - Pin12 (Data) gpi018
#  - Pin14 (ground)
#
# Relay
#  - Pin07 (motor) gpio04
#  - Pin11 (n/a) gpio17
#  - Pin13 (n/a) gpio27
#  - Pin15 (n/a) gpio22


import PiSound    
import PiRelay
import time
import random

# setup Relays
ChannelPin1 = 4
r1 = PiRelay.Relay(ChannelPin1, "RELAY1")

# setup Sounds
folderpath = "./music"
fileExtension = ".mp3"
player = "mplayer"
sound1 = PiSound.Sound(folderpath, fileExtension, player)

random.seed()
for i in range(100):
    print("#### For loop = ", i, " ####")

    # Randomly play sound and open box
    randomPlayNumber = random.randint(0, 100)
    print("## randomPlayNumber = ", randomPlayNumber, " ##")
    if (randomPlayNumber < 50):
        print("## Playing monster box ##")
        sound1.playAllAudioFile(0)
        r1.onDelayOff(10)
        time.sleep(10) #wait for sounds finish

    # wait random time
    randomWaitNumber = random.randint(0, 10)
    print("## randomWaitNumber = ", randomWaitNumber, " ##")
    time.sleep(randomWaitNumber )
    
