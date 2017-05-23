#!/usr/bin/env python

import rospy
from multi_tier_robot_system.msg import Drive


class Motors(object):

    def __init__(self, nb):
        self.left = 0
        self.right = 0
        self.left_dir = True
        self.right_dir = True
        self.message = Drive()
        topic = "buggy" + str(nb) + "/drive"
        self.publisher = rospy.Publisher(topic, Drive, queue_size=1)

    def drive(self, cmd):
        self._update(cmd)
        self.message.left = self.left
        self.message.right = self.right
        self.message.left_dir = self.left_dir
        self.message.right_dir = self.right_dir
        self.publisher.publish(self.message)

    def _update(self, cmd):
        left, right = cmd
        self.left = abs(left)
        self.right = abs(right)
        if left < 0:
            self.left_dir = False
        else:
            self.left_dir = True
        if right < 0:
            self.right_dir = False
        else:
            self.right_dir = True
