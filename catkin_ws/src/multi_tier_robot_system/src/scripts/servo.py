#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32


class Servo(object):

    def __init__(self, nb, orientation="yaw"):
        self.pos = 0
        self.pwm = 0
        self.orientation = orientation
        topic = "buggy" + str(nb) + "/servo0"
        self.publisher = rospy.Publisher(topic, Float32, queue_size=1)

    def _deg2pwm(self):
        self.pwm = self.pos * 500.0 / 90.0 + 1500

    # Publish servo position
    def move(self, pos):
        self.pos = pos
        self._update()
        self.publisher.publish(self.pwm)

    def _update(self):
        self._deg2pwm()
        if self.pwm < 5:
            self.pwm = 5
        elif self.pwm > 10:
            self.pwm = 10
