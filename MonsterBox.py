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
import subprocess

# set sound output on RPI to analog (headphones 3.5mm jack)
subprocess.call(['amixer', 'cset', 'numid=3', '1'])

# setup Relays
ChannelPin1 = 4
ChannelPin2 = 11
r1 = PiRelay.Relay(ChannelPin1, "RELAY1")
r2 = PiRelay.Relay(ChannelPin2, "RELAY2")

# setup Sounds
folderpath = "./music"
fileExtension = ".mp3"
player = "mplayer"
sound1 = PiSound.Sound(folderpath, fileExtension, player)

random.seed()
i = 0
while(True):
    i++
    print("#### Playing monster box: loop = ", i, " ####")

    print("### Playing Audio##")
    sound1.playAllAudioFile(0)

    print("### Lights on##")
    r2.on()

    print("### Motor on and off ##")
    r1.onDelayOff(10)
    time.sleep(5) #wait for sounds finish

    print("### Lights off##")
    r2.off()

    # wait random time
    randomWaitNumber = random.randint(0, 10)
    print("## randomWaitNumber = ", randomWaitNumber, " ##")
    time.sleep(randomWaitNumber )
    
