#!/usr/bin/python
# The Sound class helps with MP3 playback

import time
from os import listdir
import subprocess

class Sound:


    def __init__(self, folderpath, fileExtension, playerProgram):
        self.folderpath = folderpath
        self.extension = fileExtension  
        self.player = playerProgram        
      
        # gather a list of mp3 files in the folder
        mp3_files = [ f for f in listdir(self.folderpath) if f[-4:] == self.extension ]
        if not len(mp3_files) > 0:
            print("Sound init: No audio files found!")
        self.mp3_files = mp3_files   

    def playAllAudioFile(self, delaySeconds):
        mp3_files = self.mp3_files 
        print('--- Available audio files ---')
        print(mp3_files)
        print('--- Starting Playback ---')

        index = 0
        for mp3_item in mp3_files:
            # print name
            print("--- " + mp3_item + " ---")

            # play file
            subprocess.Popen([self.player, self.folderpath + "/" + mp3_item, "-ss", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print('--- Playing ' + mp3_item + ' ---')

            time.sleep(delaySeconds)

    def playAudioFile(mp3_file, delaySeconds):
        print('--- audio file ---')
        print(mp3_file)
        print('--- Starting Playback ---')

        # play file
        subprocess.Popen([self.player self.folderpath + "/" + mp3_item, "-ss", "0"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print('--- Playing ' + mp3_item + ' ---')

        time.sleep(delaySeconds)
    
    def stopPlaybackAll(self):
        # stop playback
        subprocess.call(['killall', self.player])
        print('--- stop audio item ---')