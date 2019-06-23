#!/usr/bin/python

import time
from os import listdir
import subprocess

class Sound:


    def __init__(self, folderpath):
        self.folderpath = folderpath
        mp3_files = [ f for f in listdir('./music') if f[-4:] == '.mp3' ]
        if not len(mp3_files) > 0:
            print("No mp3 files found!")
        self.mp3_files = mp3_files   

    def playAllAudioFile(self):
        print('--- Available mp3 files ---')
        print(mp3_files)
        print('--- Starting Playback ---')

        index = 0
        for mp3_item in mp3_files:
            # print name
            print("--- " + mp3_item + " ---")

            # play file
            subprocess.Popen(["mplayer", './music/' + mp3_item, "-ss", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print('--- Playing ' + mp3_item + ' ---')


            # stop playback (untested code)
            ##subprocess.call(['killall', 'mplayer'])
            ##print('--- stop mp3_item ---')

            time.sleep(2)

    def playAudioFile(mp3_file):
        print('--- mp3 files ---')
        print(mp3_file)
        print('--- Starting Playback ---')

        # play file
        subprocess.Popen(["mplayer", './music/' + mp3_file, "-ss", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print('--- Playing ' + mp3_item + ' ---')

        time.sleep(2)
    

    def stopPlayback(self):
        # stop playback
        subprocess.call(['killall', 'mplayer'])
        print('--- stop mp3_item ---')


