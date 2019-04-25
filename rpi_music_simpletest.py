# Simple test for playing music on Raspberry Pi
# references:
#   - https://raspberrypi.stackexchange.com/questions/7088/playing-audio-files-with-python
#   - https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/master/Playing_Sounds_and_Using_Buttons_with_Raspberry_Pi/simple-jukebox.py
import time
from os import listdir
import subprocess

# get a list of MP3 files
mp3_files = [ f for f in listdir('./music') if f[-4:] == '.mp3' ]
if not len(mp3_files) > 0:
    print("No mp3 files found!")

print('--- Available mp3 files ---')
print(mp3_files)
print('--- Starting Playback ---')

index = 0
for mp3_item in mp3_files
    # print name
    print("--- " + mp3_item + " ---")

    # play file
    ##player = subprocess.Popen(["mplayer", "song.mp3", "-ss", "30"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    subprocess.Popen(['omxplayer', mp3_files[index]])
    print('--- Playing ' + mp3_item + ' ---')


    # stop playback
    ##subprocess.call(['killall', 'omxplayer'])
    ##print('--- mp3_item ---')

    time.sleep(2)
