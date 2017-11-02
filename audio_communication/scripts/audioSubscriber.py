#!/usr/bin/env python
#-*- coding: UTF-8 -*- 

import rospy
import wave
from pyaudio import PyAudio, paInt16 
import numpy as np 
import time
from audio_common_msgs.msg import *

class audioSubscriber:

    def __init__(self):
        rospy.init_node('pc_audioSubscriber', anonymous = True) 
        rospy.Subscriber('android_audioPublisher', AudioData, self.voice_callback, queue_size = 1)
        self.dev_to_play = PyAudio()
        self.stream = self.dev_to_play.open(format = paInt16, channels = 1, rate = 16000, output = True)


    def voice_callback(self, msg):
        try:
            self.stream.write(msg.data)
        except Exception as e:
            print("pc_audioSubscriber is error:"+str(e))



if __name__=="__main__":
    try:
        audioSubscriber()
        rospy.spin()
    except rospy.ROSInterruptException:
        print("pc_audioSubscriber is over!")
