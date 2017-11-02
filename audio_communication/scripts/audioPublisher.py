#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import rospy
import os
import wave
from pyaudio import PyAudio, paInt16 
import numpy as np 
import time
from audio_common_msgs.msg import *

def audioPublisher():       
    audioPublisher = rospy.Publisher('android_audioSubscriber', AudioData, queue_size=1)
    dev_to_capture = PyAudio()
    stream = dev_to_capture.open(format = paInt16, channels = 1, rate = 16000, input = True)
    audioData = AudioData()

    while not rospy.is_shutdown():
        audioData.data = stream.read(1280) 
        audioPublisher.publish(audioData)


if __name__=="__main__":
    rospy.init_node('pc_audioPublisher', anonymous=True) 
    audioPublisher()
    print("pc_audioPublisher is over!")