# The goal of the monster box is to turn a motor (via relay), 
#  play scary sounds, and flash lights

import PiSound    
import PiRelay
import time

# setup Relays
ChannelPin1 = 4
relay1 = PiRelay.Relay(ChannelPin1, "RELAY1")

# setup Sounds
folderpath = "./music"
fileExtension = ".mp3"
sound1 = PiSound.Sound(folderpath, fileExtension)

while
    sound1.playAllAudioFile()
    r1.onDelayOff(2)

    time.sleep(5)
    
