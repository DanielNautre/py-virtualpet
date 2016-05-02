#!/usr/bin/python2.7
# -*- coding: utf8 -*


class Pet(object):
    """docstring for Pet"""
    def __init__(self, arg):
        super(Pet, self).__init__()
        self.arg = arg

    def initializeValues(self):
        """ set values when the pet is born"""

        self.age = 0  # age in gametick
        self.hunger = 100  # how hungry is the pet
        self.health = 100  # how healthy is the pet
        self.joy = 50  # set the joy level
        self.love = 0  # how much does your pet love you
